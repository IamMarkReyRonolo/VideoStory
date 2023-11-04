import axios from "axios";
const url = "http://localhost:8000/api/videos/";

export default class API {
	async login(credentials) {
		const user = await axios.post(url + "/login", credentials);
		console.log(user);
		return user;
	}

	async upload_video(video_data) {
		const video = await axios.post(url + "upload", video_data);
		return video.data;
	}

	async get_all_videos() {
		const videos = await axios.get(url);
		return videos.data;
	}

	async get_specific_video(id) {
		const video = await axios.get(url + id);
		return video.data;
	}

	async update_videopost(id, data) {
		const video = await axios.put(url + id, data);
		return video.data;
	}

	async delete_videopost(id) {
		const video = await axios.delete(url + id);
		return video.data;
	}
}
