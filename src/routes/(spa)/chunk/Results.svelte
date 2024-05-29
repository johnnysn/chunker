<script lang="ts">
	import ChunksAccordion from "$lib/components/ChunksAccordion.svelte";
	import { chunks } from "$lib/stores/chunks-store";

</script>
<div>
	{#if $chunks.length > 0}
		<div class="card-header"><h3 class="h3 mb-4">Retrieved Chunks</h3></div>
		<div class="card-content"><ChunksAccordion chunks={$chunks} /></div>
	{/if}
</div>