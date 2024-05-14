import { browser } from "$app/environment";
import { configSchema } from "$lib/schemas/config.schema";
import type { Config } from "$lib/types/config";
import { writable, type Updater } from "svelte/store";

const defaultConfig = {
  baseUrl: 'http://localhost:8000',
  methodsEndpoint: '/methods'
};

export function createConfigStore() {
  const actualStore = writable<Config>(defaultConfig, (set) => {
    if (browser) {
      const configItem = localStorage.getItem("config");

      if (configItem) {
        const obj = JSON.parse(configItem);

        const configObj = configSchema.parse(obj);

        set(configObj);
      }
    }

    return () => {};
  });


  function update(updater: Updater<Config>) {
    actualStore.update(curr => {
      const newValue = updater(curr);

      localStorage.setItem("config", JSON.stringify(newValue));

      return newValue;
    });
  }

  function patch(data: Partial<Config>) {
    update(curr => {
      return {
        ...curr,
        ...data
      }
    });
  }

  return {
    subscribe: actualStore.subscribe,
    update,
    patch
  }
}

export const config = createConfigStore();