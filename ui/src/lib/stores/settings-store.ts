import { browser } from '$app/environment';
import { settingsSchema } from '$lib/schemas/settings-schema';
import { type Settings } from '$lib/types/settings';
import { type Updater, writable } from 'svelte/store';

const defaultSettings = {
	sanitize: true
};

function createSettingsStore() {
	const actualStore = writable(defaultSettings, (set) => {
		if (browser) {
			const objStr = localStorage.getItem('settings');

			if (objStr) {
				const obj = settingsSchema.parse(JSON.parse(objStr));

				set(obj);
			}
		}

		return () => {};
	});

	function update(updater: Updater<Settings>) {
		actualStore.update((curr) => {
			const newValue = updater(curr);

			localStorage.setItem('settings', JSON.stringify(newValue));

			return newValue;
		});
	}

	function patch(data: Partial<Settings>) {
		update((curr) => ({
			...curr,
			...data
		}));
	}

	return {
		subscribe: actualStore.subscribe,
		update,
    patch
	};
}


export const settings = createSettingsStore();