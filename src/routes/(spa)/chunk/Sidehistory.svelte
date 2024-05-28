<script lang="ts">
	import { requests, selectedRequest } from "$lib/stores/requests-store";
	import { Trash2 } from "lucide-svelte";
	import { blur } from "svelte/transition";

  $: selId = $selectedRequest ? $selectedRequest.request.id : '';
</script>
<div class="py-2 px-2">
  <h5 class="h5 mb-6">Chunk history</h5>

  <ul>
    {#each $requests as reqResp}
      <li class="py-2 text-sm">
        <div class={`card card-hover p-4 flex justify-between items-center ${selId === reqResp.request.id ? 'border border-primary-500' : ''}`} transition:blur>
          <button type="button" class="cursor-pointer" on:click={() => selectedRequest.set(reqResp)}>
            {reqResp.request.text.substring(0, 20)}... - 
            {reqResp.request.methodId} -
            {reqResp.request.chunkSize}/{reqResp.request.chunkOverlap}
          </button>
          <button class="btn-icon" on:click={() => {
            if (reqResp.request.id === selId) selectedRequest.set(null);
            requests.remove(reqResp.request.id);
          }}>
            <Trash2 class="size-5" />
          </button>
        </div>
      </li>
    {/each}
  </ul>
</div>