<script lang="ts">
	import { settings } from "$lib/stores/settings-store";

  let sanitize = $settings.sanitize;

  function submit(evt: SubmitEvent) {
    evt.preventDefault();

    settings.patch({
      sanitize
    });
  }
</script>

<form class="flex flex-col gap-3" on:submit={submit}>
  <h2 class="h2 mb-6">Settings</h2>

  <label class="flex items-center space-x-2">
		<input class="checkbox" type="checkbox" name="sanitize" bind:checked={sanitize} />
		<p>Sanitize texts</p>
	</label>

  <div class="mt-6 flex flex-start gap-3">
    <button class="btn variant-filled-primary">
      Save
    </button>
  </div>
</form>