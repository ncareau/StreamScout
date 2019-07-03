import Vue from 'vue'
import App from './App.vue'
import store from "./store";
import VueClipboard from 'vue-clipboard2'

Vue.use(VueClipboard)

import * as filters from './common/filters'

Vue.config.productionTip = false

Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

import ApiService from "./common/api.service";
ApiService.init();

import 'bulma/css/bulma.min.css'
import '@fortawesome/fontawesome-free/css/all.min.css'

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
