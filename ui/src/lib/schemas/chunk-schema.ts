import { number, z } from "zod";

export const chunkSchema = z.object({
  text: z.string().min(1),
  number: z.number().int().min(1),
  document: z.optional(z.string()),
  tag: z.optional(z.string()),
  id: z.optional(z.string()),
})