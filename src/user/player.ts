import { User, UserOptions } from './user';

export interface PlayerOptions {
    achievements: string[];
    runLevel: number;
    runUpgrades: string[];
    lobbyUUID: number;
}

export class Player extends User {
    readonly achievements: string[]; //placeholder
    readonly runLevel: number = 1;
    readonly runUpgrades: string[]; //placeholder
    readonly lobbyUUID: number;

    constructor(user: UserOptions, options: PlayerOptions) {
    
        super(user);
        this.achievements = options.achievements;
        this.runLevel = options.runLevel;
        this.runUpgrades = options.runUpgrades;
        this.lobbyUUID = options.lobbyUUID;

    }
}
