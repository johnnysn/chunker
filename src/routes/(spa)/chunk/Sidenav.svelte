<script lang="ts">
	import { page } from "$app/stores";
	import { Aperture, Settings } from "lucide-svelte";

  $: classesActive = (href: string) =>
		href === $page.url.pathname ? '!variant-filled-primary' : '';
</script>

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
