<div class="mx-auto w-full max-w-screen-xl px-2 md:px-6 mt-6">
  <h2 class="h2 mb-6">Text chunker</h2>

  <form class="flex flex-col gap-3">
    <label class="label">
      <span>Text</span>
      <textarea class="textarea" rows="12" placeholder="Place your text to be chunked here." />
    </label>

    <div class="flex gap-3">
      <label class="label">
        <span>Method</span>
        <select class="select">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
      </label>
    </div>

    <div class="flex justify-start gap-3 mt-6">
      <button class="btn variant-filled-primary">Send</button>
    </div>
  </form>
</div>

<style>
  textarea {
    resize: none;
  }
</style>
