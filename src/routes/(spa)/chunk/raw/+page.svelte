<script lang="ts">
	import { getToastStore } from '@skeletonlabs/skeleton';
	import { appStatus } from '$lib/stores/app-status-store';
	import { apiConfig } from '$lib/stores/api-config-store';
	import { methods } from '$lib/stores/methods-store';

	const toasts = getToastStore();
  $: postUrl = $apiConfig.baseUrl + $apiConfig.chunkRawEndpoint;

	const submitToServer = async (methodId: string, text: string) => {
		appStatus.setIsLoading(true);
		try {
			const response = await fetch(postUrl, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ methodId, text })
			});
			const data = await response.json();
			console.log(data);

			toasts.trigger({
				message: "Chunks retrieved from the API",
				background: "variant-filled-success",
				timeout: 3000
			})
		} catch (error) {
			console.error('Error:', error);
			toasts.trigger({
				message: "There's been an error",
				background: "variant-filled-error",
				timeout: 3000
			})
		}
		appStatus.setIsLoading(false);
	};

	function submit(evt: SubmitEvent) {
		evt.preventDefault();

		const data = new FormData(evt.target as HTMLFormElement);
		submitToServer(data.get('methodId') as string, data.get('text') as string);
	}
</script>

<div>
	<h2 class="h2 mb-6">Raw text chunker</h2>

	<form class="flex flex-col gap-3" on:submit={submit}>
		<label class="label">
			<span>Text</span>
			<textarea class="textarea" rows="12" name="text" placeholder="Place your text to be chunked here." required />
		</label>

		<div class="flex gap-3">
			<label class="label">
				<span>Method</span>
				<select class="select" required name="methodId">
					{#each $methods as method}
						<option value={method.id}>{method.name}</option>
					{/each}
				</select>
			</label>
		</div>

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
