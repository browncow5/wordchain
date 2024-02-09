<template>
  <div>
    <h1>WebSocket messages:</h1>
    <div class="word-feed" >
      <ul class="messages">
        <li v-for="message in messages" :key="message.id">{{ message }}</li>
      </ul>
    </div>
  </div>
  </template>
  
  <script>
    import { ref, watchEffect, inject } from 'vue';
  
  export default {
    setup() {
      const messages = ref([]);
      const maxMessages = 10;
  
    // Get the WebSocket connection from the parent App.vue
    const socket = inject('socket');

      console.log('WebSocket connection established');
  
      // Subscribe to the 'message' event
      socket.on('message', (message) => {
        console.log(`Received message: ${message}`);
        // Add the message to the list
        messages.value.push(message);
  
        // Trim the list to the maximum length
        if (messages.value.length > maxMessages) {
          messages.value.shift();
        }
      });

    // Use watchEffect to trigger a re-render whenever the messages array changes
    watchEffect(() => {
      console.log('Messages changed:', messages.value);
    });
  
      // Return the data and methods to be used in the template
      return { messages };
    },
  };
  </script>

<style scoped>
.word-feed {
  background-color: #f5f5f5;
  padding: 2rem;
  border-radius: 1rem;
  width: 50%;
  margin: 0 auto;
  max-height: 70vh;
  display: flex;
  flex-direction: column;
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  margin-bottom: 1rem;
  color: #535353;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.messages {
  flex-grow: 1;
  overflow-y: auto;
  list-style: none;
  padding: 0;
  margin: 0;
}

.messages li {
  padding: 1rem;
  background-color: #fff;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
  color: black;
}

@media (min-width: 1024px) {
  .word-feed {
    width: 40%;
    height: 40%;
    
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>