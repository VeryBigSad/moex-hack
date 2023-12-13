<script lang="ts">
    import { Timelines, type File } from "$lib";
    import OptionList from "$lib/OptionList.svelte";
    import Plot from "$lib/Plot.svelte";
    import { writable } from "svelte/store";
    import InfoButton from "$lib/InfoButton.svelte";
    import ProgressBar from "$lib/ProgressBar.svelte";
    import { json } from "@sveltejs/kit";

    let timeline = Timelines[1];

    const stats = [
        { name: "Starting Balance", value: "1000$" },
        { name: "Final Balance", value: "15051$" },
        { name: "Total Profit", value: "14051$" },
        { name: "Avg Daily Product", value: "141$" },
        { name: "Avg Stake Amount", value: "23$" },
        { name: "Best Trade", value: "100$" },
        { name: "Worst Trade", value: "-21$" }
    ];

    export let files: File[];
    export let file: File;

    let start_backtest = async () => {
        let _files = files.map(file => {
            let id = Math.floor(Math.random() * 999999999);
            return { id, ...file };
        });
        let data = fetch("https://khromdev.ru/api/v1/backtest/backtest", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                files: _files,
                date_start,
                date_end
            })
        });
        data.then(a => a.text()).then(a => console.log(a));
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
        <button on:click={start_backtest} disabled={!start_enabled}>
            Запустить
            <img src="/icons/arrow_back.svg" alt="" />
        </button>
    </div>
    <OptionList options={Timelines} bind:selected={timeline} />
    <hr />
    <Plot data={writable([])} />
    <hr />
    <div class="label">
        <img src="/icons/eye_open.svg" alt="selected graph" />
        <h1>{file.name}</h1>
        <InfoButton />
    </div>
    <div class="stats">
        {#each stats as value}
            <div>
                <span>{value.name}</span>
                <span>{value.value}</span>
            </div>
        {/each}
    </div>
    <div class="algos">
        {#each files as algo}
            <div>
                {#if file == algo}
                    <img src="/icons/eye_open.svg" alt="" />
                {:else}
                    <img src="/icons/eye_closed.svg" alt="" />
                {/if}
                <span>{algo.name}</span>
                <ProgressBar percent={50} />
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
        }
        > button {
            margin-left: auto;
            background-color: var(--good-color);
            border-radius: 12px;
            padding: 8px 16px;
        }
    }

    .stats {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
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

    .algos {
        display: flex;
        flex-direction: column;
        gap: 20px;
        overflow-y: scroll;
        > div {
            display: flex;
            align-items: center;
            gap: 4px;
            > img {
                width: 16px;
                height: 16px;
            }
            > span {
                flex: 1;
            }
        }
    }
</style>
