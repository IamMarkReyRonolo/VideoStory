import axios from "axios";
const url = "http://localhost:8000/api/videos/";
export default class API {
	async upload_video(video_data) {
		axios.defaults.headers.common["Authorization"] =
			"Bearer " + localStorage.getItem("token");
		const video = await axios.post(url + "post", video_data);
		return video.data;
	}

	async get_all_videos() {
		axios.defaults.headers.common["Authorization"] =
			"Bearer " + localStorage.getItem("token");
		const videos = await axios.get(url);
		return videos.data.videos;
	}

	async get_specific_video(id) {
		axios.defaults.headers.common["Authorization"] =
			"Bearer " + localStorage.getItem("token");
		const video = await axios.get(url + id);
		return video.data;
	}

	async update_videopost(id, data) {
		axios.defaults.headers.common["Authorization"] =
			"Bearer " + localStorage.getItem("token");
		const video = await axios.put(url + id, data);
		return video.data;
	}

	async delete_videopost(id) {
		axios.defaults.headers.common["Authorization"] =
			"Bearer " + localStorage.getItem("token");
		const video = await axios.delete(url + id);
		return video.data;
	}
}
