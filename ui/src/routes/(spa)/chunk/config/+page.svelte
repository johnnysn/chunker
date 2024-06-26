<script lang="ts">
	import { apiConfigFormSchema } from "$lib/schemas/api-config-schema";
	import { apiConfig } from "$lib/stores/api-config-store";

	let baseUrl = $apiConfig.baseUrl;
	let methodsEndpoint = $apiConfig.methodsEndpoint;
	let chunkRawEndpoint = $apiConfig.chunkRawEndpoint;

  function submit(evt: SubmitEvent) {
    evt.preventDefault();

    const data = new FormData(evt.target as HTMLFormElement);

    const {baseUrl, methodsEndpoint, chunkRawEndpoint} = apiConfigFormSchema.parse(data);

    apiConfig.patch({
      baseUrl, methodsEndpoint, chunkRawEndpoint
    });
  }
</script>

<form class="flex flex-col gap-3" on:submit={submit}>
	<h2 class="h2 mb-6">API config</h2>

	<label class="label max-w-md">
		<span>Base URL</span>
		<input type="text" class="input" name="baseUrl" placeholder="API base URL" bind:value={baseUrl} required />
	</label>

	<label class="label max-w-md">
		<span>List methods</span>
		<input
			type="text"
			class="input"
			placeholder="Endpoint for listing chunking methods"
      name="methodsEndpoint"
			bind:value={methodsEndpoint}
			required
		/>
		<p class="text-sm">
			Example: <span class="code">/methods</span>
		</p>
	</label>

	<label class="label max-w-md">
		<span>Chunk raw text</span>
		<input
			type="text"
			class="input"
			placeholder="Endpoint for chunking raw text"
      name="chunkRawEndpoint"
			bind:value={chunkRawEndpoint}
			required
		/>
		<p class="text-sm">
			Example: <span class="code">/chunks/raw</span>
		</p>
	</label>

	<div class="mt-6 flex flex-start gap-3">
		<button class="btn variant-filled-primary">Save</button>
	</div>
</form>
