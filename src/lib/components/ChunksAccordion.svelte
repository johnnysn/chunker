<script lang="ts">
	import type { Chunk } from '$lib/types/chunk';
	import { Accordion, AccordionItem } from '@skeletonlabs/skeleton';

	export let chunks: Chunk[] = [];
</script>

<Accordion>
	{#each chunks as chunk}
		<AccordionItem>
			<svelte:fragment slot="lead"><strong>#{chunk.number}</strong></svelte:fragment>
			<svelte:fragment slot="summary"><strong>{ chunk.tag ?? 'Text chunk' }</strong></svelte:fragment>
			<svelte:fragment slot="content">{chunk.text}</svelte:fragment>
		</AccordionItem>
	{/each}
</Accordion>
