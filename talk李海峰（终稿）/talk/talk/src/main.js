import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store'
import axios from 'axios'


Vue.prototype.$axios=axios
import $ from 'jquery'
import './plugins/element.js'
Vue.prototype.$=$;
Vue.config.productionTip = false

$.ajaxSetup({
  async:false,
  dataType:"json"
})
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
