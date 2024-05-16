<script>
	import { methods } from "$lib/stores/methods-store";

</script>
<div>
  <h2 class="h2 mb-6">Raw text chunker</h2>

  <form class="flex flex-col gap-3">
    <label class="label">
      <span>Text</span>
      <textarea class="textarea" rows="12" placeholder="Place your text to be chunked here." />
    </label>

    <div class="flex gap-3">
      <label class="label">
        <span>Method</span>
        <select class="select">
          {#each $methods as method }
            <option value={method.id}>{method.name}</option>
          {/each}
        </select>
      </label>
    </div>

    <div class="flex justify-start gap-3 mt-6">
      <button class="btn variant-filled-primary">Send</button>
    </div>
  </form>
</div>

<style>
  textarea {
    resize: none;
  }
</style>
