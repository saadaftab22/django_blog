<template>
  <main id="blogs-display">
    <div class="row">
      <div class="col-12">
        <h2 class="tm-page-title mb-4">My Blogs</h2>
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
          <router-link :to="{ name: 'blog-edit', params: { id: blog.pk } }">
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
import HTTPErrrorsMixin from '../mixins/HTTPErrorsMixin.vue';

export default {

  props: ['userData'],

  mixins: [
    HTTPErrrorsMixin,
  ],

  data() {
    return {
      categories: [],
      blogs: [],
      showNextButton: false,
      showPrevButton: false,
      currentPage: this.$route.query.page,
    }
  },

  methods: {

    loadNextFiltered() {
      this.currentPage += 1;
      this.$router.push({ name: 'profile', query: { page: this.currentPage } })
    },

    loadPrevFiltered() {
      this.currentPage -= 1
      this.$router.push({ name: 'profile', query: { page: this.currentPage } })
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

    async getUserBlogs() {
      try {

        const response = await this.$http.get(`http://localhost:8000/api/blogs/user/${this.userData.pk}/`,
          {
            headers: {
              'Authorization': `Token ${this.token}`
            }
          });
        this.blogs = response.data.results;

        console.log(this.blogs)
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
      this.getUserBlogs()
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
    this.getUserBlogs()
  }
}
</script>