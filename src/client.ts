import {query} from 'express';
import io from 'socket.io-client';
const socket = io("ws://localhost:3000",{
    query: {
        name: "guilherme",
        level: 1,
        upgrades: '123123'
    }

});

socket.on("connect", () => {
  socket.emit("createLobby", "Hello!")
});

// handle the event sent with socket.send()
socket.on("message", (data: string) => {
  console.log(data);
});

socket.on('joinedLoby', (message:string) => {
    console.log('lobby joined. UUID Is ' + message);
});

// handle the event sent with socket.emit()
socket.on("greetings", (elem1: any, elem2:any, elem3:any) => {
  console.log(elem1, elem2, elem3);
});
