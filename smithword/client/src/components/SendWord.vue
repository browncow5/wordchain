<template>
  <div class="send-word">
    <div>
      <input v-model="message" type="text" />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
  </template>
  
  <script>
  import { ref, inject } from 'vue';
  
  export default {
    setup() {
      const message = ref('');
      const socket = inject('socket'); // Get the WebSocket connection from the parent App.vue
  
      function sendMessage() {
        socket.emit('message', message.value);
        message.value = '';
      }
  
      return {
        message,
        sendMessage,
      };
    },
  };
  </script>
  
  <style scoped>
  .send-word {
    margin-bottom: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>

