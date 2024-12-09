const WebSocket = require('ws');

const server = new WebSocket.Server({ port: 8080 });

server.on('connection', ws => {
  ws.send('Hello World, my name is Daniela Cáceres!');
});
console.log("WebSocket server listening on port 8080");
