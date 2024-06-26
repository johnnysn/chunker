import { z } from "zod";

export const methodSchema = z.object({
  id: z.string(),
  name: z.string()
});