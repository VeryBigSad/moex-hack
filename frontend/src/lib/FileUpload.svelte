<script lang="ts">
    import type { File } from "$lib";
    import { createEventDispatcher } from "svelte";

    let dispatch = createEventDispatcher<{ upload: File }>();
    let input: HTMLInputElement;

    async function getFile() {
        if (input.files && input.files.length >= 0)
        {
            let file = input.files[0];
            let name = file.name;
            let content = await file.text();
            dispatch("upload", { name, content });
        }
    }
</script>

<label class="upload-button">
    <input type="file" bind:this={input} on:change={getFile} />
    <div>
        <img src="/icons/file.svg" alt="" />
        <span>Выберите файлы</span>
    </div>
    <span>или перетащите их сюда</span>
</label>

<style lang="scss">
    .upload-button {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        margin-top: 20px;
        cursor: pointer;

        > input {
            display: none;
        }
        > div {
            align-self: stretch;
            display: flex;
            gap: 4px;
            display: flex;
            align-items: center;
            justify-content: center;

            background-color: var(--block-background);
            border: 1px solid var(--good-color);
            padding: 8px 12px;
            border-radius: 12px;

            > span {
                color: var(--good-color);
                font-size: 20px;
                line-height: 22px;
            }
        }
    }
</style>
