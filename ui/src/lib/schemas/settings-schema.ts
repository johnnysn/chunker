import { z } from "zod";

export const settingsSchema = z.object({
  sanitize: z.boolean()
});