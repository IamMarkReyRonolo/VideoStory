<template>
	<div class="home">
		<div class="headerCon">
			<div class="logoSection" id="logo">
				<span>Video</span><span style="color: #3500d4">Story</span>
			</div>
			<ProfileMenu :user="user" v-if="!loading" />
		</div>
		<br />
		<div class="headerCon">
			<h2
				style="font-weight: bolder; font-size: 28px; cursor: pointer"
				@click="$router.push('/')"
			>
				🎥 Your Videos
			</h2>
			<v-btn color="#3500D4" dark large to="/add"
				><span style="text-transform: capitalize; font-weight: bold"
					>Upload video</span
				></v-btn
			>
		</div>

		<div class="videoListsCon">
			<VideoList />
		</div>
	</div>
</template>

<script>
	import ProfileMenu from "../components/ProfileMenu.vue";
	import VideoList from "../components/VideoList.vue";
	import UserAPI from "../apis/UserAPI";
	export default {
		name: "Home",
		async created() {
			if (localStorage.getItem("token")) {
				try {
					this.loading = true;
					let user = await UserAPI.prototype.get_user_data();
					this.user = user;
					setTimeout(() => {
						this.loading = false;
					});
				} catch (error) {
					this.$router.push({
						name: "login",
						params: { token_error: error.response.data.detail },
					});
				}
			} else {
				this.$router.push("/login");
			}
		},
		components: { VideoList, ProfileMenu },
		data: () => ({
			user: {},
			loading: false,
		}),
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

	.logoSection {
		font-size: 30px;
		font-weight: bold;
	}
</style>
