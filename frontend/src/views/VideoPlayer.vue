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
				<v-btn color="#3500D4" dark large
					><span style="text-transform: capitalize; font-weight: bold"
						>Edit video</span
					></v-btn
				>
				<v-btn outlined color="error" large
					><span style="text-transform: capitalize; font-weight: bold"
						>Delete Video</span
					></v-btn
				>
			</div>
		</div>
		<div class="videoPlayerSection">
			<video width="1000" controls>
				<source src="movie.mp4" type="video/mp4" />
			</video>
		</div>
		<div class="videoDetailsSection">
			<div class="titleCon">Video Title Number 1</div>
			<div class="descriptionCon">
				Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ipsum nihil
				voluptates saepe exercitationem consectetur odit! Dolor asperiores
				dolores vero magni. Lorem ipsum, dolor sit amet consectetur adipisicing
				elit. Fugit, doloremque?
			</div>
			<div class="dateAdded">Added at: November 3, 2023</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: "VideoPlayer",
		components: {},
		data: () => ({}),
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
</style>
