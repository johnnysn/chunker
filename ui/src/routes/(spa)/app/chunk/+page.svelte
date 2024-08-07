<script lang="ts">
	import { getToastStore } from '@skeletonlabs/skeleton';
	import { appStatus } from '$lib/stores/app-status-store';
	import { apiConfig } from '$lib/stores/api-config-store';
	import { methods } from '$lib/stores/methods-store';
	import { z } from 'zod';
	import { chunkSchema } from '$lib/schemas/chunk-schema';
	import ParametersFormGroup from './ParametersFormGroup.svelte';
	import { requests } from '$lib/stores/requests-store';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	const toasts = getToastStore();
	let rawText = '';
	let methodId: string | null = null;
	let parameters = {
		chunkSize: 200,
		chunkOverlap: 10,
		separator: ''
	};

	$: postUrl = $apiConfig.baseUrl + $apiConfig.chunkRawEndpoint;
	$: {
		const urlParams = $page.url.searchParams;
		const request_id = urlParams.get('request_id');

		if (request_id) {
			const selectedRequest = $requests.find((r) => r.request.id === request_id);

			if (selectedRequest) {
				rawText = selectedRequest.request.text;
				methodId = selectedRequest.request.methodId;
				parameters = {
					...selectedRequest.request
				};
			}
		}
	}

	const submitToServer = async (
		methodId: string,
		text: string,
		chunkSize: number,
		chunkOverlap: number
	) => {
		appStatus.setIsLoading(true);
		try {
			const response = await fetch(postUrl, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ methodId, text, chunkSize, chunkOverlap })
			});
			const data = await response.json();
			const { chunks: retrievedChunks } = z.object({ chunks: z.array(chunkSchema) }).parse(data);

			const request_id = requests.append(
				{
					methodId,
					text,
					chunkOverlap,
					chunkSize,
					separator: ''
				},
				retrievedChunks
			);

			toasts.trigger({
				message: 'Chunks retrieved from the API',
				background: 'variant-filled-success',
				timeout: 3000
			});

			goto(`/app/chunk?request_id=${request_id}`);
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
			Number(data.get('chunkSize')),
			Number(data.get('chunkOverlap'))
		);
	}
</script>

<div>
	<h2 class="h2 mb-6">Raw text chunker</h2>

	<form class="flex flex-col gap-3" on:submit={submit}>
		<label class="label">
			<span>Your text</span>
			<textarea
				class="textarea"
				rows="6"
				name="text"
				placeholder="Place your text to be chunked here."
				required
				value={rawText}
			/>
		</label>

		<label class="label max-w-[320px]">
			<span>Method</span>
			<select class="select" required name="methodId" value={methodId}>
				{#each $methods as method}
					<option value={method.id}>{method.name}</option>
				{/each}
			</select>
		</label>

		<ParametersFormGroup {parameters} />

		<div class="flex justify-start gap-3 mt-6">
			<button class="btn variant-filled-primary" disabled={$appStatus.isLoading}>Send</button>
		</div>
	</form>
</div>
