<script lang="ts">
	import { requests } from '$lib/stores/requests-store';
	import { Trash2 } from 'lucide-svelte';
	import { blur } from 'svelte/transition';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	$: request_id = $page.url.searchParams.get('request_id');
</script>

<div class="py-2 px-2">
	<h5 class="h5 mb-6">Chunk history</h5>

	<ul class="overflow-y-scroll max-h-[700px] px-1">
		{#each $requests as reqResp (reqResp.request.id)}
			<li class="py-2 text-sm">
				<div
					class={`card card-hover p-2 flex justify-between items-center ${request_id === reqResp.request.id ? 'border border-primary-500' : ''}`}
					transition:blur
				>
					<a
						type="button"
						class="cursor-pointer flex flex-col"
						href={`/app/chunk?request_id=${reqResp.request.id}`}
					>
						<h4 class="font-medium">{reqResp.request.methodId}</h4>
						<p class="text-xs">
							{reqResp.request.text.substring(0, 50)}
							{reqResp.request.text.length > 50 ? '...' : ''}
						</p>
						<span class="text-xs">{reqResp.request.chunkSize}, {reqResp.request.chunkOverlap}</span>
					</a>
					<button
						class="btn-icon"
						on:click={() => {
							requests.remove(reqResp.request.id);
							if (request_id === reqResp.request.id) goto(`/app/chunk`);
						}}
					>
						<Trash2 class="size-5" />
					</button>
				</div>
			</li>
		{/each}
	</ul>
</div>
