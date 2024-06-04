<script lang="ts">
	import { methodSchema } from '$lib/schemas/method-schema';
	import { apiConfig } from '$lib/stores/api-config-store';
	import { appStatus } from '$lib/stores/app-status-store';
	import { methods } from '$lib/stores/methods-store';
	import { CheckCircle, Info, Loader2, RefreshCcw, TriangleAlert } from 'lucide-svelte';
	import { z } from 'zod';
	import { getToastStore } from '@skeletonlabs/skeleton';
	import Sidenav from './Sidenav.svelte';
	import Sidehistory from './Sidehistory.svelte';
	import Results from './Results.svelte';
	import { chunks } from '$lib/stores/chunks-store';
	import { selectedRequest } from '$lib/stores/requests-store';

	const toastStore = getToastStore();

	let statusMessage = '';
	let statusType: '' | 'info' | 'loading' | 'warning' | 'success' = '';

	const fetchMethods = async (baseUrl: string, methodsEndpoint: string) => {
		appStatus.setIsFetchingParameters(true);
		appStatus.setIsParametersFetched(false);
		let ok = false;
		try {
			const response = await fetch(baseUrl + methodsEndpoint);
			appStatus.setIsFetchingParameters(false);

			if (response.ok) {
				const data = await response.json();

				const methodsData = z.array(methodSchema).safeParse(data);

				if (methodsData.success) {
					methods.set(methodsData.data);
					appStatus.setIsParametersFetched(true);
					ok = true;
				}
			}
		} catch (err) {
			appStatus.setIsFetchingParameters(false);
		}

		if (!ok) {
			toastStore.trigger({
				message: 'Could not retrieve parameters from the API',
				background: 'variant-filled-error',
				timeout: 3000
			});
		}
	};

	$: {
		const { baseUrl, methodsEndpoint } = $apiConfig;
		fetchMethods(baseUrl, methodsEndpoint);
	}

	$: {
		if ( $selectedRequest ) {
			chunks.set($selectedRequest.response);
		}
	}

	$: {
		if ($appStatus.isFetchingParameters) {
			statusMessage = 'Fetching parameters from API...';
			statusType = 'loading';
		} else if ($appStatus.isLoading) {
			statusMessage = 'Loading...';
			statusType = 'loading';
		} else if ($appStatus.isParametersFetched) {
			statusMessage = 'Parameters fetched from API';
			statusType = 'success';
		} else {
			statusMessage = 'Please, setup API';
			statusType = 'warning';
		}
	}
</script>

<div class="bg-surface-500/5 h-12 flex items-center justify-end px-2 md:px-6">
	<div class="flex items-center gap-2">
		{#if statusType === 'success'}
			<CheckCircle class="size-4 text-success-500" />
		{:else if statusType === 'info'}
			<Info class="size-4 text-primary-500" />
		{:else if statusType === 'loading'}
			<Loader2 class="size-4 animate-spin" />
		{:else if statusType === 'warning'}
			<TriangleAlert class="size-4 text-warning-500" />
		{/if}

		<span>{statusMessage}</span>

		<button
			class="btn-icon btn-icon-sm variant-ghost ml-3"
			on:click={() => fetchMethods($apiConfig.baseUrl, $apiConfig.methodsEndpoint)}
		>
			<RefreshCcw class="size-4" />
		</button>
	</div>
</div>
<div class="flex">
	<div class="w-1/5 mr-6 bg-surface-500/5">
		<Sidenav />
	</div>

	<div class="w-3/5 py-2">
		<slot />
	</div>

	<div class="w-1/5 bg-surface-500/5 ml-6 py-2">
		<Sidehistory />
	</div>
</div>

<section class="card mt-4" id="retrieved-chunks">
	{#if $appStatus.isLoading}
		<div class="p-4 space-y-4 w-full">
			<div class="placeholder animate-pulse"></div>
			<div class="placeholder animate-pulse"></div>
			<div class="placeholder animate-pulse"></div>
		</div>
	{:else}
		<Results />
	{/if}
</section>