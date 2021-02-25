import { Player } from '../user/player';
import { User } from '../user/user';
import { userToPlayer } from '../utils/userToPlayer';

enum Difficulty {
    Easy,
    Medium,
    Hard
}

export class Lobby {
    hasStarted: boolean = false;
    players: Player[] = [];
    entities = [];
    seed: number;
    uuid: number;
    difficulty: Difficulty = Difficulty.Medium;

    constructor(seed: number, uuid: number) {
        this.seed = seed // imagine it was a random numbre
        this.uuid = uuid;
    }

    addPlayer(user: User) {
        user.webSocket.join(`${this.uuid}`)
        user.webSocket.emit('joinedLoby', this.uuid);
        this.players.push(userToPlayer(user, {runLevel: 0,
                            lobbyUUID: this.uuid,
                            runUpgrades: [],
                            achievements: []
        }));

    }


}
