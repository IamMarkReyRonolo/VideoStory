import axios from "axios";
const url = "http://localhost:8000/api/videos/";

export default class API {
	async login(credentials) {
		const user = await axios.post(url + "/login", credentials);
		console.log(user);
		return user;
	}

	async get_all_videos() {
		const videos = await axios.get(url);
		return videos.data;
	}

	async get_specific_video(id) {
		const video = await axios.get(url + id);
		return video.data;
	}
}
