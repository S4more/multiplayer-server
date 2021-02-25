import { User, UserOptions } from '../user/user';
import { Player, PlayerOptions } from '../user/player';

export function userToPlayer(user: User, playerOptions: PlayerOptions): Player {
    let userOptions: UserOptions = {
        name: user.name,
        uuid: user.uuid,
        level: user.level,
        upgrades: user.upgrades,
        webSocket: user.webSocket,
        friendList: user.friendList
    }
    return new Player(userOptions, playerOptions);
}
