<form class="flex flex-col gap-3">
  <h2 class="h2 mb-6">API Config</h2>

  <label class="label max-w-md">
    <span>Base URL</span>
    <input type="text" class="input" placeholder="API base URL" />
  </label>

  <label class="label max-w-md">
    <span>List methods</span>
    <input type="text" class="input" placeholder="Endpoint for listing chunking methods" />
    <p class="text-sm">Example: <span class="code">/methods</span></p>
  </label>

  <label class="label max-w-md">
    <span>Raw text chunk</span>
    <input type="text" class="input" placeholder="Endpoint for chunking raw text" />
  </label>

  <div class="mt-6 flex flex-start gap-3">
    <button class="btn variant-filled-primary">Save</button>
  </div>

</form>