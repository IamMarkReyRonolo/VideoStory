<template>
	<div class="main">
		<div
			class="dropzone-container"
			@dragover="dragover"
			@dragleave="dragleave"
			@drop="drop"
		>
			<input
				type="file"
				multiple
				name="file"
				id="fileInput"
				class="hidden-input"
				@change="onChange"
				ref="file"
				accept=".mp4,.jpg,.jpeg,.png"
			/>

			<label for="fileInput" class="file-label">
				<div v-if="files.length == 0">
					<div v-if="isDragging">Release to drop file here.</div>
					<div v-else>Drop file here or <u>click here</u> to upload.</div>
				</div>
			</label>
			<div class="preview-container mt-4" v-if="files.length">
				<div v-for="file in files" :key="file.name" class="preview-card">
					<div>
						<img
							class="preview-img"
							:src="generateURL(file)"
							@click="remove(files.indexOf(file))"
						/>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				isDragging: false,
				files: [],
			};
		},
		methods: {
			onChange() {
				this.files.push(...this.$refs.file.files);
			},
			dragover(e) {
				e.preventDefault();
				this.isDragging = true;
			},
			dragleave() {
				this.isDragging = false;
			},
			drop(e) {
				e.preventDefault();
				this.$refs.file.files = e.dataTransfer.files;
				this.onChange();
				this.isDragging = false;
			},
			remove(i) {
				this.files.splice(i, 1);
			},
			generateURL(file) {
				let fileSrc = URL.createObjectURL(file);
				setTimeout(() => {
					URL.revokeObjectURL(fileSrc);
				}, 1000);
				return fileSrc;
			},
		},
	};
</script>
<style scoped>
	.dropzone-container {
		padding: 2rem;
		background: #f7fafc;
		border: 1px solid #e2e8f0;
		width: 200px;
		height: 150px;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.hidden-input {
		opacity: 0;
		overflow: hidden;
		position: absolute;
		width: 1px;
		height: 1px;
	}

	.file-label {
		font-size: 12px;
		display: block;
		cursor: pointer;
		text-align: center;
	}

	/* .preview-container {
		display: flex;
		margin-top: 2rem;
	} */

	/* .preview-card {
		display: flex;
		padding: 5px;
		margin-left: 5px;
	} */

	.preview-img {
		width: 200px;
		height: 150px;
		/* border-radius: 5px;
		border: 1px solid #a2a2a2;
		background-color: #a2a2a2; */
	}
</style>
