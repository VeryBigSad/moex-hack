<script lang="ts">
    import { type File, runBacktest } from "$lib";
    import Plot from "$lib/Plot.svelte";
    import { writable } from "svelte/store";
    import InfoButton from "$lib/InfoButton.svelte";
    import type { Data, PlotData } from "plotly.js-dist";
    import ProgressButton from "./ProgressButton.svelte";

    export let files: File[];
    export let file: File;

    let stats: { name: string; value: string }[][] = [];
    $: _stats = stats.length > 0 ? stats[0] : [];

    let loading = false;

    let plot_data = writable<Data[]>([]);
    let start_backtest = async () => {
        loading = true;
        stats = [];
        const colors = ["#72DEE5", "#7472E5", "#D572E5", "#E5B072", "#E3E572"];
        try
        {
            let result: Partial<PlotData>[] = [];
            let algorithms = await runBacktest(files, date_start, date_end);
            for (const [index, { data, candles }] of algorithms.entries()) {
                let x = [];
                let y = [];
                for (const { begin, close } of candles) {
                    x.push(begin);
                    y.push(close);
                }
                stats.push(
                    Object.entries(data).map(dat => ({ name: dat[0], value: dat[1].toString() }))
                );
                stats = stats;
                result.push({ x, y, line: { color: colors[index % colors.length] } });
            }
            plot_data.set(result);
        }
        catch
        {
            alert("Ошибка! Попробуйте поменять даты бектеста."); // TODO
        }
        loading = false;
    };

    let date_start: string;
    let date_end: string;
    $: start_enabled = date_start && date_end;
</script>

<section class="results">
    <h2>Backtest</h2>
    <div class="period">
        <div>
            <span>Начало теста</span>
            <input type="date" bind:value={date_start} />
        </div>
        <div>
            <span>Конец теста</span>
            <input type="date" bind:value={date_end} />
        </div>
        <ProgressButton on:click={start_backtest} disabled={!start_enabled} {loading} />
    </div>
    <hr />
    <div style="height=250px;">
        <Plot data={plot_data} />
    </div>
    <hr />
    <div class="label">
        <img src="/icons/eye_open.svg" alt="selected graph" />
        <h1>{file.name}</h1>
        <InfoButton />
    </div>
    <div class="stats">
        {#each _stats as value}
            <div>
                <span>{value.name}</span>
                <span>{value.value}</span>
            </div>
        {/each}
    </div>
</section>

<style lang="scss">
    .results {
        flex: 1 0 0;
        display: flex;
        overflow-x: hidden;
        flex-direction: column;
        padding: 32px 40px;
        border-radius: 12px;
        background-color: var(--block-background);
        justify-content: stretch;
        align-items: stretch;
        > .label {
            display: flex;
            align-items: center;
            gap: 8px;
            margin: 16px 0;
            > img {
                width: 16px;
                height: 16px;
            }
            > h1 {
                flex: 1;
                font-weight: normal;
            }
        }
        > h2 {
            margin-bottom: 8px;
        }
    }

    .period {
        display: flex;
        margin-bottom: 24px;
        gap: 20px;
        > div {
            display: flex;
            flex-direction: column;
            gap: 4px;
            > input {
                color: white;
                background-color: transparent;
                text-decoration: dashed;
            }
        }
    }

    .stats {
        display: grid;
        grid-template-columns: 1fr 1fr;
        margin-bottom: 20px;
        gap: 12px;
        overflow-x: scroll;
        > div {
            display: flex;
            flex-direction: column;
            border-radius: 12px;
            > span:nth-child(1) {
                white-space: nowrap;
            }
        }
    }
</style>
