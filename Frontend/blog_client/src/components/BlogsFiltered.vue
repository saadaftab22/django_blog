<template>
  <main id="blogs-display">
    <div class="row">
      <div class="col-12">
        <h2 class="tm-page-title mb-4">{{ categoryName }}</h2>
        <div class="tm-categories-container mb-5">
          <h3 class="tm-text-primary tm-categories-text">Categories:</h3>
          <ul class="nav tm-category-list">
            <li v-for="category in this.categories" class="nav-item tm-category-item"><a
                @click.prevent="filter(category.pk)" href="#" class="nav-link tm-category-link active">{{
                  category.name
                }}</a></li>
          </ul>
        </div>
      </div>
    </div>

    <div class="row tm-catalog-item-list">
      <div v-for="blog in this.blogs" class="col-lg-4 col-md-6 col-sm-12 tm-catalog-item">
        <div class="position-relative tm-thumbnail-container">
          <a href="video-page.html" class="position-absolute tm-img-overlay">
            <i class="fas fa-play tm-overlay-icon"></i>
          </a>
        </div>
        <div class="p-4 tm-bg-gray tm-catalog-item-description">
          <router-link :to="{ name: 'blog-details', params: { id: blog.pk } }">
            <h3 class="tm-text-primary mb-3 tm-catalog-item-title">{{ blog.title }}</h3>
          </router-link>
          <p class="tm-catalog-item-text">{{ blog.body }}</p>
          <p>Written by: {{ blog.user.username }}</p>
          <div v-for="category in blog.category">
            <p>Categories: {{ category.name }}</p>
          </div>
        </div>
      </div>
    </div>

    <div>
      <ul class="nav tm-paging-links">
        <template v-if="showPrevButton" class="nav-item">
          <button @click="loadPrevFiltered()">Prev</button>
        </template>

        <template v-if="showNextButton" sclass="nav-item">
          <button @click="loadNextFiltered()">Next</button>
        </template>
      </ul>
    </div>
  </main>
</template>

<script>
import categoriesMixin from '@/mixins/CategoriesMixin.vue'
import HTTPErrrorsMixin from '../mixins/HTTPErrorsMixin.vue'


export default {

  mixins: [
    categoriesMixin,
    HTTPErrrorsMixin,
  ],


  data() {
    return {
      blogs: [],
      showNextButton: false,
      showPrevButton: false,
      categoryID: this.$route.params.id,
      categoryName: null,
      currentPage: this.$route.query.page,
    }
  },

  methods: {

    loadNextFiltered() {
      this.currentPage += 1;
      this.$router.push({ name: 'blogs-filtered', query: { page: this.currentPage }, params: { id: this.categoryID } })
    },

    loadPrevFiltered() {
      this.currentPage -= 1
      this.$router.push({ name: 'blogs-filtered', query: { page: this.currentPage }, params: { id: this.categoryID } })
    },


    filter(categoryID) {
      this.$router.push({ name: 'blogs-filtered', query: { page: 1 }, params: { id: categoryID } })
    },

    async getFiltered() {
      try {
        const blogsResponse = await this.$http.get(`http://localhost:8000/api/categories/${this.categoryID}/?page=${this.currentPage}`);
        this.blogs = blogsResponse.data.results;
        this.determinePage(blogsResponse)
      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
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

    reInitialize() {
      this.categoryID = parseInt(this.$route.params.id)
      if (this.categoryID == NaN) {
        this.categoryID = 1
      }
      this.currentPage = parseInt(this.$route.query.page)
      if (this.currentPage == NaN) {
        this.currentPage = 1
      }
      this.getFiltered()
    }

  },

  computed: {
    user() {
      return this.$store.state.user

    },
  },

  watch: {
    $route: 'reInitialize'
  },

  created() {
    this.getCategories();
    this.getFiltered();
  }
}
</script>