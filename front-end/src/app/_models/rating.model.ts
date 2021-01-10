import { Movie } from "./movie.model";
import { User } from "./user.model";

export class Rating {
    id: number;
    rating: number;
    comment: string;
    user: User;
    movieId?: number;
}