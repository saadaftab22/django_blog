import { createApp } from 'vue'
import App from './App.vue'
import * as Vue from 'vue' // in Vue 3
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import store from './store'


const app = Vue.createApp(App)
app.use(VueAxios, axios)
app.use(store)
app.use(router)
app.mount('#app')
