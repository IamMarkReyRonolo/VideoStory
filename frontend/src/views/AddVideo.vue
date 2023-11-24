<template>
    <div class="add-video">
        <div class="headerCon">
            <h2
                style="font-weight: bolder; font-size: 28px; cursor: pointer"
                @click="$router.push('/')"
            >
                🎥 Your Videos
            </h2>
            <v-btn
                color="#3500D4"
                large
                @click="saveVideo()"
                :disabled="!validateFields"
                :dark="validateFields"
                ><span style="text-transform: capitalize; font-weight: bold"
                    >Post video</span
                ></v-btn
            >
        </div>
        <div class="addVideoCon" v-if="!resetData">
            <div class="section">
                <div class="fieldCon fileSection">
                    <div
                        class="fieldLabel"
                        style="font-weight: bold; padding: 5px 0px"
                    >
                        Video
                    </div>
                    <input
                        type="file"
                        accept="video/*"
                        @change="handleFileUpload($event)"
                    />
                </div>
                <div class="fieldCon fileSection">
                    <div
                        class="fieldLabel"
                        style="font-weight: bold; padding: 5px 0px"
                    >
                        Thumbnail
                    </div>
                    <input
                        type="file"
                        name="thumbnail"
                        accept="image/png, image/jpeg"
                        @change="onFileChange"
                    />
                </div>
                <div class="fieldCon">
                    <div
                        class="fieldLabel"
                        style="font-weight: bold; padding: 5px 0px"
                    >
                        Title
                    </div>
                    <v-text-field
                        outlined
                        clearable
                        v-model="title"
                    ></v-text-field>
                </div>

                <div class="fieldCon">
                    <div
                        class="fieldLabel"
                        style="font-weight: bold; padding: 5px 0px"
                    >
                        Description
                    </div>
                    <v-textarea
                        outlined
                        no-resize
                        v-model="description"
                    ></v-textarea>
                </div>
            </div>
            <div class="section">
                <h2 style="font-weight: bolder; font-size: 28px">Preview</h2>
                <div class="videoPlayerSection">
                    <video
                        id="video-preview"
                        width="450px"
                        height="250px"
                        controls
                        v-show="this.videoData != ''"
                        :poster="thumbnail"
                    />
                </div>
                <div class="videoDetailsSection">
                    <div class="titleCon">{{ title ? title : "No Title" }}</div>
                    <div class="descriptionCon">
                        {{ description ? description : "No description" }}
                    </div>
                </div>
            </div>
        </div>

        <SavingModal :dialog="clickedSaved" v-if="clickedSaved" />
        <Snackbar
            :snackbar="snackbar"
            :message="message"
            @closeSnackbar="snackbar = false"
            v-if="snackbar"
        />
    </div>
</template>

<script>
import SavingModal from "../components/SavingModal.vue";
import CloudinaryAPI from "../apis/CloudinaryAPI";
import VideoAPI from "../apis/VideoAPI";
import UserAPI from "../apis/UserAPI";
import Snackbar from "../components/Snackbar.vue";
export default {
    name: "AddVideo",
    components: { SavingModal, Snackbar },
    data: () => ({
        video: "",
        thumbnail: "",
        title: "",
        description: "",
        clickedSaved: false,
        resetData: false,
        videoData: null,
        thumbnailImage: null,
        validated: false,
        snackbar: false,
        message: "",
    }),
    async created() {
        if (localStorage.getItem("token")) {
            try {
                let user = await UserAPI.prototype.get_user_data();
                console.log(user);
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
    methods: {
        onFileChange(e) {
            const file = e.target.files[0];
            if (file) {
                this.thumbnail = URL.createObjectURL(file);
                this.thumbnailImage = file;
            } else {
                this.thumbnail = "";
                this.thumbnailImage = null;
            }
        },

        handleFileUpload(event) {
            const file = event.target.files[0];
            if (file) {
                this.videoData = file;
                this.previewVideo();
            } else {
                this.videoData = null;
                let video = document.getElementById("video-preview");
                video.src = null;
            }
        },
        previewVideo() {
            let video = document.getElementById("video-preview");
            let reader = new FileReader();

            reader.readAsDataURL(this.videoData);
            reader.addEventListener("load", function () {
                video.src = reader.result;
            });
        },

        async saveVideo() {
            try {
                this.clickedSaved = true;
                let video_post = {
                    title: this.title,
                    description: this.description,
                    video_url: null,
                    thumbnail_url: null,
                };

                video_post.video_url = await this.uploadFile(
                    this.videoData,
                    "video"
                );
                video_post.thumbnail_url = await this.uploadFile(
                    this.thumbnailImage,
                    "thumbnail"
                );

                const result = await VideoAPI.prototype.upload_video(
                    video_post
                );
                this.clickedSaved = false;
                this.snackbar = true;
                this.message = result.message;
                this.reset();
            } catch (error) {
                this.snackbar = true;
                this.message = "An error occured";
            }
        },

        reset() {
            this.video = "";
            this.thumbnail = "";
            this.title = "";
            this.description = "";
            this.resetData = true;
            setTimeout(() => {
                this.clickedSaved = false;
                this.resetData = false;
            }, 200);
        },

        async uploadFile(file, file_type) {
            if (file_type == "video") {
                let formData = new FormData();
                formData.append("file", file);
                formData.append("upload_preset", "video-app");
                const result = await CloudinaryAPI.prototype.uploadVideo(
                    formData
                );
                if (result) {
                    return result.secure_url;
                }
            }

            if (file_type == "thumbnail") {
                let formData = new FormData();
                formData.append("file", file);
                formData.append("upload_preset", "video-app");
                const result = await CloudinaryAPI.prototype.uploadImage(
                    formData
                );
                if (result) {
                    return result.secure_url;
                }
            }
        },
    },

    computed: {
        validateFields: function () {
            if (
                this.title &&
                this.description &&
                this.thumbnailImage &&
                this.videoData
            ) {
                return true;
            }
            return false;
        },
    },
};
</script>

<style scoped>
.add-video {
    padding: 10px 20px;
}
.headerCon {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 40px;
}

.addVideoCon {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.section {
    width: 45%;
}

.fileSection {
    padding-bottom: 30px;
}

.videoPlayerSection {
    padding: 10px 0px;
}

.videoDetailsSection {
    padding: 10px 0px;
}

.titleCon {
    font-weight: bold;
    font-size: 24px;
}

.descriptionCon,
.dateAdded {
    font-size: 14px;
    text-align: justify;
    padding: 10px 0px;
}
</style>
