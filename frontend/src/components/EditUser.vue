<template>
    <div class="edit-user-con">
        <v-dialog v-model="dialog" width="400" color="white" persistent>
            <div class="editCon">
                <div class="headerSection">
                    <div class="sectionTitle">Update User</div>
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
                            id="lname"
                            v-model="user.last_name"
                            :rules="fieldRules"
                        ></v-text-field>
                    </div>
                    <div class="field">
                        <div class="fieldLabel">Username *</div>
                        <v-text-field
                            dense
                            outlined
                            id="username"
                            v-model="user.username"
                            :rules="fieldRules"
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
                        @click="$emit('confirmUpdate', user)"
                        :loading="loading"
                        large
                        >Update</v-btn
                    >

                    <v-btn
                        color="warning"
                        outlined
                        large
                        @click="$emit('closeDialog')"
                        >Cancel</v-btn
                    >
                </div>
            </div>
        </v-dialog>
    </div>
</template>

<script>
export default {
    name: "ProfileView",
    props: {
        dialog: Boolean,
        loading: Boolean,
        user_details: Object,
    },
    created() {
        this.user = JSON.parse(JSON.stringify(this.user_details));
        console.log(this.user);
    },
    components: {},
    data: () => ({
        user: {
            first_name: "",
            last_name: "",
            username: "",
            password: "",
        },
        fieldRules: [(v) => !!v || "This field is required"],
    }),
    methods: {
        handleUpdateEvent() {},
    },
    computed: {
        validated: function () {
            if (
                this.user.first_name == "" ||
                this.user.last_name == "" ||
                this.user.username.trim() == ""
            ) {
                return false;
            }

            if (
                JSON.stringify(this.user_details) == JSON.stringify(this.user)
            ) {
                return false;
            }

            return true;
        },
    },
};
</script>

<style scoped>
.editCon {
    padding: 30px;
    background-color: white;
}

.sectionTitle {
    font-size: 24px;
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

.v-btn {
    margin: 10px;
}
</style>
