<template>
	<div class="home">
		<div class="headerCon">
			<h2 style="font-weight: bolder; font-size: 28px">Your Videos</h2>
			<v-btn color="#3500D4" dark large to="/add"
				><span style="text-transform: capitalize; font-weight: bold"
					>Upload video</span
				></v-btn
			>
		</div>

		<div class="searchCon">
			<v-text-field
				outlined
				placeholder="Search video"
				rounded
				dense
			></v-text-field>
		</div>

		<div class="videoListsCon">
			<VideoList />
		</div>
	</div>
</template>

<script>
	import VideoList from "../components/VideoList.vue";
	export default {
		name: "Home",
		components: { VideoList },
	};
</script>

<style scoped>
	.home {
		padding: 10px 20px;
	}
	.headerCon {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.searchCon {
		margin: 25px auto;
		width: 350px;
	}
</style>
