<template>
	<div class="video-item">
		<div class="videoPlayerSection">
			<v-img
				:width="300"
				:height="200"
				:src="videoData.thumbnail_url"
				style="
					display: flex;
					justify-content: center;
					align-items: center;
					text-align: center;
					border: 1px solid rgb(150, 150, 150);
					border-radius: 5px;
				"
			>
				<v-icon size="70" dark>mdi-play</v-icon>
			</v-img>
		</div>
		<div class="videoDetailsSection">
			<div class="titleCon">{{ videoData.title }}</div>
			<div class="descriptionCon">
				{{ videoData.description }}
			</div>
			<div class="dateAdded">Added at:{{ getCreatedDate() }}</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: "VideoItem",
		components: {},
		props: {
			videoData: Object,
		},
		data: () => ({}),
		methods: {
			getCreatedDate() {
				var d = new Date(this.videoData.created_at);
				return d.toLocaleDateString("en-US");
			},
		},
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
