const express = require('express');
const app = express();
const cors = require('cors');

const http = require('http');
const socketio = require('socket.io');
const { Server } = require("socket.io");

app.use(cors());

app.use(express.static(__dirname + '/dist'))
app.listen(3000, () => {
  console.log('Express Server listening on: http://localhost:%s', 3000)
})

const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: ["http://localhost:5173","http://localhost:3000","http://localhost:3001"],
    methods: ["GET", "POST"],
  },
});

io.on('connection', (socket) => {
  console.log(`Client connected: ${socket.id}`);

  socket.on('disconnect', () => {
    console.log(`Client disconnected: ${socket.id}`);
  });

  socket.on('message', (data) => {
    console.log(`Received message from ${socket.id}: ${data}`);
    receiveMessage(socket, data);
  });

  socket.on('create_room', (roomToken) => {
    console.log(`Creating room with token: ${roomToken}`);
    createRoom(socket, roomToken);
  });

  socket.on('join_room', (roomToken) => {
    console.log(`Joining room with token: ${roomToken}`);
    joinRoom(socket, roomToken);
  });

  function receiveMessage(socket, data) {
    // ...
    broadcastMessage(socket.room, data);
  }

  function broadcastMessage(room, data) {
    io.to(room).emit('message', data);
  }

  function createRoom(socket, roomToken) {
    socket.join(roomToken);
    socket.room = roomToken;
    console.log(`Room ${roomToken} created by ${socket.id}`);
  }

  function joinRoom(socket, roomToken) {
    const room = io.sockets.adapter.rooms.get(roomToken);
    if (room) {
      socket.join(roomToken);
      socket.room = roomToken;
      console.log(`${socket.id} joined room ${roomToken}`);
    } else {
      console.log(`${socket.id} tried to join non-existent room ${roomToken}`);
    }
  }
});

server.listen(3001, () => {
  console.log('Socket Server is listening on port 3001');
});