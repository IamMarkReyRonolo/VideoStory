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
				<v-btn color="#3500D4" dark large to="/update"
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
				<video width="1000" controls>
					<source src="movie.mp4" type="video/mp4" />
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
			v-if="clickedDelete"
			@closeDialog="closeDialog"
		/>
	</div>
</template>

<script>
	import DeleteDialog from "../components/DeleteDialog.vue";
	import VideoAPI from "../apis/VideoAPI";
	export default {
		name: "VideoPlayer",
		components: { DeleteDialog },
		data: () => ({
			clickedDelete: false,
			video: {},
			loading: false,
			fetched: false,
			error: false,
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
				}, 500);
			} catch (error) {
				this.error = true;
				this.loading = false;
			}
		},
		methods: {
			closeDialog() {
				this.clickedDelete = false;
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
