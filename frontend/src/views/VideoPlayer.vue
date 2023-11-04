<template>
	<div class="video-player">
		<div class="headerCon">
			<h2
				style="font-weight: bolder; font-size: 28px; cursor: pointer"
				@click="$router.push('/')"
			>
				🎥 Your Videos
			</h2>
			<div class="controls">
				<v-btn color="#3500D4" dark large @click="updateVideo()"
					><span style="text-transform: capitalize; font-weight: bold"
						>Edit video</span
					></v-btn
				>
				<v-btn outlined color="error" large @click="clickedDelete = true"
					><span style="text-transform: capitalize; font-weight: bold"
						>Delete Video</span
					></v-btn
				>
			</div>
		</div>
		<div class="fetched" v-if="fetched">
			<div class="videoPlayerSection">
				<video width="1000" height="600" controls :poster="video.thumbnail_url">
					<source :src="video.video_url" type="video/mp4" />
				</video>
			</div>
			<div class="videoDetailsSection">
				<div class="titleCon">{{ video.title }}</div>
				<div class="descriptionCon">
					{{ video.description }}
				</div>
				<div class="dateAdded">Added at: {{ video.created_at }}</div>
				<div class="dateAdded">Updated at: {{ video.updated_at }}</div>
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

		<DeleteDialog
			:dialog="clickedDelete"
			:loading="loadingDelete"
			v-if="clickedDelete"
			@confirm="deleteVideoPost"
			@closeDialog="closeDialog"
		/>

		<Snackbar
			:snackbar="snackbar"
			:message="message"
			@closeSnackbar="snackbar = false"
			v-if="snackbar"
		/>
	</div>
</template>

<script>
	import DeleteDialog from "../components/DeleteDialog.vue";
	import VideoAPI from "../apis/VideoAPI";
	import Snackbar from "../components/Snackbar.vue";
	export default {
		name: "VideoPlayer",
		components: { DeleteDialog, Snackbar },
		data: () => ({
			clickedDelete: false,
			video: {},
			loading: false,
			fetched: false,
			error: false,
			loadingDelete: false,
			snackbar: false,
			message: "",
		}),
		async created() {
			try {
				this.loading = true;
				this.fetched = false;
				const response = await VideoAPI.prototype.get_specific_video(
					this.$route.params.id
				);
				setTimeout(() => {
					this.video = response;
					var d = new Date(this.video.created_at);
					var u = new Date(this.video.updated_at);
					this.video.created_at = d.toLocaleDateString("en-US");
					this.video.updated_at = u.toLocaleDateString("en-US");
					this.fetched = true;
					this.loading = false;
				}, 200);
			} catch (error) {
				this.error = true;
				this.loading = false;
			}
		},
		methods: {
			closeDialog() {
				this.clickedDelete = false;
			},

			updateVideo() {
				this.$router.push({
					name: "update-video",
					params: { video_data: this.video },
				});
			},

			async deleteVideoPost() {
				try {
					this.loadingDelete = true;
					const result = await VideoAPI.prototype.delete_videopost(
						this.$route.params.id
					);

					this.loadingDelete = false;
					this.clickedDelete = false;
					this.snackbar = true;
					this.message = "Successfully deleted video";

					setTimeout(() => {
						this.$router.push("/");
					}, 1000);
				} catch (error) {
					this.snackbar = true;
					this.message = "An error occured";
				}
			},
		},
	};
</script>

<style scoped>
	.video-player {
		padding: 10px 20px;
	}
	.headerCon {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 50px;
	}

	.v-btn {
		margin-left: 10px;
	}
	.videoDetailsSection {
		padding: 10px 0px;
	}

	.titleCon {
		font-weight: bold;
		font-size: 24px;
	}

	.descriptionCon,
	.dateAdded {
		font-size: 14px;
		text-align: justify;
		padding: 10px 0px;
	}

	.loadingCon {
		height: 50vh;
		display: flex;
		justify-content: center;
		align-items: center;
	}
</style>
