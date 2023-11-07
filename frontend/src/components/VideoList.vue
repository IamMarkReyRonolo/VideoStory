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
					v-if="this.videos.length != 0"
				></v-text-field>
			</div>
			<div class="video-list-con" v-if="this.filter_videos.length != 0">
				<div
					class="videoCon"
					v-for="(data, index) in this.videos"
					:key="index"
					@click="goTo(data.id)"
				>
					<VideoItem :videoData="data" />
				</div>
			</div>
			<div class="emptyList" v-if="this.filter_videos.length == 0">
				<v-img
					lazy-src="../assets/empty.png"
					max-width="200"
					src="../assets/empty.png"
				></v-img>
				<span style="padding: 10px">You have no videos yet. Upload Now.</span>
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
			loading: false,
			fetched: false,
			error: false,
			videos: [],
			search_word: "",
		}),

		async created() {
			try {
				this.loading = true;
				this.fetched = false;
				const response = await VideoAPI.prototype.get_all_videos();
				setTimeout(() => {
					this.videos = response;
					this.fetched = true;
					this.loading = false;
				}, 500);
			} catch (error) {
				this.error = true;
				this.loading = false;
			}
		},

		watch: {
			search_word() {},
		},

		methods: {
			goTo(id) {
				this.$router.push("/video/" + id);
			},
		},

		computed: {
			filter_videos: function () {
				const filteredVideos = this.videos.filter((video) => {
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
