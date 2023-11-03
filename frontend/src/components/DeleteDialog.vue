<template>
	<v-row justify="center">
		<v-dialog v-model="dialog" max-width="290" persistent>
			<v-card>
				<v-card-title class="text-h5"> Delete </v-card-title>

				<v-card-text
					>Do you want to delete this video? This action cannot be undone
				</v-card-text>

				<v-card-actions>
					<v-spacer></v-spacer>

					<v-btn color="black" text @click="$emit('closeDialog')">
						Cancel
					</v-btn>

					<v-btn color="error" text @click="dialog = false"> Delete </v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</v-row>
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
