import { error, redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async ({ fetch, params, parent }) => {
    let { articles } = await parent();

    let article = articles.find(v => v.id == params.article_id);
    if (!article) throw error(404);

    let content = fetch(`/article-sources/${params.article_id}.html`)
        .then(response => {
            if (response.status == 404) throw error(404);
            return response.text();
        });

    return { article, content };
};
