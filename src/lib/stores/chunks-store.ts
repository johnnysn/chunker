import type { Chunk } from "$lib/types/chunk";
import { writable } from "svelte/store";

function createStore() {
  const actualStore = writable<Chunk[]>([]);

  return {
    subscribe: actualStore.subscribe,
    set: actualStore.set
  }
}

export const chunks = createStore();