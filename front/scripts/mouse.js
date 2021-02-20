var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var websocket = new WebSocket("ws://127.0.0.1:8765/");
var cords = [[0,0]]
var local_cords = [[0, 0]]

websocket.onmessage = function (event) {
    data = JSON.parse(event.data);
    switch (data.type) {
        case 'mouse_move':
            cords = data.cords;
            console.log(data.cords)
            draw();
            break;
        default:
            console.error(
                "unsupported event", data);
    }
};

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "black";
    for (let i = 0; i < cords.length; i++){
        ctx.fillRect(cords[i][0] - 5, cords[i][1] -5, 10, 10);
    }
}


canvas.addEventListener('mousemove', e => {
    local_cords = [e.offsetX, e.offsetY];
    websocket.send(JSON.stringify({"action":"mouse_move", 'value': [e.offsetX, e.offsetY]}))
})
