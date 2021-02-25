import * as socketio from 'socket.io'
import { User } from './user/user';
/**
 * Guilhere Samore
 * 22 Dec 2020
 * Handles the socket.io back end connection. 
 **/

interface ExternalConfig {
    function: Function;
    class: object;
}

export class WebSocket {
    private readonly io: socketio.Server;
    private connections: {[id: string]: User} = {};
    events: Function[] = [
        // listeners
        this.eDisconnect,
        this.eMessage
    ];

    externalEvents: ExternalConfig[] = [];

    constructor (http:any) {
        this.io = new socketio.Server(http);
        this.onConnection(this);
    }

    public sendChat(message: string) {
        this.io.emit('message', message);
    }

    private onConnection(that: WebSocket) {
        this.io.on('connection', (socket: socketio.Socket) => {
            let uuid = Math.floor(Math.random() * 100);
            this.connections[socket.id] = new User({
                name: 'placeholder name until we get a DB',
                uuid: uuid,
                level: 1,
                upgrades: 'nothing!',
                webSocket: socket,
                friendList: []
            });

            console.log(socket.handshake.query);
            socket.emit('message', 'Hey there');
            console.log('connect');
            that.addListeners(socket);
        });
    }

    // This is executed on every single new socket
    private addListeners(socket: socketio.Socket) {
        this.events.map((event) => event(this, socket));
        this.externalEvents.forEach(x => x.function(x.class, socket));
    }

    private eDisconnect(that: WebSocket, socket: socketio.Socket) { 
        socket.on('disconnect', function() {
            delete that.connections[socket.id];
            console.log('disconnect');
        });
    }

    private eMessage(that: WebSocket, socket: socketio.Socket) {
        socket.on('chat message', (msg:string) => {
            console.log(msg);
        });
    }

    getUserByWebsocket(socket: socketio.Socket): User | undefined {
        if (this.connections[socket.id]) {
            return this.connections[socket.id];
        }
        console.error('getUserByWebsocket failed. User not found!')
    };
}
