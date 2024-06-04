<script lang="ts">
	export let parameters = {
		chunkSize: 200,
		chunkOverlap: 10,
		separator: ""
	}
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
			value={parameters.chunkSize}
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
			value={parameters.chunkOverlap}
		/>
		<span class="text-xs">Size of chunk overlap</span>
	</label>
</div>

<label class="label flex flex-col max-w-md">
  <span>Separator</span>
  <input type="text" name="separator" class="input" placeholder="\n\n" value={parameters.separator} />
  <span class="text-xs">Usually you don't need to specify a separator</span>
</label>
