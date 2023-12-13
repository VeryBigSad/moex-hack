import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async ({ fetch }) => {
    let name = "Sample.py";
    let content = await fetch(`/${name}`).then(r => r.text());
    return { sample: { name, content } };
};
