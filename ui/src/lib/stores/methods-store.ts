import type { Method } from "$lib/types/method";
import { writable } from "svelte/store";

function createMethodsStore() {
  const actualStore = writable<Method[]>([]);

  return {
    ...actualStore
  };
}

export const methods = createMethodsStore();