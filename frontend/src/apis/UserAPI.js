import axios from "axios";
const url = "http://localhost:8000/api/users/";

export default class API {
	async login(credentials) {
		const user = await axios.post(url + "login", credentials);
		return user.data;
	}

	async register(credentials) {
		const user = await axios.post(url + "register", credentials);
		return user;
	}

	async get_user_data() {
		axios.defaults.headers.common["Authorization"] =
			"Bearer " + localStorage.getItem("token");
		const user = await axios.get(url + "user_data");
		return user.data;
	}
}
