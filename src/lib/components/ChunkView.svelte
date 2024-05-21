<script lang="ts">
	import type { Chunk } from "$lib/types/chunk";

  export let chunk: Chunk;
</script>

<div>
  <textarea name="chunk_content" id="chunk_content" class="textarea" readonly rows={7}>{chunk.text}</textarea>
</div>