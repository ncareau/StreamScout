<template xmlns:v-clipboard="http://www.w3.org/1999/xhtml">
  <div class="card" style="margin-bottom: 2em;">
    <header class="card-header">

      <p class="card-header-title" style="margin-bottom: 0px;">
        <a :href="stream.channel.url" target="_blank"><i :class="pluginIcon"></i> {{stream.channel.url}}</a>
      </p>

      <div class="card-header-icon">
        <div class="tags has-addons">
          <span class="tag">Live</span>
          <span class="tag is-success" v-if="stream.channel.live">Yes</span>
          <span class="tag is-danger" v-if="stream.channel.live === false">No</span>
        </div>
      </div>

<!--      <a href="#" class="card-header-icon" aria-label="more options">-->
<!--        <span class="icon">-->
<!--          <i class="fas fa-sync-alt"></i>-->
<!--        </span>-->
<!--      </a>-->

      <a href="#" class="card-header-icon" aria-label="more options" v-on:click="deleteStream">
        <span class="icon">
          <i class="fas fa-times" aria-hidden="true"></i>
        </span>
      </a>

    </header>
    <div class="card-content">
      <div class="content">

        <table class="table is-striped is-narrow is-fullwidth">

          <tbody>
          <tr v-for="(stream, quality) in stream.streams" v-bind:key="quality">
            <td   style="text-align: right"><span class="tag is-dark">{{quality}}</span></td>
            <td><a :href="stream">{{stream | truncate(80, '...')}} <i class="fas fa-external-link"></i></a></td>
            <td>

              <button class="button is-small is-link"  type="button"
                v-clipboard:copy="stream">Copy</button>
            </td>
          </tr>
          </tbody>

        </table>


      </div>
    </div>
  </div>
</template>

<script>

  import {REMOVE_STREAM_ACTION} from "../store/actions.type";

  export default {
    props: {
      stream: {type: Object, required: true}
    },
    methods: {
      deleteStream: function () {
        this.$store.dispatch(REMOVE_STREAM_ACTION, this.stream)
      }
    },
    computed: {
      pluginIcon(){
        return 'fab fa-'+this.stream.channel.plugin
      }
    }
  }
</script>
