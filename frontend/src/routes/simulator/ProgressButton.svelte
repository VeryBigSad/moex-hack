<script lang="ts">
    import Loader from "$lib/Loader.svelte";

    export let disabled: boolean = false;
    export let loading: boolean = false;
</script>

<!-- {percent}% -->

<button on:click {disabled}>
    {#if !loading}
        Запустить
        <img src={`/icons/arrow_back${disabled ? "_light" : ""}.svg`} alt="" />
    {:else}
        Загрузка...
    {/if}
</button>

<style lang="scss">
    button {
        width: 150px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
        background-color: var(--good-color);
        border-radius: 12px;
        padding: 8px 16px;

        margin-left: auto;
        &:disabled {
            color: #a6a3a3;
            background-color: #3d3f42;
        }
        img {
            width: 16px;
            height: 16px;
        }
    }
</style>
