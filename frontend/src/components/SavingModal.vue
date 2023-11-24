<template>
    <div class="text-center">
        <v-dialog v-model="dialog" persistent width="300" hidden="100">
            <v-card
                color="white"
                dark
                style="padding: 10px; padding-top: 20px"
                outlined
            >
                <v-card-text>
                    <span style="color: #4514d7">Saving Video</span>
                    <v-progress-linear
                        indeterminate
                        color="#4514d7"
                        style="margin: 10px 0px"
                    ></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
export default {
    props: {
        dialog: Boolean,
    },
    data() {
        return {};
    },
};
</script>
