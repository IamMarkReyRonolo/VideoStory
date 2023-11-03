import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import VideoPlayer from "../views/VideoPlayer.vue";
import AddVideo from "../views/AddVideo.vue";
Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "home",
		component: HomeView,
	},
	{
		path: "/video/:id",
		name: "video-player",
		component: VideoPlayer,
	},
	{
		path: "/add",
		name: "add-video",
		component: AddVideo,
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;
