import { z } from "zod";
import { zfd } from "zod-form-data";

const url = z.string().url();
const endpoint = z.string().startsWith("/");

export const apiConfigSchema = z.object({
  baseUrl: url,
  methodsEndpoint: endpoint,
  chunkRawEndpoint: endpoint
});

export const apiConfigFormSchema = zfd.formData({
  baseUrl: zfd.text(url),
  methodsEndpoint: zfd.text(endpoint),
  chunkRawEndpoint: zfd.text(endpoint)
});