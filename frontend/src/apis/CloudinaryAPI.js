import axios from "axios";
const url = "https://api.cloudinary.com/v1_1/markuscloud/";
export default class API {
	async uploadImage(data) {
		delete axios.defaults.headers.common["Authorization"];
		const response = await axios.post(url + "image/upload", data);
		return response.data;
	}

	async uploadVideo(data) {
		delete axios.defaults.headers.common["Authorization"];
		const response = await axios.post(url + "video/upload", data);
		return response.data;
	}
}
