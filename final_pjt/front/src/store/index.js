import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import { createFlashStore } from 'vuex-flash';

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: window.sessionStorage // 세션 저장소로 저장되게 설정
    }),
    createFlashStore()
  ],
  state: {
    mainCheck : true,
    username: "",
    JWTToken: "",
    userpk: "",
    movies: [],
    point : "",
  },
  getters: {
  },
  mutations: {
    MainChange(state) {
      state.mainCheck = false
    },
    SET_JWTTOKEN(state, data) {
      state.JWTToken = data.access
      state.username = data.user.username
      state.userpk = data.user.pk
    },
    DEL_JWTTOKEN(state) {
      state.JWTToken = ""
      state.username = ""
      state.userpk = ""
    }
  },
  actions: {
    signupLogin(context, data) {
      context.commit('SET_JWTTOKEN', data)
    },
    logout(context) {
      context.commit('DEL_JWTTOKEN')
    }
  },
  modules: {
  }
})
