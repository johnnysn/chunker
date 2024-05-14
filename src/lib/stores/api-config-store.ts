import { browser } from "$app/environment";
import { apiConfigFormSchema } from "$lib/schemas/api-config-schema";
import { type ApiConfig } from "$lib/types/api-config";
import { writable, type Updater } from "svelte/store";

const defaultConfig = {
  baseUrl: 'http://localhost:8000',
  methodsEndpoint: '/methods'
};

export function createConfigStore() {
  const actualStore = writable<ApiConfig>(defaultConfig, (set) => {
    if (browser) {
      const configItem = localStorage.getItem("api-config");

      if (configItem) {
        const obj = JSON.parse(configItem);

        const configObj = apiConfigFormSchema.parse(obj);

        set(configObj);
      }
    }

    return () => {};
  });


  function update(updater: Updater<ApiConfig>) {
    actualStore.update(curr => {
      const newValue = updater(curr);

      localStorage.setItem("api-config", JSON.stringify(newValue));

      return newValue;
    });
  }

  function patch(data: Partial<ApiConfig>) {
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

export const apiConfig = createConfigStore();