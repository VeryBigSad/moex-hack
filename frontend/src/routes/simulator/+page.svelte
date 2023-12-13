<script lang="ts">
    import type { File } from "$lib";
    import type { PageServerData } from "./$types";
    import Results from "./Results.svelte";
    import Upload from "./Upload.svelte";

    export let data: PageServerData;

    let files: File[] = [data.sample];
    let file: File | undefined = files[0];
</script>

<main>
    <Upload bind:file bind:files />
    {#if file}
        <Results bind:file bind:files />
    {:else}
        <section class="empty">
            <span>Загрузите файл в поле слева</span>
            <img src="/blur.svg" alt="" />
        </section>
    {/if}
</main>

<style lang="scss">
    main {
        flex: 1;
        display: flex;
        gap: 20px;
        align-items: stretch;
        overflow-y: hidden;
    }
    .empty {
        flex: 1 0 0;
        padding: 32px 40px;
        border-radius: 12px;
        background-color: var(--block-background);
        overflow-y: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        > span {
            position: absolute;
            text-align: center;
            font-size: 20px;
            line-height: 24px;
        }
        > img {
            width: 100%;
        }
    }
</style>
