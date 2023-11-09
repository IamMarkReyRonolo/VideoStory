<template>
	<div class="loginStaff">
		<v-alert
			outlined
			type="warning"
			v-if="error"
			v-model="error"
			class="mx-auto my-5"
			width="300px"
			dismissible
			>{{ message }}</v-alert
		>
		<div class="wrapperDiv">
			<div class="rightCon">
				<div class="pageDesc">
					<div class="logoSection" id="logo">
						<span>Video</span><span style="color: #3500d4">Story</span>
					</div>
					<div class="sub">Preserve and cherish every moment</div>
				</div>

				<div class="imgCon"><img src="../assets/moments.png" alt="" /></div>
			</div>
			<div class="leftCon">
				<div class="innerWrap">
					<div class="headerSection">
						<div class="sectionTitle">Login</div>
					</div>
					<br />
					<div class="fieldsSection">
						<div class="field">
							<div class="fieldLabel">Email *</div>
							<v-text-field
								outlined
								id="email"
								v-model="user.email"
								:rules="usernameRules"
							></v-text-field>
						</div>

						<div class="field">
							<div class="fieldLabel">Password *</div>
							<v-text-field
								outlined
								id="password"
								v-model="user.password"
								:rules="passwordRules"
								:append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
								:type="show ? 'text' : 'password'"
								@click:append="show = !show"
							></v-text-field>
						</div>
					</div>
					<p
						style="
							padding: 0px 0px;
							margin: 0px;
							font-size: 14px;
							font-weight: 500;
						"
					>
						* means required
					</p>
					<br />
					<div class="ctrlSection">
						<v-btn
							color="#3500D4"
							:dark="validated"
							:disabled="!validated"
							@click="handleLoginEvent()"
							:loading="loading"
							id="logInBtn"
							large
							>Log In</v-btn
						>
					</div>
					<br />
					<p
						style="
							padding: 0px 0px;
							margin: 0px;
							font-size: 14px;
							font-weight: 500;
						"
					>
						Don't have an account?
						<v-btn small text to="/register"
							><span
								style="
									color: #3500d4;
									font-size: 12px;
									text-transform: capitalize;
									font-weight: bolder;
								"
								>Sign up</span
							></v-btn
						>
						instead
					</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import UserAPI from "../apis/UserAPI";
	export default {
		name: "Login",
		data: () => ({
			loading: false,
			fetched: false,
			error: false,
			show: false,
			user: {
				email: "",
				password: "",
			},
			message: "",
			usernameRules: [
				(v) => !!v.trim() || "This field is required",
				(v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || "Email must be valid",
			],
			passwordRules: [(v) => !!v || "This field is required"],
		}),
		created() {
			if (this.$route.params.token_error) {
				this.message = this.$route.params.token_error;
				this.error = true;
			}
			try {
				const token = localStorage.getItem("token");
				if (token) {
					this.$router.push("/");
				}
			} catch (error) {
				console.log(error);
				localStorage.removeItem("token");
			}
		},

		methods: {
			async handleLoginEvent() {
				try {
					this.loading = true;
					const user = await UserAPI.prototype.login(this.user);
					console.log(user);
					localStorage.setItem("token", user.token);
					this.loading = false;
					this.$router.push("/");
				} catch (error) {
					this.loading = false;
					this.error = true;
					this.message = error.response.data.message;
				}
			},
		},
		computed: {
			validated: function () {
				if (this.user.email.trim() == "" || this.user.password.trim() == "") {
					return false;
				}
				if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.user.email)) {
					return false;
				}
				return true;
			},
		},
	};
</script>

<style scoped>
	.wrapperDiv {
		padding: 20px 50px;
		margin: auto;
		display: flex;
		padding-top: 70px;
		justify-content: space-between;
		align-items: center;
	}

	.leftCon {
		width: 40%;
	}

	.rightCon {
		width: 60%;
		/* display: flex;
		justify-content: space-between;
		align-items: flex-start; */
	}

	.leftCon {
		display: flex;
		justify-content: center;
		align-items: flex-start;
	}

	.pageDesc {
		margin-bottom: -150px;
		z-index: 5;
		position: relative;
		margin-left: -50px;
	}

	.logoSection {
		font-size: 40px;
		font-weight: bold;
	}

	.sectionTitle {
		font-size: 32px;
		font-weight: bold;
	}

	.fieldLabel {
		padding-bottom: 10px;
		font-weight: normal;
		font-size: 18px;
	}

	.v-text-field {
		font-size: 18px;
	}

	.imgCon img {
		width: 500px;
	}

	.v-alert {
		position: absolute;
		margin: 0 auto;
		left: 0;
		right: 0;
	}
</style>
