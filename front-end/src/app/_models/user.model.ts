import { Role } from "./role.model";

export class User {
    id: number;
    username: string;
    firstName: string;
    lastName: string;
    email: string;
    roles: Role[];
}