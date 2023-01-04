<template>
  <div v-if="blog">
    <h2>{{ blog.title }}</h2>
    <p>{{ blog.body }}</p>
    <p>Written by: {{ blog.user.username }}</p>
    <div v-for="category in blog.category">
      <p>Categories: {{ category.name }}</p>
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
      blog: null,
      blogID: this.$route.params.id
    }
  },

  methods: {

    async getBlog() {
      try {

        const response = await this.$http.get(`http://localhost:8000/api/blogs/${this.blogID}/`);
        this.blog = response.data;
        console.log(this.blog)
      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },

  },

  created() {
    this.getBlog();
  },

}

</script>