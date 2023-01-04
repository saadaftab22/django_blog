<template>
  <div class="position-relative">
    <div class="potition-absolute tm-site-header">
      <div class="container-fluid position-relative">
        <div class="row">
          <div class="tm-site-nav">
            <nav class="navbar navbar-expand-lg mr-0 ml-auto" id="tm-main-nav">
              <ul class="navbar-nav text-uppercase">
                <li class="nav-item active">
                  <router-link :to="{ name: 'blogs', query: { page: 1 } }" class="nav-link tm-nav-link">Blogs<span
                      class="sr-only">(current)</span></router-link>
                </li>
                <template v-if="!isAuthenticated">
                  <li class="nav-item active">
                    <router-link to="/login" class="nav-link tm-nav-link">Login<span
                        class="sr-only">(current)</span></router-link>
                  </li>

                </template>
                <template v-else>
                  <li class="nav-item active">
                    <router-link :to="{ name: 'profile', params: { username: username } }"
                      class="nav-link tm-nav-link">Profile<span class="sr-only">(current)</span></router-link>
                  </li>
                  <li class="nav-item active">
                    <router-link :to="{ name: 'blog-add' }" class="nav-link tm-nav-link">Add Blog<span
                        class="sr-only">(current)</span></router-link>
                  </li>
                  <li class="nav-item active">
                    <router-link :to="{ name: 'category-add' }" class="nav-link tm-nav-link">Add Category<span
                        class="sr-only">(current)</span></router-link>
                  </li>
                  <template v-if="isAdmin">
                    <li class="nav-item active">
                      <router-link :to="{ name: 'admin', query: { page: 1} }" class="nav-link tm-nav-link">Admin<span
                          class="sr-only">(current)</span></router-link>
                    </li>
                  </template>
                </template>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>

    <div id="tm-video-container" class="header-pad">
      <video autoplay muted loop id="tm-video" class="header-pad">
        <source src="video/wheat-field.mp4" type="video/mp4">
      </video>
    </div>

    <i id="tm-video-control-button" class="fas fa-pause"></i>
  </div>
</template>


<script>
export default {

  data() {
    return {
      username: this.$store.state.user
    }
  },
  computed: {
    isAuthenticated() {
      console.log(!!this.$store.state.token)
      return this.$store.state.token
    },

    isAdmin() {
      return this.$store.state.isAdmin
    }
  }
}

</script>


<style>
#header-pad {
  height: 100px;
}
</style>