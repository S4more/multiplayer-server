import { WebSocket } from '../socket';
import { Socket } from 'socket.io';
import { Lobby } from './lobby';
import { User } from '../user/user';

export class LobbyManager {
    private lobbies: Lobby[] = [];
    private uuidCounter: number = 0;
    private webSocket: WebSocket;

    constructor(webSocket: WebSocket) {
        this.webSocket = webSocket;
        this.webSocket.externalEvents.push({class: this, function: this.eCreateLobby});
    }

    private generateSeed() {
        return Math.floor(Math.random() * 100) + 1;
    }

    createLobby(): Lobby {
        let lobby = new Lobby(this.generateSeed(), this.uuidCounter);
        this.uuidCounter += 1;
        this.lobbies.push(lobby);
        return lobby;
    }

    removeLobby(lobby: Lobby) {
        //lobby.desintegrate()
        this.lobbies.splice(this.lobbies.indexOf(lobby));
    }

    private getLobbyByUUID(uuid: number | string): Lobby | undefined {
        if (typeof uuid == 'string') uuid = +uuid;
        return this.lobbies.find(lobby => lobby.uuid == uuid);
    }

    private joinLobby(user: User, lobbyUUID: number) {
        let lobby = this.getLobbyByUUID(lobbyUUID);
        if ( lobby ) {
            lobby.addPlayer(user);
        } else {
            console.log('Lobby not found!');
        }

    }

    private eCreateLobby(that: LobbyManager, socket: Socket) {
        socket.on('createLobby', (msg:string) => {
            let lobby = that.createLobby();
            socket.emit('lobbyCreated', lobby.uuid);
            let user = that.webSocket.getUserByWebsocket(socket);
            if (user) {
                that.joinLobby(user, lobby.uuid);
            }
        });
    }

}
