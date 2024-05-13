<script lang="ts">
	import { Github, Linkedin } from 'lucide-svelte';
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center flex flex-col items-center">
		<h1 class="text-4xl md:text-6xl font-bold gradient-text">This is Chunker UI.</h1>

		<p class="text-lg md:text-xl max-w-sm font-medium">
			Here you can test different schemes for chunking <span class="text-tertiary-500">your texts</span> and improving
			the quality of your RAG application
		</p>
		
		<!-- / -->
		<div class="flex justify-center space-x-2">
			<a
				class="btn variant-filled"
				href="/chunk"
			>
				Get started now
			</a>
		</div>
		<div class="space-y-6">
			<p>Get the source code or contact me:</p>
			
			<div class="flex justify-center gap-3 items-center">
				<a href="" target="_blank" rel="noreferrer">
					<Github class="size-12" />
				</a>
				<a href="https://www.linkedin.com/in/johnny-gomes-2672b7121/" target="_blank" rel="noreferrer">
					<Linkedin class="size-12" />
				</a>
			</div>
		</div>
	</div>
</div>

<style lang="postcss">
	.gradient-text {
		@apply bg-clip-text text-transparent box-decoration-clone;
		/* Direction */
		@apply bg-gradient-to-br;
		/* Color Stops */
		@apply from-primary-500 via-secondary-500 to-tertiary-500;
	}
</style>
