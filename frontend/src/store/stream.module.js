import { StreamlinkService } from "@/common/api.service";
import {REMOVE_SEARCH_ERROR_ACTION, REFRESH_STREAM_ACTION, REMOVE_STREAM_ACTION, SEARCH_PLUGIN, SEARCH_URL} from "./actions.type";
import {
  SEARCH,
  ADD_STREAM,
  REMOVE_STREAM,
  ADD_SEARCH_ERROR,
  REMOVE_SEARCH_ERROR
} from "./mutations.type";

const state = {
  streams: [],
  isLoading: false,
  searchErrors: []
};

const getters = {
  streams(state) {
    return state.streams;
  },
  isLoading(state) {
    return state.isLoading;
  },
  searchErrors(state) {
    return state.searchErrors;
  },
};

const actions = {
  [SEARCH_PLUGIN]({ commit }, params) {
    commit(SEARCH);
    return StreamlinkService.get(params.plugin, params.name)
      .then(({ data }) => {
        commit(ADD_STREAM, data);
      })
      .catch(error => {
        commit(ADD_SEARCH_ERROR, error)
        throw new Error(error);
      });
  },
  [SEARCH_URL]({ commit }, url) {
    commit(SEARCH);
    return StreamlinkService.query(url)
      .then(({ data }) => {
        commit(ADD_STREAM, data);
      })
      .catch(error => {
        commit(ADD_SEARCH_ERROR, error)
        throw new Error(error);
      });
  },
  [REMOVE_STREAM_ACTION]({ commit }, stream) {
    commit(REMOVE_STREAM, stream);
  },
  [REFRESH_STREAM_ACTION]({ commit }, stream) {
    commit(REMOVE_STREAM, stream);
  },
  [REMOVE_SEARCH_ERROR_ACTION]({commit}, error) {
    commit(REMOVE_SEARCH_ERROR, error)
  }
};

/* eslint no-param-reassign: ["error", { "props": false }] */
const mutations = {
  [REMOVE_STREAM](state, stream) {
    state.streams.splice(state.streams.indexOf(stream), 1)
  },
  [ADD_STREAM](state, stream){
    state.isLoading = false;
    state.streams.unshift(stream)
  },
  [SEARCH](state) {
    state.isLoading = true;
  },
  [ADD_SEARCH_ERROR](state, error) {
    state.searchErrors.unshift(error);
    state.isLoading = false;
  },
  [REMOVE_SEARCH_ERROR](error){
    state.searchErrors.splice(state.searchErrors.indexOf(error) , 1)
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
