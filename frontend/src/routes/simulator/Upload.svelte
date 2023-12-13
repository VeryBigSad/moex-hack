<script lang="ts">
    import CodeMirror from "svelte-codemirror-editor";
    import { python } from "@codemirror/lang-python";
    import { oneDark } from "@codemirror/theme-one-dark";
    import type { File } from "$lib";
    import Tabs from "./Tabs.svelte";
    import FileUpload from "$lib/FileUpload.svelte";

    export let files: File[];
    export let file: File | undefined;

    let addFile = (file: File) => {
        files.push(file);
        files = files;
    };
</script>

<section class="upload">
    <div class="tabs">
        <Tabs bind:files bind:selected={file} />
    </div>
    <div class="editor">
        {#if file}
            <CodeMirror
                bind:value={file.content}
                lang={python()}
                theme={oneDark}
                styles={{
                    "&": { backgroundColor: "var(--block-background)" }
                }}
            />
        {:else}
            <CodeMirror
                value={'print("Загрузите файл со стратегией, чтобы начать")'}
                readonly
                lang={python()}
                theme={oneDark}
                styles={{
                    "&": { backgroundColor: "var(--block-background)" }
                }}
            />
        {/if}
    </div>
    <FileUpload on:upload={e => addFile(e.detail)} />
</section>

<style lang="scss">
    section {
        flex: 1 0 0;
        display: flex;
        overflow-x: hidden;
        flex-direction: column;
        padding: 32px 40px;
        border-radius: 12px;
        background-color: var(--block-background);
        &.upload {
            display: flex;
            flex-direction: column;
            > .tabs {
                max-width: min-content;
                overflow-x: scroll;
            }
            > .editor {
                flex: 1 0 0;
                overflow-y: scroll;
                border: 1px solid #56595e;
            }
        }
    }
</style>
