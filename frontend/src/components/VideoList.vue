<template>
    <div class="video-list">
        <div class="fetched" v-if="fetched">
            <div class="searchCon">
                <v-text-field
                    outlined
                    placeholder="Search video"
                    rounded
                    dense
                    v-model="search_word"
                    v-if="this.videos.results.length != 0"
                ></v-text-field>
            </div>
            <div class="video-list-con" v-if="this.filter_videos.length != 0">
                <p style="font-weight: bold; font-size: 14px">
                    {{ videos.count }} total videos
                </p>
                <div
                    class="videoCon"
                    v-for="(data, index) in this.filter_videos"
                    :key="index"
                    @click="goTo(data.id)"
                >
                    <VideoItem :videoData="data" />
                </div>
                <div class="text-center" style="padding-top: 100px">
                    <v-pagination
                        v-model="videos.page_num"
                        :length="
                            Math.floor(videos.count / videos.page_size) + 1
                        "
                        :total-visible="7"
                    ></v-pagination>
                </div>
            </div>
            <div class="emptyList" v-if="this.filter_videos.length == 0">
                <v-img
                    lazy-src="../assets/empty.png"
                    max-width="200"
                    src="../assets/empty.png"
                ></v-img>
                <span style="padding: 10px"
                    >You have no videos yet. Upload Now.</span
                >
            </div>
        </div>
        <div class="loading" v-if="loading">
            <div class="loadingCon">
                <v-progress-circular
                    :size="50"
                    color="primary"
                    indeterminate
                ></v-progress-circular>
            </div>
        </div>
        <div class="error" v-if="error"></div>
    </div>
</template>

<script>
import VideoItem from "./VideoItem.vue";
import VideoAPI from "../apis/VideoAPI";
export default {
    name: "VideoList",
    components: { VideoItem },
    data: () => ({
        page: 1,
        loading: false,
        fetched: false,
        error: false,
        videos: {},
        search_word: "",
    }),

    async created() {
        await this.fetchAllVideos();
    },

    watch: {
        search_word() {},
        async "videos.page_num"() {
            await this.fetchAllVideos(this.videos.page_num);
        },
    },

    methods: {
        goTo(id) {
            this.$router.push("/video/" + id);
        },
        async fetchAllVideos(page_num = 1) {
            try {
                console.log(page_num);
                this.loading = true;
                this.fetched = false;
                const response = await VideoAPI.prototype.get_all_videos(
                    page_num
                );
                setTimeout(() => {
                    this.videos = response;
                    this.fetched = true;
                    this.loading = false;
                    window.scrollTo({
                        top: 0,
                        behavior: "smooth", // Optional: for smooth scrolling
                    });
                }, 400);
            } catch (error) {
                this.error = true;
                this.loading = false;
            }
        },
    },

    computed: {
        filter_videos: function () {
            const filteredVideos = this.videos.results.filter((video) => {
                const title = video.title.toLowerCase();
                let filterWord = this.search_word.toLowerCase();
                return title.includes(filterWord);
            });

            return filteredVideos;
        },
    },
};
</script>

<style scoped>
.loadingCon {
    height: 50vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.emptyList {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-top: 100px;
}

.searchCon {
    margin: 25px auto;
    width: 350px;
}
</style>
