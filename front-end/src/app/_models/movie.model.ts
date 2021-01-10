import { Genre } from "./genre.model";
import { Rating } from "./rating.model";

export class Movie {
    id : number;
    name: string;
    description: string;
    year: number;
    duration: number;
    ratings: Rating[];
    genres: Genre[];
}