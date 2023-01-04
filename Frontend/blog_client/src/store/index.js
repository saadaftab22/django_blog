import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";


const store = createStore({
  state() {
    return {
      user: null,
      token: null,
      isAdmin: null,
    }
  },

  actions: {

    // LogIn({ commit }, username, token) {
    //   commit('setUser', username, token)
    // },

    // LogOut({ commit }) {
    //   commit('logout', user)
    // }
  },
  mutations: {
    setUser(state, user) {
      state.user = user.name
      state.token = user.token
      state.isAdmin = user.isAdmin
      console.log(state.user)
      console.log(state.token)
      console.log(state.isAdmin)
    },
    setToken(state, token) {
      console.log(state.token)
    },

    logOutUser(state) {
      state.user = null
      console.log(state.user)
    },

    logOutToken(state) {
      state.token = null
      state.isAdmin = null
      console.log(state.token)
    },
  },

  getters: {
    isAuthenticated: state => !!state.user,
    StateUser: state => state.user,
    StateToken: state => state.token
  },

  plugins: [createPersistedState()]
})

export default store