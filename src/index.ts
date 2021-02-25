import { WebSocket } from './socket'
import { LobbyManager } from './lobby/lobbyManager';

const app = require('express')();
const http = require('http').createServer(app);

const websocket = new WebSocket(http); 
const lobbyManager = new LobbyManager(websocket);

app.get('/', (req:any, res:any) => {
  res.sendFile('hi');
});

http.listen(3000, () => {
  console.log('listening on *:3000');
});

