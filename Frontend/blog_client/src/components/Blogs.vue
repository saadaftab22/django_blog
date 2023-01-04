<template>
  <main id="blogs-display">
    <div class="row">
      <div class="col-12">
        <h2 class="tm-page-title mb-4">Published Blogs</h2>
        <div class="col-sm-12 mb-4">
          <input type="text" v-model="searchQuery" placeholder="Search Category" />
          <button @click.prevent="search()">Search</button>
          <br />
        </div>
        <div class="tm-categories-container mb-5">
          <h3 class="tm-text-primary tm-categories-text">Categories:</h3>
          <p v-if="noResult">No results</p>
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
          <router-link :to="{ name: dynamicRoute, params: { id: blog.pk } }">
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
          <button @click="loadPrev()">Prev</button>
        </template>

        <template v-if="showNextButton" sclass="nav-item">
          <button @click="loadNext()">Next</button>
        </template>
      </ul>
    </div>
  </main>
</template>

<script>
import categoriesMixin from '@/mixins/CategoriesMixin.vue';
import HTTPErrrorsMixin from '../mixins/HTTPErrorsMixin.vue';


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
      currentPage: parseInt(this.$route.query.page),
      searchQuery: '',
      noResult: false,
    }
  },

  methods: {
    loadNext() {
      this.currentPage += 1;
      console.log(this.currentPage + 1)
      this.$router.push({ name: 'blogs', query: { page: this.currentPage } })
    },

    loadPrev() {
      this.currentPage -= 1;
      this.$router.push({ name: 'blogs', query: { page: this.currentPage } })
    },


    filter(categoryID) {
      this.$router.push({ name: 'blogs-filtered', query: { page: 1 }, params: { id: categoryID } })
    },

    async getBlogs() {
      try {

        const blogsResponse = await this.$http.get(`http://localhost:8000/api/blogs/?page=${this.currentPage}`);
        this.blogs = blogsResponse.data.results;

        console.log(blogsResponse.data)
        this.determinePage(blogsResponse)

      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },



    async search() {
      try {
        const categoriesResponse = await this.$http.get(`http://localhost:8000/api/categories/?search=${this.searchQuery}`);
        this.categories = categoriesResponse.data.results;
        if (this.categories.length == 0) {
          this.noResult = true
          console.log('No results')
        }
        else {
          this.noResult = false
        }
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

      this.currentPage = parseInt(this.$route.query.page)
      if (this.currentPage == NaN) {
        this.currentPage = 1
      }
      this.getBlogs()
    }


  },

  computed: {
    user() {
      return this.$store.state.user
    },

    dynamicRoute() {
      if (this.$store.state.isAdmin) {
        return 'blog-edit'
      }
      else {
        return 'blog-details'
      }
    }
  },

  watch: {
    $route: 'reInitialize'
  },

  created() {
    this.getCategories();
    console.log(this.$data)
    this.getBlogs();
    console.log(this.currentPage);
  }
}
</script>