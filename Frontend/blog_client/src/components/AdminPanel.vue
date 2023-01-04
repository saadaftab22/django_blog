<template>
  <div class="row tm-catalog-item-list">
    <div v-for="category in this.categories" class="col-lg-4 col-md-6 col-sm-12 tm-catalog-item">
      <div class="position-relative tm-thumbnail-container">
        <a href="video-page.html" class="position-absolute tm-img-overlay">
          <i class="fas fa-play tm-overlay-icon"></i>
        </a>
      </div>
      <div class="p-4 tm-bg-gray tm-catalog-item-description">
        <!-- <router-link :to="{ name: dynamicRoute, params: { id: blog.pk } }"> -->
        <h3 class="tm-text-primary mb-3 tm-catalog-item-title">{{ category.name }}</h3>
        <button @click.prevent="deleteCategory(category.pk)">Delete</button>
        <!-- </router-link> -->
      </div>
    </div>
  </div>

  <div>
    <ul class="nav tm-paging-links">
      <template v-if="showPrevButton" class="nav-item">
        <button @click="loadPrev()">Prev</button>
      </template>

      <template v-if="showNextButton" sclass="nav-item">
        <button @click="loadNext()">Next</button>
      </template>
    </ul>
  </div>
</template>



<script>
import HTTPErrrorsMixin from '../mixins/HTTPErrorsMixin.vue';

export default {

  mixins: [
    HTTPErrrorsMixin,
  ],

  data() {
    return {
      categories: [],
      currentPage: parseInt(this.$route.query.page),
      showNextButton: false,
      showPrevButton: false,
    }
  },

  methods: {
    loadNext() {
      this.currentPage += 1;
      console.log(this.currentPage + 1)
      this.$router.push({ name: 'admin', query: { page: this.currentPage } })
    },

    loadPrev() {
      this.currentPage -= 1;
      this.$router.push({ name: 'admin', query: { page: this.currentPage } })
    },

    determinePage(response) {
      this.showNextButton = false
      this.showPrevButton = false

      if (response.data.next) {
        this.showNextButton = true
      }

      if (response.data.previous) {
        this.showPrevButton = true
      }
    },

    async getCategories(pageNo = 1) {
      try {
        const categoriesResponse = await this.$http.get(`http://localhost:8000/api/categories/?page=${pageNo}`)
        this.categories = categoriesResponse.data.results
        this.determinePage(categoriesResponse)
        console.log(this.categories)
      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },

    async deleteCategory(categoryID) {
      try {
        const response = await this.$http.delete(`http://localhost:8000/api/categories/delete/${categoryID}/`,
          {
            headers: {
              'Authorization': `Token ${this.token}`
            }
          });
        console.log(response);
        const indexOfObject = this.categories.findIndex(object => {
          return object.pk === categoryID;
        });


        this.categories.splice(indexOfObject, 1);
        this.$router.push({ name: 'admin', query: { page: this.currentPage } })

      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },


    reInitialize() {

      this.currentPage = parseInt(this.$route.query.page)
      if (this.currentPage == NaN) {
        this.currentPage = 1
      }
      this.getCategories(this.currentPage)
    },
  },

  computed: {
    token() {
      return this.$store.state.token
    }
  },

  watch: {
    $route: 'reInitialize',
  },


  created() {
    this.getCategories();
    console.log(this.$data)
  },
}
</script>