<script lang="ts">
	import { page } from '$app/stores';
	import { BadgeHelp, Cpu, Scissors, Settings } from 'lucide-svelte';

	$: classesActive = (href: string) =>
		href === $page.url.pathname ? '!variant-filled-primary' : '';
</script>

<nav class="list-nav mt-2">
	<ul>
		<li>
			<a href={'/app/chunk'} class={classesActive('/app/chunk')}>
				<span><Scissors class="size-6" /></span>
				<span class="flex-auto">Chunk text</span>
			</a>
			<a href={'/app/methods'} class={classesActive('/app/methods')}>
				<span><Cpu class="size-6" /></span>
				<span class="flex-auto">Methods</span>
			</a>
			<a href={'/app/config'} class={classesActive('/app/config')}>
				<span><Settings class="size-6" /></span>
				<span class="flex-auto">API Config</span>
			</a>
			<a href={'/app/help'} class={classesActive('/app/help')}>
				<span><BadgeHelp class="size-6" /></span>
				<span class="flex-auto">Help</span>
			</a>
		</li>
	</ul>
</nav>
