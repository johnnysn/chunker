<script lang="ts">
	let chunkSize = 200;
  let chunkOverlap = 10;
</script>

<div class="flex gap-6 flex-wrap">
	<label class="label flex flex-col">
		<span>Chunk size</span>
		<input
			type="number"
			class="input w-32"
			step="1"
			min="0"
			max="10000"
			required
			name="chunkSize"
			bind:value={chunkSize}
		/>
		<span class="text-xs">Number of paragraphs, sentences, etc</span>
	</label>

  <label class="label flex flex-col">
		<span>Chunk overlap</span>
		<input
			type="number"
			class="input w-32"
			step="1"
			min="0"
			max="1000"
			required
			name="chunkOverlap"
			bind:value={chunkOverlap}
		/>
		<span class="text-xs">Size of chunk overlap</span>
	</label>
</div>

<label class="label flex flex-col max-w-md">
  <span>Separator</span>
  <input type="text" name="separator" class="input" placeholder="\n\n" />
  <span class="text-xs">Usually you don't need to specify a separator</span>
</label>
