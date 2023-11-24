<template>
	<div>
		<div class="headerCon">
			<div class="logoSection" id="logo" @click="$router.push('/')">
				<span>Video</span><span style="color: #3500d4">Story</span>
			</div>
		</div>
		<br />
		<br />
		<h1>Page Not Found</h1>
		<p>Click the title to login</p>
	</div>
</template>

<style scoped>
	.headerCon {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.logoSection {
		font-size: 30px;
		font-weight: bold;
		cursor: pointer;
	}
</style>
