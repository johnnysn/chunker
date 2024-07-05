<script lang="ts">
	import ChunkView from './ChunkView.svelte';
	import type { Chunk } from '$lib/types/chunk';
	import { Accordion, AccordionItem } from '@skeletonlabs/skeleton';

	export let chunks: Chunk[] = [];
</script>

<Accordion>
	{#each chunks as chunk (chunk.number)}
		<AccordionItem open>
			<svelte:fragment slot="lead"><strong>#{chunk.number}</strong></svelte:fragment>
			<svelte:fragment slot="summary"><strong>{chunk.tag ?? 'Text chunk'}</strong></svelte:fragment>
			<svelte:fragment slot="content">
				<ChunkView {chunk} />
			</svelte:fragment>
		</AccordionItem>
	{/each}
</Accordion>
