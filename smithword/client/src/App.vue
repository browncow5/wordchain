<script setup>
import { ref, provide } from 'vue';
import io from 'socket.io-client';

import HelloWorld from './components/HelloWorld.vue'
import SendWord from './components/SendWord.vue';
//import TheWelcome from './components/TheWelcome.vue'
import WordFeed from './components/WordFeed.vue';
import RoomManager from './components/RoomManager.vue';
import WordList from './components/WordList.vue'


const socket = io('http://localhost:3001');
provide('socket', socket);
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <div>
      <RoomManager></RoomManager>
    </div>
    <div>
      <WordFeed></WordFeed>
      <SendWord></SendWord>
    </div>
    <div>
      <WordList></WordList>
    </div>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
