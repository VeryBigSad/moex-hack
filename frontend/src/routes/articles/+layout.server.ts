import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async () => {
    return { articles: ARTICLES };
};

export type ArticleInfo = { id: string; title: string; description: string; source: { name: string, href: string } };

const ARTICLES = [
    {
        id: "guide",
        title: "Входим в алготрейдинг",
        description: "Наш гайд о том, как сделать первые шаги в алготрейдинге!",
        source: { name: "", href: "https://khromdev.ru/" },
    },
    {
        id: "python-algotrading",
        title: "Python для алготрейдинга",
        description:
            "В этом посте я собрал все известные мне полезные штуки, которые могут пригодится в алготрейдинге. Чем-то я пользуюсь сам, что-то пробовал и не мне понравилось, а чем-то не пользовался вовсе, но это не значит что это не может быть вам полезным. Не все относиться к алготрейдингу напрямую, но может быть полезным в какой-то степени.",
        source: { name: "day0markets.ru", href: "https://day0markets.ru/python-algotrading/" },
    },
    {
        id: "trade-bots",
        title: "Торговые роботы на Python",
        description:
            "Привет! На связи команда Тинькофф Инвестиций. В этой статье рассказываем про Tinkoff Invest API, объясняем, как написать робота на Python, и разбираем плюсы этого языка в сравнении с другими. А вместо заключения ловите гайд по созданию робота на примере работы победителя нашего конкурса Tinkoff Invest Robot Contest.",
        source: { name: "habr.ru", href: "https://habr.com/ru/companies/tinkoff/articles/709166/" },
    },
    {
        id: "100-lines",
        title: "100 строк Python-кода: Автоматизируем биржевую торговлю",
        description: "Алгоритмическая торговля еще никогда не была такой доступной, как в настоящее время. Совсем недавно этот вид деятельности был по плечу лишь институциональным инвесторам с миллионными бюджетами, однако сегодня фактически любой желающий при наличии ноутбука и подключения к Интернет может заняться алгоритмической торговлей.",
        source: { name: "datareview.info", href: "https://datareview.info/article/100-strok-python-koda-avtomatiziruem-birzhevuyu-torgovlyu/" },
    },
    {
        id: "transformer",
        title: "О практической пользе transformer для торговли на бирже",
        description:
            "В этой статье рассмотрим, как Transformer может улучшить торговлю на бирже. Разберем, как эта технология улучшает анализ данных и помогает принимать более точные решения, оптимизируя стратегии трейдинга.",
        source: { name: "habr.com", href: "https://habr.com/ru/articles/651607/" },
    }
] satisfies ArticleInfo[];
