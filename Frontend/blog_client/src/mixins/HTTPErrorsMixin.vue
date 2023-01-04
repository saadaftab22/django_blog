<script>
var HTTPErrrorsMixin = {
  data() {
    return {

    }
  },

  methods: {
    handleHTTPErrors(error) {
      console.log(error)
      if (error.code == "ERR_NETWORK" || error.response.status == 503) {
        alert('Server Unavailable')
      }
      else if (error.response.status == 400) {
        alert(error.response.data.errors[0].attr + ': ' + error.response.data.errors[0].detail)
      }
      else if (error.response.status == 401) {
        alert(error.response.data.errors[0].code)

      }
      else if (error.response.status == 403) {
        alert(error.response.data.errors[0].detail)

      }
      else if (error.response.status == 404) {
        this.$router.push({ name: 'invalid-page' })
      }
      else if (error.response.status == 500) {
        alert('Server Error')
      }
    }
  }
}
export default HTTPErrrorsMixin

</script>