<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-5">
        <div class="card">
          <h2 class="card-title text-center">Register New User</h2>
          <div class="card-body py-md-4">
            <form @submit.prevent="register" _lpchecked="1">
              <div class="form-group">
                <input v-model="user.firstname" type="text" class="form-control" placeholder="First Name" required>
              </div>
              <div class="form-group">
                <input v-model="user.lastname" type="text" class="form-control" placeholder="Last Name" required>
              </div>
              <div class="form-group">
                <input v-model="user.name" type="text" class="form-control" placeholder="Username" required>
              </div>
              <div class="form-group">
                <input v-model="user.email" type="email" class="form-control" placeholder="Email" required>
              </div>
              <div class="form-group">
                <input v-model="user.password" type="password" class="form-control" placeholder="Password" required>
              </div>
              <div class="form-group">
                <input v-model="user.password2" type="password" class="form-control" placeholder="confirm-password" required>
              </div>
              <div class="d-flex flex-row align-items-center justify-content-between">
                <button class="btn btn-primary">Create Account</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
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
      user: {
        name: "",
        firstname: "",
        lastname: "",
        email: "",
        password: "",
        password2: "",
        token: "",
        isAdmin: false,
      }
    };
  },
  methods: {
    async register() {
      try {
        const registerResponse = await this.$http.post("http://localhost:8000/api/api-user-register/", { "first_name": this.user.firstname, "last_name": this.user.lastname, "username": this.user.name, "email": this.user.email, "password": this.user.password, "password2": this.user.password2 });
        console.log(registerResponse.data);
        this.user.name = registerResponse.data.username;
        this.user.token = registerResponse.data.token;
        this.user.isAdmin = registerResponse.data.is_superuser
        this.$store.commit('setUser', this.user);
        this.$router.push('/login');
        console.log(this.user.name);
        console.log(this.user.token);
      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },
  },
}

</script>