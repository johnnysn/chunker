<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
	import { Skull, CircleHelp } from 'lucide-svelte';
</script>

<svelte:head>
	<title>Chunker UI</title>
	<meta name="description" content="Application for testing text chunking schemes">
</svelte:head>

<!-- App Shell -->
<AppShell>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<strong class="text-lg md:text-xl tracking-tighter uppercase gradient-text">
					Chunker UI
				</strong>
			</svelte:fragment>
			<svelte:fragment slot="trail">
				<a
					class="btn btn-sm variant-ghost-surface flex items-center justify-center"
					href="/chunk"
					aria-label="Chunk"
				>
					<Skull class="size-6" />
				</a>
				<a
					class="btn btn-sm variant-ghost-surface flex items-center justify-center"
					href="/about"
					aria-label="About"
				>
					<CircleHelp class="size-6" />
				</a>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<!-- Page Route Content -->
	<slot />
</AppShell>

<style>
	.gradient-text {
		@apply bg-clip-text text-transparent box-decoration-clone;
		/* Direction */
		@apply bg-gradient-to-br;
		/* Color Stops */
		@apply from-primary-500 via-tertiary-500 to-secondary-500;
	}
</style>
