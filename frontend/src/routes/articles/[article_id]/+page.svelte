<script lang="ts">
    import { beforeUpdate } from "svelte";
    import type { PageServerData } from "./$types";

    export let data: PageServerData;

    let content = data.content;
    let headers: string[] = [];

    beforeUpdate(() => {
        if (headers.length != 0) return;
        let dummy = document.createElement("div");
        dummy.innerHTML = data.content;
        let elements = Array.from(dummy.querySelectorAll("h1, h2, h3, h4, h5, h6"));
        elements.forEach((el, i) => {
            el.id = `header-${i}`;
        });
        headers.splice(0, 0, ...elements.map(el => el.textContent!));
        headers = headers;
        content = dummy.innerHTML;
    });
</script>

<article>
    {#if data.article.source.name}
    <section class="header">
        <h1>Источник</h1>
        <a href={data.article.source.href}>{data.article.source.name}</a>
    </section>
    {/if}
    <section class="main">
        <section class="table">
            <h1 class="title">Содержание</h1>
            {#each headers as header, i}
                <a href={`#header-${i}`}>{header}</a>
            {/each}
            <h1 class="title">{data.article.title}</h1>
        </section>
        <section class="content">
            {@html content}
        </section>
    </section>
</article>

<style lang="scss">
    article {
        flex: 1;
        background-color: var(--block-background);
        border-radius: 12px;
        display: flex;
        padding: 32px 40px;
        padding-left: 0;
        overflow-y: hidden;
        > section {
            display: flex;
            flex-direction: column;
            &.header {
                flex: 0 0 180px;
                border-right: 1px solid #57595e;
                margin-right: 8px;
                margin-left: 30px;
            }
        }
    }
    .main {
        flex: 1 0 0;
        overflow-y: scroll;
        margin-left: 30px;
        * {
            max-width: 800px;
        }
        :global(pre) {
            max-width: none;
            width: fit-content;
        }
        > .table {
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin-bottom: 20px;
        }
        > .content {
            display: flex;
            flex-direction: column;
            gap: 12px;
            :global(pre) {
                display: block;
                color: var(--text);
            }
            :global(h1) {
                font-size: 28px;
                line-height: 32px;
            }
            :global(h2) {
                font-size: 20px;
                line-height: 24px;
            }
            :global(b) {
                font-weight: bold;
            }
            :global(li), :global(pre) {
                margin-bottom: 10px;
            }
            :global(pre) {
                background-color: rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                padding: 8px;
            }
        }
        h1.title {
            font-size: 32px;
            line-height: 40px;
        }
    }
    h1 {
        font-size: 32px;
        line-height: 40px;
    }
</style>
