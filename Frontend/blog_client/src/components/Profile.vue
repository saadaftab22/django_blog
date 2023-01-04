<template>
  <div>
    <div class="row">
      <div v-if="userData" class="col-12">
        <h2 class="tm-page-title mb-4">{{ user }}'s Profile</h2>
        <p>First Name: {{ userData.first_name }}</p>
        <p>Last Name: {{ userData.last_name }}</p>
        <p>Email: {{ userData.email }}</p>
      </div>
    </div>
  </div>
  <BlogsUser v-if="userData" :user-data="userData"></BlogsUser>

  <router-link :to="{ name: 'blogs', query: { page: 1 } }" @click="logout"><button>Logout</button></router-link>
</template>

<script>
import router from '@/router';
import { RouterLink } from 'vue-router';
import BlogsUser from './BlogsUser.vue'
import HTTPErrrorsMixin from '../mixins/HTTPErrorsMixin.vue';

export default {

  mixins: [
    HTTPErrrorsMixin,
  ],

  data() {
    return {
      userData: null,
      blogs: [],
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    },
    token() {
      return this.$store.state.token
    }
  },

  methods: {
    logout() {
      this.$store.commit('logOutUser');
      this.$store.commit('logOutToken');
    },

    async getUserData() {
      try {

        const response = await this.$http.get(`http://localhost:8000/api/profile/`,
          {
            headers: {
              'Authorization': `Token ${this.token}`
            }
          });
        this.userData = response.data;
        console.log(response.data)
        //this.getUserBlogs()

      }

      catch (error) {
        this.handleHTTPErrors(error)
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
        this.blogs = response.data;

        console.log(response.data)
      }

      catch (error) {
        this.handleHTTPErrors(error)
      }
    }
  },

  components: {
    RouterLink,
    BlogsUser,
  },

  created() {
    this.getUserData()
  }
}
</script>