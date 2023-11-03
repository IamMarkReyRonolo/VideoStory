<template>
	<div class="video-list">
		<div class="fetched" v-if="fetched">
			<div class="video-list-con">
				<div
					class="videoCon"
					v-for="(data, index) in this.videos"
					:key="index"
					@click="goTo(data.id)"
				>
					<VideoItem />
				</div>
			</div>
		</div>
		<div class="loading" v-if="loading"></div>
		<div class="error" v-if="error"></div>
	</div>
</template>

<script>
	import VideoItem from "./VideoItem.vue";
	export default {
		name: "VideoList",
		components: { VideoItem },
		data: () => ({
			loading: false,
			fetched: false,
			error: false,
			videos: [
				{ id: "1", name: "Heyyy" },
				{ id: "2", name: "Yow" },
				{ id: "3", name: "Yow" },
			],
		}),

		created() {
			try {
				this.loading = true;
				this.fetched = false;

				// code here

				this.fetched = true;
				this.loading = false;
			} catch (error) {
				this.error = true;
				this.loading = false;
			}
		},

		methods: {
			goTo(id) {
				this.$router.push("/video/" + id);
			},
		},
	};
</script>

<style scoped></style>
