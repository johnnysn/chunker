<script lang="ts">
	import type { Chunk } from '$lib/types/chunk';

	export let chunk: Chunk;
</script>

<div class="max-h-36 overflow-y-scroll">
	{chunk.text}
</div>
