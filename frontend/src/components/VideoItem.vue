<template>
	<div class="video-item">
		<div class="videoPlayerSection">
			<v-img
				:width="300"
				src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
			></v-img>
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
		name: "VideoItem",
		components: {},
		data: () => ({}),
	};
</script>

<style scoped>
	.video-item {
		display: flex;
		margin: 0px 0px;
		cursor: pointer;
		padding: 20px;
		border-radius: 10px;
	}

	.video-item:hover {
		background-color: rgb(231, 229, 229);
		transition: 0.4s ease;
	}

	.videoDetailsSection {
		padding: 10px 20px;
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
