import type { Chunk } from "$lib/types/chunk";
import type { ChunkRequest } from "$lib/types/chunk-request";
import { writable, type Updater } from "svelte/store";
import { createId } from '@paralleldrive/cuid2';

interface RequestResponse {
  request: ChunkRequest,
  response: Chunk[]
}

function createRequestsStore() {
  const actualStore = writable<RequestResponse[]>([]);

  function update(updater: Updater<RequestResponse[]>) {
    actualStore.update(curr => {
      const newValue = updater(curr);

      return newValue;
    })
  }

  function append(request: Omit<ChunkRequest, "id">, chunks: Chunk[]) {
    const value = {
      request: {
        ...request,
        id: createId()
      },
      response: chunks
    }
    update(curr => [...curr, value])
  }

  function remove(id: string) {
    update(curr => curr.filter(c => c.request.id !== id));
  }

  return {
    subscribe: actualStore.subscribe,
    append,
    remove
  }
}

export const requests = createRequestsStore();

export const selectedRequest = writable<RequestResponse | null>(null);