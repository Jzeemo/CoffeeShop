export class Drink {
    id: number;
    title: string;
    recipe: Array<{
        name: string,
        color: string,
        parts: number
    }>;
}