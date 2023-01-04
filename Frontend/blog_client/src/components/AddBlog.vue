<template>
  <div>
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
          <option v-for="category in categories" :value="category">{{ category.name }}</option>
        </select>
      </div>
      <div>
        <label>Add Blog</label>
        <input type="submit" @click.prevent="saveBlog" />
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

      blog: {
        title: '',
        body: '',
        categoryID: [],
      },
      categoryObj: [],


    }

  },

  methods: {

    async saveBlog() {
      try {
        const response = await this.$http.post(`http://localhost:8000/api/blogs/`, {
          'title': this.blog.title, 'body': this.blog.body, 'category': this.blog.categoryID
        },
          {
            headers: {
              'Authorization': `Token ${this.token}`
            }
          });
        console.log(response);
        this.$router.push({ name: 'blog-details', params: { id: response.data.pk } })
      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },

    onChange(event) {
      this.blog.categoryID.push(this.categoryObj.pk)
    }
  },

  computed: {
    token() {
      console.log(this.$store.state.token)
      return this.$store.state.token
    },
  },
  created() {
    this.getCategoriesAll();
  }
}
</script>



<style>
textarea {
  width: 100vh;
  height: 60vh;
}
</style>