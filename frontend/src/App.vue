<template>
  <div id="app">
    <section class="hero is-medium is-primary">
      <div class="hero-body">
        <div class="container">
          <div class="columns">
            <div class="column is-8-desktop is-offset-2-desktop">
              <h1 class="title is-2 is-spaced">
                StreamScout
              </h1>
              <h2 class="subtitle is-4">
                  This site and API let's you find URL information on a stream like Twitch or youtube.
              </h2>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-8-desktop is-offset-2-desktop">
            <div class="content">
              <SearchBar></SearchBar>
            </div>

          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>

import SearchBar from './components/SearchBar'

export default {
  name: 'app',
  components: {
    SearchBar
  }
}
</script>

<style>
/*#app {*/
/*  font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
/*  -webkit-font-smoothing: antialiased;*/
/*  -moz-osx-font-smoothing: grayscale;*/
/*  text-align: center;*/
/*  color: #2c3e50;*/
/*  margin-top: 60px;*/
/*}*/
</style>
