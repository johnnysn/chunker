<script lang="ts">
	import { page } from '$app/stores';
	import ChunksAccordion from '$lib/components/ChunksAccordion.svelte';
	import { requests } from '$lib/stores/requests-store';
	import type { Chunk } from '$lib/types/chunk';

	let chunks: Chunk[] = [];

	$: {
		const request_id = $page.url.searchParams.get('request_id');

		if (request_id) {
			const selectedRequest = $requests.find((r) => r.request.id === request_id);

			if (selectedRequest) {
				chunks = selectedRequest.response;
			}
		}
	}
</script>

<div>
	{#if chunks.length > 0}
		<div class="card-header"><h3 class="h3 mb-4">Retrieved Chunks</h3></div>
		<div class="card-content"><ChunksAccordion {chunks} /></div>
	{/if}
</div>
