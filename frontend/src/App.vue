<template>
	<v-app>
		<v-main>
			<router-view />
		</v-main>
	</v-app>
</template>

<script>
	export default {
		name: "App",

		data: () => ({
			//
		}),
	};
</script>

<style>
	#app {
		font-family: "Inter", sans-serif;
		box-sizing: border-box;
		padding: 50px 250px;
	}
</style>
