<template>
  <div v-if="blog">
    <form>
      <p>
        <input v-model="blog.title" type="text" placeholder="Title" required />
      </p>
      <p>
        <textarea v-model="blog.body" placeholder="Blog Content" required></textarea>
      </p>
      <div id="selectbox">
        <label>Category</label>
        <select v-model="categoryObj" @change="onChange">
          <option v-for="category in categories" :value="category" required>{{ category.name }}</option>
        </select>
      </div>
      <div>
        <label>Edit Blog: </label>
        <input type="submit" @click.prevent="editBlog" />
      </div>
      <div>
        <button @click.prevent="deleteBlog">Delete Blog</button>
      </div>
    </form>
  </div>
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
      categoryObj: '',
      blogID: this.$route.params.id,
      blog: null,
    }

  },

  methods: {

    async editBlog() {
      try {
        const response = await this.$http.patch(`http://localhost:8000/api/blogs/${this.blog.pk}/`, {
          'title': this.blog.title, 'body': this.blog.body, 'category': this.blog.category.pk,
        }, {
          headers: {
            'Authorization': `Token ${this.token}`
          }
        });
        console.log(response);
        this.$router.push({ name: 'blog-details', params: { id: this.blog.pk } })

      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },

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

    async deleteBlog() {
      try {
        const response = await this.$http.delete(`http://localhost:8000/api/blogs/${this.blog.pk}/`,
          {
            headers: {
              'Authorization': `Token ${this.token}`
            }
          });
        console.log(response);
        this.$router.push({ name: 'blogs', query: { page: 1 } })

      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },

    onChange(event) {
      this.blog.category.pk = this.categoryObj.pk
    },
  },

  computed: {
    token() {
      return this.$store.state.token
    },
    user() {
      return this.$store.state.user
    },
  },
  created() {
    this.getCategoriesAll();
    this.getBlog();
  }
}
</script>



<style>
textarea {
  width: 100vh;
  height: 60vh;
}
</style>