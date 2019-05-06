<template>
    <div>
        <h3>Paste stream URL or enter stream ID.</h3>
        <div>
            <div class="field has-addons">

                <div class="control has-icons-left">
                    <div class="select">
                        <select>
                            <option>Paste URL</option>
                            <option value="twitch.tv">Twitch</option>
                            <option value="twitch.tv">Youtube</option>
                        </select>
                    </div>
                    <div class="icon is-left">
                        <i class="" v-bind:class="[siteIcon]"></i>
                    </div>
                </div>

                <p class="control is-expanded">
                    <input v-model="search_text" v-on:change="checkinput" class="input" type="text"
                           placeholder="URL or Stream ID">
                </p>
                <p class="control">
                    <a class="button" v-on:click="search">
                        Search
                    </a>
                </p>
            </div>
        </div>


        <div>
            <div class="card" v-if="result.url">
                <header class="card-header">
                    <p class="card-header-title">

                        <a :href="result.full_url" target="_blank">{{result.url}}</a>
                    </p>

                    <!--                    <a href="#" class="card-header-icon" aria-label="more options">-->
                    <!--      <span class="icon">-->
                    <!--        <i class="fas fa-angle-down" aria-hidden="true"></i>-->
                    <!--            Offline-->
                    <!--      </span>-->


                    <!--    </a>-->
                    <!--                    <a href="#" class="card-header-icon" aria-label="more options">-->
                    <!--      <span class="icon">-->
                    <!--        <i class="fas fa-angle-down" aria-hidden="true"></i>-->
                    <!--      </span>-->
                    <!--                        Live-->
                    <!--    </a>-->
                </header>
                <div class="card-content">
                    <div class="content">
                        <!--                        <div v-for="(stream, quality) in result.streams">-->
                        <!--                            {{ quality }}: {{ stream }}-->
                        <!--                        </div>-->


                        <div class="field is-grouped is-grouped-multiline">

                            <div class="control" v-for="(stream, quality) in result.streams">
                                <div class="tags has-addons">
                                    <span class="tag is-dark is-medium">{{quality}}</span>
                                    <span class="tag is-info is-medium">
                                        <a :href="stream"><i class="far fa-clipboard"></i> copy</a>
                                    </span>
                                </div>
                            </div>

                        </div>

                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>

    import axios from "axios";

    export default {
        name: "SearchBar",


        data() {
            return {
                url: '',
                full_url: '',
                search_text: '',
                site: '',
                user: '',
                errors: [],
                result: {
                    url: '',
                    full_url: '',
                    streams: {}
                },
                siteIcon: 'fas fa-globe'
            }
        },

        methods: {
            search: function () {


                var bodyFormData = new FormData();
                bodyFormData.set('url', this.url)

                this.result.url = this.url
                this.result.full_url = this.full_url

                axios.get('http://127.0.0.1:8000/' + this.site + '/' + this.user)
                    .then(response => (this.result.streams = response.data.data.streams))


                    .catch(function (response) {
                        //handle error
                        console.log(response);
                    });
            },
            checkinput: function () {
                var text = this.search_text

                text = text.replace(/(^\w+:|^)\/\//, '')

                text = text.split('/')

                switch (text[0]) {
                    case 'twitch.tv':
                    case 'www.twitch.tv':
                        this.changesite('twitch')
                        this.user = text[1]
                        this.url = 'twitch.tv/' + this.user
                        this.full_url = 'https://twitch.tv/' + this.user
                        break
                }

                console.log(text)
                console.log(this.site)


            },
            changesite: function (site) {

                this.site = site
                switch (site) {
                    case 'twitch':
                        this.siteIcon = 'fab fa-twitch'
                }
            }

        },

    }
</script>

<style scoped>

</style>