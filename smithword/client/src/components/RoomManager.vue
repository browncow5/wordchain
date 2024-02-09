<template>
    <div class="room-manager">
      <h2>Room Manager</h2>
      <div>
        <button @click="createRoom">Create Room</button>
      </div>
      <div>
        <input v-model="roomToken" type="text" :placeholder="placeholderText" />
        <button @click="joinRoom">Join Room</button>
      </div>
      <div>
        <p>Connected to room: {{ currentRoom }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, inject } from 'vue';
  
  export default {
    setup() {
      const roomToken = ref('');
      const placeholderText = 'Enter room token';
      const socket = inject('socket');
      const currentRoom = ref('default');
  
      const createRoom = () => {
        // Generate a unique token for a new room
        const newRoomToken = Math.random().toString(36).substr(2, 8);
        console.log(`Creating new room with token: ${newRoomToken}`);
  
        // Update the placeholder text
        roomToken.value = `${newRoomToken}`;
  
        // Emit an event to create the new room on the server
        socket.emit('create_room', newRoomToken);
      };
  
      const joinRoom = () => {
        console.log(`Joining room with token: ${roomToken.value}`);
  
        // Emit an event to join the room on the server
        socket.emit('join_room', roomToken.value);

        // Update room variables
        currentRoom.value = roomToken.value;
      };
  
      return { roomToken, createRoom, joinRoom, placeholderText, currentRoom };
    },
  };
  </script>
  
  <style scoped>
  .room-manager {
    margin-bottom: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  </style>
  