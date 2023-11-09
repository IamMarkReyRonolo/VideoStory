import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import VideoPlayer from "../views/VideoPlayer.vue";
import AddVideo from "../views/AddVideo.vue";
import UpdateVideo from "../views/UpdateVideo.vue";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import NotFound from "../views/NotFound.vue";
Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "home",
		component: HomeView,
	},
	{
		path: "/login",
		name: "login",
		component: Login,
	},
	{
		path: "/register",
		name: "register",
		component: Register,
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
	{
		path: "/update",
		name: "update-video",
		component: UpdateVideo,
	},
	{
		path: "/:notFound",
		component: NotFound,
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;
