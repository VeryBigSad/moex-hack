<div/>

<style>
    div {
        display: inline-block;
        width: calc(var(--size, 64p) * 1.2);
        height: calc(var(--size, 64px) * 1.2);
    }
    div:after {
        content: " ";
        display: block;
        width: var(--size, 64px);
        height: var(--size, 64px);
        margin: 8px;
        border-radius: 50%;
        border: 6px solid #fff;
        border-color: #fff transparent #fff transparent;
        animation: lds-dual-ring 1.2s linear infinite;
    }
    @keyframes lds-dual-ring {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>
