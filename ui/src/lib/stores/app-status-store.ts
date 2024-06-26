import { type AppStatus } from "$lib/types/app-status";
import { writable } from "svelte/store";

const appStatusDefault = {
  isLoading: false,
  isFetchingParameters: false,
  isParametersFetched: false
}

function createAppStatusStore() {
  const actualStore = writable<AppStatus>(appStatusDefault);

  function setIsLoading(isLoading: boolean) {
    actualStore.update(curr => ({
      ...curr,
      isLoading
    }));
  }

  function setIsFetchingParameters(isFetchingParameters: boolean) {
    actualStore.update(curr => ({
      ...curr,
      isFetchingParameters
    }));
  }

  function setIsParametersFetched(isParametersFetched: boolean) {
    actualStore.update(curr => ({
      ...curr,
      isParametersFetched
    }));
  }

  return {
    subscribe: actualStore.subscribe,
    setIsLoading,
    setIsFetchingParameters,
    setIsParametersFetched
  }
}

export const appStatus = createAppStatusStore();