<template>
    <div class="profile-view">
        <div class="headerCon">
            <h2>Profile View</h2>
            <div class="btnActions">
                <v-btn color="#714ce1" dark @click="clickedUpdate = true"
                    ><span style="text-transform: capitalize"
                        >Update</span
                    ></v-btn
                >
                <v-btn outlined color="error" @click="clickedDelete = true"
                    ><span style="text-transform: capitalize"
                        >Delete</span
                    ></v-btn
                >
            </div>
        </div>

        <div class="mainDetails">
            <div class="imgCon">
                <v-avatar color="#3500d4" style="margin: 20px 0px" size="120">
                    <span class="white--text text-h3">{{
                        this.user.first_name.split("")[0] +
                        this.user.last_name.split("")[0]
                    }}</span>
                </v-avatar>
            </div>
            <div class="profileDetails">
                <div class="field name">
                    {{ this.user.first_name + " " + this.user.last_name }}
                </div>
                <div class="field username">@{{ this.user.username }}</div>
                <div class="field created_at">
                    Joined on:
                    {{
                        new Date(this.user.created_at).toLocaleDateString(
                            "en-US"
                        )
                    }}
                </div>
            </div>
        </div>

        <hr />
        <p style="margin: 20px; font-weight: bold; text-align: center">
            For future use
        </p>

        <DeleteUser
            :dialog="clickedDelete"
            :loading="loadingDelete"
            v-if="clickedDelete"
            @confirm="deleteUser"
            @closeDialog="clickedDelete = false"
        />
        <EditUser
            :dialog="clickedUpdate"
            :loading="loadingUpdate"
            v-if="clickedUpdate"
            :user_details="user"
            @confirmUpdate="updateUser"
            @closeDialog="clickedUpdate = false"
        />
    </div>
</template>

<script>
import UserAPI from "../apis/UserAPI";
import DeleteUser from "./DeleteUser.vue";
import EditUser from "./EditUser.vue";
export default {
    name: "ProfileView",
    props: {
        user: Object,
    },
    components: { DeleteUser, EditUser },
    data: () => ({
        clickedDelete: false,
        loadingDelete: false,
        clickedUpdate: false,
        loadingUpdate: false,
    }),
    methods: {
        async deleteUser() {
            try {
                this.loadingDelete = true;
                const result = await UserAPI.prototype.delete_user(
                    this.user.id
                );
                this.loadingDelete = false;
                localStorage.removeItem("token");
                this.$router.push("/login");
            } catch (error) {
                this.loadingDelete = false;
            }
        },

        async updateUser(user) {
            try {
                this.loadingUpdate = true;
                const result = await UserAPI.prototype.update_user(
                    this.user.id,
                    user
                );
                this.loadingUpdate = false;
                window.location.reload();
            } catch (error) {
                this.loadingUpdate = false;
            }
        },
    },
};
</script>

<style scoped>
.headerCon {
    display: flex;
    justify-content: space-between;
    align-items: centers;
}

.v-btn {
    margin: 0px 5px;
}

.mainDetails {
    padding: 20px 0px;
    width: 400px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    /* margin: 20px auto; */
}

.profileDetails {
    margin: 0px 40px;
}

.name {
    font-size: 28px;
    font-weight: bold;
}

.username {
    font-size: 16px;
    font-style: italic;
}

.created_at {
    font-size: 12px;
}
</style>
