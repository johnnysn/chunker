import { z } from "zod";
import { zfd } from "zod-form-data";

const url = z.string().url();
const endpoint = z.string().startsWith("/");

export const configSchema = z.object({
  baseUrl: url,
  methodsEndpoint: endpoint
});

export const configFormSchema = zfd.formData({
  baseUrl: zfd.text(url),
  methodsEndpoint: zfd.text(endpoint),
});