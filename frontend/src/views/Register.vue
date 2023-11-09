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
		<v-alert
			outlined
			type="success"
			v-if="successful"
			v-model="successful"
			class="mx-auto my-5"
			width="400px"
			dismissible
			>{{ message }}</v-alert
		>
		<div class="wrapperDiv" v-if="!refresh">
			<div class="leftCon">
				<div class="innerWrap">
					<div class="headerSection">
						<div class="sectionTitle">Register</div>
					</div>
					<br />
					<div class="fieldsSection">
						<div class="field">
							<div class="fieldLabel">First Name *</div>
							<v-text-field
								dense
								outlined
								id="fname"
								v-model="user.first_name"
								:rules="fieldRules"
							></v-text-field>
						</div>
						<div class="field">
							<div class="fieldLabel">Last Name *</div>
							<v-text-field
								dense
								outlined
								id="email"
								v-model="user.last_name"
								:rules="fieldRules"
							></v-text-field>
						</div>
						<div class="field">
							<div class="fieldLabel">Email *</div>
							<v-text-field
								dense
								outlined
								id="email"
								v-model="user.email"
								:rules="usernameRules"
							></v-text-field>
						</div>

						<div class="field">
							<div class="fieldLabel">Password *</div>
							<v-text-field
								dense
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
							@click="handleSignupEvent()"
							:loading="loading"
							id="logInBtn"
							large
							>Sign up</v-btn
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
						Have an account?
						<v-btn small text to="/login"
							><span
								style="
									color: #3500d4;
									font-size: 12px;
									text-transform: capitalize;
									font-weight: bolder;
								"
								>Log in</span
							></v-btn
						>
						instead
					</p>
				</div>
			</div>
			<div class="rightCon">
				<div class="pageDesc">
					<div class="logoSection" id="logo">
						<span>Video</span><span style="color: #3500d4">Story</span>
					</div>
					<div class="sub">Preserve and cherish every moment</div>
				</div>

				<div class="imgCon"><img src="../assets/moments.png" alt="" /></div>
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
			successful: false,
			refresh: false,
			show: false,
			user: {
				first_name: "",
				last_name: "",
				email: "",
				password: "",
			},
			message: "",
			fieldRules: [(v) => !!v || "This field is required"],
			usernameRules: [
				(v) => !!v.trim() || "This field is required",
				(v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || "Email must be valid",
			],
		}),
		created() {
			if (this.$route.params.token_error) {
				this.message = this.$route.params.token_error;
				this.error = true;
			}
			try {
				const token = JSON.parse(localStorage.getItem("token"));
				if (token) {
					this.$router.push("/");
				}
			} catch (error) {
				localStorage.removeItem("token");
			}
		},

		methods: {
			async handleSignupEvent() {
				try {
					this.loading = true;
					const user = await UserAPI.prototype.register(this.user);
					this.message = user.data.message;
					this.successful = true;

					this.error = false;
					this.loading = false;
					this.user = {
						first_name: "",
						last_name: "",
						email: "",
						password: "",
					};
					this.refresh = true;
					setTimeout(() => {
						this.refresh = false;
					}, 200);
				} catch (error) {
					this.successful = false;
					this.loading = false;
					this.error = true;
					if (error.response.data.hasOwnProperty("message")) {
						this.message = error.response.data.message;
					} else {
						this.message = error.response.data.email[0];
					}
				}
			},
		},
		computed: {
			validated: function () {
				if (
					this.user.first_name == "" ||
					this.user.last_name == "" ||
					this.user.email.trim() == "" ||
					this.user.password.trim() == ""
				) {
					return false;
				}
				if (this.passwordRules[0] != true) {
					console.log("password");
					return false;
				}
				if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.user.email)) {
					return false;
				}
				return true;
			},

			passwordRules: function () {
				if (this.user.password == "") {
					return ["Required"];
				}

				if (this.user.password.length > 30) {
					return ["Exceeded number of characters"];
				}

				if (this.user.password.length < 8) {
					return ["Minimum of 8 characters"];
				}

				if (!/^(?=.*?[a-z])/.test(this.user.password)) {
					return ["Password must have lowercase letter."];
				}

				if (!/^(?=.*?[A-Z])/.test(this.user.password)) {
					return ["Password must have uppercase letter."];
				}

				if (!/^(?=.*?[0-9])/.test(this.user.password)) {
					return ["Password must have a number."];
				}

				if (!/^(?=.*?[#?!@$%^&*-])/.test(this.user.password)) {
					return ["Password must have a character."];
				}

				return [true];
			},
		},
	};
</script>

<style scoped>
	.wrapperDiv {
		padding: 0px 50px;
		margin: auto;
		display: flex;
		padding-top: 20px;
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
		text-align: right;
	}

	.pageDesc {
		text-align: left;
		padding-left: 100px;
		margin-bottom: -150px;
		z-index: 5;
		position: relative;
	}

	.leftCon {
		display: flex;
		justify-content: center;
		align-items: flex-start;
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
		z-index: 1;
	}

	.v-alert {
		position: absolute;
		margin: 0 auto;
		left: 0;
		right: 0;
	}
</style>
