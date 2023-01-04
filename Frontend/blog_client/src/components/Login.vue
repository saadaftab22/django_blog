<template>
  <div class="login">
    <form @submit.prevent="login">
      <div class="container">
        <label><b>Username</b></label>
        <input v-model="user.name" type="text" placeholder="Enter Username" required>

        <label><b>Password</b></label>
        <input v-model="user.password" type="password" placeholder="Enter Password" required>

        <button type="submit">Login</button>
      </div>
    </form>
    <div>
      <p>Don't have an account: <router-link to="/register">Register</router-link></p>
    </div>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';
import HTTPErrrorsMixin from '../mixins/HTTPErrorsMixin.vue';

export default {

  mixins: [
    HTTPErrrorsMixin,
  ],

  data() {
    return {
      // tasks
      user: {
        name: '',
        token: '',
        password: '',
        isAdmin: false,
      },
    };
  },
  methods: {
    async login() {
      try {
        const loginResponse = await this.$http.post("http://localhost:8000/api/api-user-login/", { "username": this.user.name, "password": this.user.password });
        this.user.name = loginResponse.data.username;
        this.user.token = loginResponse.data.token;
        const response = await this.$http.get(`http://localhost:8000/api/profile/`,
          {
            headers: {
              'Authorization': `Token ${this.user.token}`
            }
          });
        
        
        this.user.isAdmin = response.data.is_superuser
        this.$store.commit('setUser', this.user);
        //this.$store.commit('setToken', this.token);
        this.$router.push({ name: 'blogs', query: { page: 1 } })
      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },
  },

  components: { RouterLink }
}
</script>