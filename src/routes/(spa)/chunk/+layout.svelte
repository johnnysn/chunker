<script lang="ts">
	import { page } from "$app/stores";
	import { methodSchema } from "$lib/schemas/method-schema";
	import { apiConfig } from "$lib/stores/api-config-store";
	import { methods } from "$lib/stores/methods-store";
	import { Aperture, Settings } from "lucide-svelte";
	import { z } from "zod";

  $: classesActive = (href: string) => (href === $page.url.pathname ? '!variant-filled-primary' : '');

  $: {
    const { baseUrl, methodsEndpoint } = $apiConfig;

    const fetchMethods = async () => {
      const response = await fetch(baseUrl + methodsEndpoint);

      if (response.ok) {
        const data = await response.json();

        const methodsData = z.array(methodSchema).safeParse(data);
        console.log(methodsData);

        if (methodsData.success) {
          methods.set(methodsData.data);
        }
      }
    };

    fetchMethods();
  }
</script>
<div class="flex">
  <div class="w-1/4 mr-6 bg-surface-500/5 h-[300px]">
    <nav class="list-nav mt-2">
      <ul>
        <li>
          <a href={"/chunk/config"} class="{classesActive("/chunk/config")}">
            <span><Settings class="size-6" /></span>
            <span class="flex-auto">API Config</span>
          </a>
          <a href={"/chunk/raw"} class="{classesActive("/chunk/raw")}">
            <span><Aperture class="size-6" /></span>
            <span class="flex-auto">Raw text</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>

  <div class="w-3/4">
    <slot />
  </div>
</div>