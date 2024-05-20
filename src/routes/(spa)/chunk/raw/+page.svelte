<script lang="ts">
	import { getToastStore } from '@skeletonlabs/skeleton';
	import { appStatus } from '$lib/stores/app-status-store';
	import { apiConfig } from '$lib/stores/api-config-store';
	import { methods } from '$lib/stores/methods-store';
	import { z } from 'zod';
	import { chunkSchema } from '$lib/schemas/chunk-schema';
	import { chunks } from '$lib/stores/chunks-store';

	const toasts = getToastStore();
	$: postUrl = $apiConfig.baseUrl + $apiConfig.chunkRawEndpoint;

	const submitToServer = async (methodId: string, text: string, chunkSize: number) => {
		appStatus.setIsLoading(true);
		try {
			const response = await fetch(postUrl, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ methodId, text, chunkSize })
			});
			const data = await response.json();
			const { chunks: retrievedChunks } = z.object({ chunks: z.array(chunkSchema) }).parse(data);
			chunks.set(retrievedChunks);

			toasts.trigger({
				message: 'Chunks retrieved from the API',
				background: 'variant-filled-success',
				timeout: 3000
			});
		} catch (error) {
			console.error('Error:', error);
			toasts.trigger({
				message: "There's been an error",
				background: 'variant-filled-error',
				timeout: 3000
			});
		}
		appStatus.setIsLoading(false);
	};

	function submit(evt: SubmitEvent) {
		evt.preventDefault();

		const data = new FormData(evt.target as HTMLFormElement);
		submitToServer(
			data.get('methodId') as string, 
			data.get('text') as string,
			Number(data.get('chunkSize'))
		);
	}
</script>

<div>
	<h2 class="h2 mb-6">Raw text chunker</h2>

	<form class="flex flex-col gap-3" on:submit={submit}>
		<label class="label">
			<span>Text</span>
			<textarea
				class="textarea"
				rows="12"
				name="text"
				placeholder="Place your text to be chunked here."
				required
			/>
		</label>

		<label class="label max-w-[320px]">
			<span>Method</span>
			<select class="select" required name="methodId">
				{#each $methods as method}
					<option value={method.id}>{method.name}</option>
				{/each}
			</select>
		</label>

		<label class="label flex flex-col">
			<span>Chunk size</span>
			<input
				type="number"
				class="input w-32"
				step="1"
				min="0"
				max="1000"
				required
				name="chunkSize"
			/>
			<span class="text-xs">Number of paragraphs, sentences, etc</span>
		</label>

		<div class="flex justify-start gap-3 mt-6">
			<button class="btn variant-filled-primary" disabled={$appStatus.isLoading}>Send</button>
		</div>
	</form>
</div>

<style>
	textarea {
		resize: none;
	}
</style>
