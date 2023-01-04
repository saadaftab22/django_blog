<template>
  <div>
    <form>
      <p>
        <input v-model="name" type="text" placeholder="Category name" required />
      </p>
      <div>
        <label>Add Category:</label>
        <input type="submit" @click.prevent="addCategory" />
      </div>
    </form>
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
      name: '',
    }



  },

  methods: {
    async addCategory() {
      try {
        console.log(this.catID);
        const response = await this.$http.post(`http://localhost:8000/api/categories/`, {
          'name': this.name,
        }, {
          headers: {
            'Authorization': `Token ${this.token}`
          }
        });
        console.log(response);

      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },
  },

  computed: {
    token() {
      return this.$store.state.token
    }
  },
}

</script>