<script lang="ts">
	import { page } from '$app/stores';
	import { methodSchema } from '$lib/schemas/method-schema';
	import { apiConfig } from '$lib/stores/api-config-store';
	import { appStatus } from '$lib/stores/app-status-store';
	import { methods } from '$lib/stores/methods-store';
	import {
		Aperture,
		CheckCircle,
		Info,
		Loader2,
		RefreshCcw,
		Settings,
		TriangleAlert
	} from 'lucide-svelte';
	import { z } from 'zod';
	import { getToastStore } from '@skeletonlabs/skeleton';
	import ChunksAccordion from '$lib/components/ChunksAccordion.svelte';
	import { chunks } from '$lib/stores/chunks-store';

	const toastStore = getToastStore();

	let statusMessage = '';
	let statusType: '' | 'info' | 'loading' | 'warning' | 'success' = '';

	$: classesActive = (href: string) =>
		href === $page.url.pathname ? '!variant-filled-primary' : '';

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

		<button class="btn-icon btn-icon-sm variant-ghost ml-3" on:click={() => fetchMethods($apiConfig.baseUrl, $apiConfig.methodsEndpoint)}>
			<RefreshCcw class="size-4" />
		</button>
	</div>
</div>
<div class="flex">
	<div class="w-1/4 mr-6 bg-surface-500/5">
		<nav class="list-nav mt-2">
			<ul>
				<li>
					<a href={'/chunk/config'} class={classesActive('/chunk/config')}>
						<span><Settings class="size-6" /></span>
						<span class="flex-auto">API Config</span>
					</a>
					<a href={'/chunk/raw'} class={classesActive('/chunk/raw')}>
						<span><Aperture class="size-6" /></span>
						<span class="flex-auto">Raw text</span>
					</a>
				</li>
			</ul>
		</nav>
	</div>

	<div class="w-3/4 py-2">
		<slot />
	</div>
</div>
<div class="card mt-4">
	<div class="card-header"><h3 class="h3 mb-4">Retrieved Chunks</h3></div>
	<div class="card-content"><ChunksAccordion chunks={$chunks} /></div>
</div>
