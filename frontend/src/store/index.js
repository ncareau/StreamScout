import Vue from "vue";
import Vuex from "vuex";

import stream from "./stream.module";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    stream
  }
});
