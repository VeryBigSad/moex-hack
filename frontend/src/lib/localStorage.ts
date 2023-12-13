import { get, writable, type Writable } from 'svelte/store'

export function storable<T>(data: T): Writable<T> {
   const store = writable(data);
   const { subscribe, set } = store;
   const isBrowser = () => typeof window !== 'undefined';

   if (isBrowser() && localStorage.storable)
   {
      set(JSON.parse(localStorage.storable));
   }

   return {
      subscribe,
      set: dat => {
         isBrowser() && (localStorage.storable = JSON.stringify(dat));
         set(dat);
      },
      update: updater => {
         const dat = updater(get(store));
         isBrowser() && (localStorage.storable = JSON.stringify(dat));
         set(dat);
      }
   };
}
