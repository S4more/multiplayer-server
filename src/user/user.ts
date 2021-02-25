import { Socket } from 'socket.io';

export interface UserOptions {
    uuid: number,
    name: string,
    upgrades: string,
    friendList: number[],
    level: number,
    webSocket: Socket;
}

export class User {
    readonly uuid: number;
    readonly name: string;
    readonly upgrades: string; // placeholder
    readonly friendList: number[];
    readonly level: number;
    readonly webSocket: Socket;


    constructor(stats: UserOptions) {
        this.uuid = stats.uuid;
        this.name = stats.name;
        this.upgrades = stats.upgrades;
        this.friendList = stats.friendList;
        this.level = stats.level;
        this.webSocket = stats.webSocket;
    }
}
