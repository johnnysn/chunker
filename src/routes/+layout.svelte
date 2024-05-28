<script lang="ts">
	import '../app.postcss';
	import { CircleHelp, Settings, Clapperboard } from 'lucide-svelte';

	import { initializeStores, Toast } from '@skeletonlabs/skeleton';

	initializeStores();
</script>

<svelte:head>
	<title>Chunker UI</title>
	<meta name="description" content="Application for testing text chunking schemes" />
</svelte:head>

<Toast />

<div class="flex flex-col w-full min-h-screen">
	<header class="bg-surface-900/60 h-16 w-full">
		<div
			class="w-full h-full max-w-screen-xl mx-auto flex items-center justify-between px-2 md:px-6"
		>
			<div>
				<a href="/">
					<strong class="text-lg md:text-xl tracking-tighter uppercase gradient-text">
						Chunker UI
					</strong>
				</a>
			</div>

			<nav class="flex items-center gap-3">
				<a
					class="btn btn-sm variant-ghost-surface flex items-center justify-center"
					href="/chunk"
					aria-label="Chunk"
				>
					<Clapperboard class="size-6" />
				</a>
				<a
					class="btn btn-sm variant-ghost-surface flex items-center justify-center"
					href="/settings"
					aria-label="Settings"
				>
					<Settings class="size-6" />
				</a>
				<a
					class="btn btn-sm variant-ghost-surface flex items-center justify-center"
					href="/about"
					aria-label="About"
				>
					<CircleHelp class="size-6" />
				</a>
			</nav>
		</div>
	</header>

	<main class="w-full flex-1 flex flex-col">
		<slot />
	</main>

	<footer class="py-6 mt-6">
		<p class="text-center">
			{new Date().getFullYear()} &copy; Johnny Moreira Gomes
		</p>
	</footer>
</div>

<style>
	.gradient-text {
		@apply bg-clip-text text-transparent box-decoration-clone;
		/* Direction */
		@apply bg-gradient-to-br;
		/* Color Stops */
		@apply from-primary-500 via-tertiary-500 to-secondary-500;
	}
</style>
