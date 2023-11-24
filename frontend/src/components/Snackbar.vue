<template>
	<div class="text-center">
		<v-snackbar v-model="snackbar" :timeout="timeout">
			{{ message }}

			<template v-slot:action="{ attrs }">
				<v-btn color="blue" text v-bind="attrs" @click="$emit('closeSnackbar')">
					Close
				</v-btn>
			</template>
		</v-snackbar>
	</div>
</template>

<script>
	export default {
		props: {
			snackbar: Boolean,
			message: String,
		},
		data: () => ({
			timeout: 2000,
		}),
	};
</script>
