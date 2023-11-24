<template>
    <div class="home">
        <div class="headerCon">
            <div class="logoSection" id="logo" @click="$router.push('/')">
                <span>Video</span><span style="color: #3500d4">Story</span>
            </div>
            <ProfileMenu :user="user" v-if="!loading" />
        </div>
        <br />

        <div class="loading" v-if="loading">
            <div class="loadingCon">
                <v-progress-circular
                    :size="50"
                    color="primary"
                    indeterminate
                ></v-progress-circular>
            </div>
        </div>
        <div class="error" v-if="error"></div>
        <div class="profileView" v-if="fetched">
            <ProfileView :user="user" />
        </div>
    </div>
</template>

<script>
import ProfileView from "../components/ProfileView.vue";
import ProfileMenu from "../components/ProfileMenu.vue";
import UserAPI from "../apis/UserAPI";
export default {
    name: "Profile",
    async created() {
        if (localStorage.getItem("token")) {
            try {
                this.loading = true;
                this.fetched = false;
                this.error = false;
                let user = await UserAPI.prototype.get_user_data();
                this.user = user;
                setTimeout(() => {
                    this.loading = false;
                    this.fetched = true;
                }, 200);
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
    components: { ProfileView, ProfileMenu },
    data: () => ({
        user: {},
        loading: false,
        fetched: false,
        error: false,
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
    cursor: pointer;
    font-size: 30px;
    font-weight: bold;
}

.loadingCon {
    height: 50vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
