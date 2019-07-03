<template>
  <div id="app">
    <TheHeader/>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-8-desktop is-offset-2-desktop">
            <div class="content">
              <SearchBar></SearchBar>
              <div v-if="isLoading" style="text-align: center;margin-bottom: 2em;">
                <div class="fa-2x">
                  <i class="fas fa-circle-notch fa-spin"></i>
                </div>
              </div>
              <div class="margin-bottom: 2em;">
                <div class="notification is-danger" v-for="(error, index) in searchErrors" :key="index">
                  <button class="delete" v-on:click="removeError(error)"></button>
                  {{error}}
                </div>
              </div>
              <div class="card-columns">
                <Stream v-for="(stream, index) in streams"
                        :stream="stream"
                        :key="stream.id + index"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <TheFooter/>
  </div>
</template>

<script>
  import TheHeader from "./components/TheHeader";
  import TheFooter from "./components/TheFooter";

  import SearchBar from "./components/SearchBar";
  import Stream from "./components/Stream";

  import {mapGetters} from "vuex";
  import {REMOVE_SEARCH_ERROR_ACTION} from "./store/actions.type";

  export default {
    name: 'app',

    components: {
      SearchBar,
      Stream,
      TheFooter,
      TheHeader
    },
    computed: {
      ...mapGetters(["isLoading", "streams", "searchErrors"])
    },
    methods: {
      removeError: function(error){
        this.$store.dispatch(REMOVE_SEARCH_ERROR_ACTION, error)
      }
    }

  }


</script>

<style lang="scss">

</style>
