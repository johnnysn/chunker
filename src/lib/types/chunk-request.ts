import type { Chunk } from "./chunk";

export interface ChunkRequest {
  id: string,
  text: string,
  methodId: string,
  chunkSize: number,
  chunkOverlap: number,
  separator?: string
}