<template>
	<div class="text-center">
		<v-dialog v-model="dialog" persistent width="300" hidden="100">
			<v-card color="primary" dark style="padding: 10px; padding-top: 20px">
				<v-card-text>
					<span>Saving Video</span>
					<v-progress-linear
						indeterminate
						color="white"
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
