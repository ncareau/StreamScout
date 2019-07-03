<template>
  <div>
    <h3>Paste stream URL or enter stream ID.</h3>
    <div>
      <div class="field has-addons">

         <p class="control">
          <a class="button is-static">
            Paste URL :
          </a>
        </p>

<!--        <div class="control has-icons-left">-->
<!--          <div class="select">-->
<!--            <select>-->
<!--              <option>Paste URL</option>-->
<!--              <option value="twitch.tv" :selected="plugin === 'twitch'">Twitch</option>-->
<!--              <option value="youtube.com" :selected="plugin === 'youtube'">Youtube</option>-->
<!--            </select>-->
<!--          </div>-->
<!--          <div class="icon is-left">-->
<!--            <i style="color: #4a4a4a" v-bind:class="[siteIcon]"></i>-->
<!--          </div>-->
<!--        </div>-->

        <p class="control is-expanded">
          <input v-model="search_text" v-on:change="checkinput" class="input" type="text" >
        </p>
        <p class="control">
          <a class="button" v-on:click="search" :disabled="isLoading">
            Search
          </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>

  import {SEARCH_URL} from "../store/actions.type";
  import { mapGetters } from "vuex";

  export default {
    name: "SearchBar",

    data() {
      return {
        urlLoading: '',
        search_text: '',
        plugin: '',
        pluginIcon: 'fas fa-globe'
      }
    },
    computed:{
      ...mapGetters(["isLoading"])
    },
    methods: {
      search: function () {
        if (this.isLoading){
          return
        }

        this.urlLoading = this.search_text;

        this.$store.dispatch(SEARCH_URL, this.search_text)
      },
      checkinput: function () {
        var text = this.search_text

        text = text.replace(/(^\w+:|^)\/\//, '')
        text = text.split('/')

        switch (text[0]) {
          case 'twitch.tv':
          case 'www.twitch.tv':
            this.plugin = 'twitch'
            this.siteIcon = 'fab fa-twitch'
            break
          case 'www.youtube.com':
            this.plugin = 'youtube'
            this.siteIcon = 'fab fa-youtube'
            break
        }

      }

    }

  }
</script>

<style scoped>

</style>
