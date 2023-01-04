<template>
  <div class="tm-page-wrap mx-auto">
    <vue-header></vue-header>
    
    <div id="content" class="mx-auto tm-content-container">
      <div v-if="errorInfo">
        <p>{{ errorInfo }}</p>
      </div>
      <router-view></router-view>
      <subscribe-form></subscribe-form>
      <vue-footer></vue-footer>
    </div>
  </div>
</template>


<script>


import VueHeader from './components/VueHeader.vue'
import blogs from './components/Blogs.vue'
import SubscribeForm from './components/SubscribeForm.vue'
import VueFooter from './components/VueFooter.vue'
import AddBlog from './components/AddBlog.vue'



export default {

  data() {
    return {
      errorInfo: null,
    }
  },
  //name:app,
  components: {
    VueHeader,
    blogs,
    SubscribeForm,
    VueFooter,
    AddBlog,
  },

  errorCaptured(err, vm, info) {
    this.errorInfo = err
    console.log(err)
    return false
  }
}
</script>



<style>

@import './css/bootstrap.min.css';
@import './css/templatemo-video-catalog.css';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
