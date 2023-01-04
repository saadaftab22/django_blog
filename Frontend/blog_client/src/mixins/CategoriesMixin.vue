<script>
import HTTPErrrorsMixin from './HTTPErrorsMixin.vue';

var categoriesMixin = {
  data() {
    return {
      categories: [],
    }
  },

  mixins: [HTTPErrrorsMixin],

  methods: {
    async getCategoriesAll() {
      try {
        const categoriesResponse = await this.$http.get('http://localhost:8000/api/categories-all/')
        this.categories = categoriesResponse.data
        console.log(this.categories)
      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },

    async getCategories(pageNo = 1) {
      try {
        const categoriesResponse = await this.$http.get(`http://localhost:8000/api/categories/?page=${pageNo}`)
        this.categories = categoriesResponse.data.results
        console.log(this.categories)
      }
      catch (error) {
        this.handleHTTPErrors(error)
      }
    },
  }
}
export default categoriesMixin

</script>