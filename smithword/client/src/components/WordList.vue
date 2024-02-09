<template>
    <div class="ordered-list-component">
      <h1>List Generator</h1>
      <div class="input-container">
        <label for="countInput">Enter a positive number:</label>
        <input type="number" id="countInput" v-model="count" placeholder="Enter a positive number">
        <input type="text" id="wordInput" v-model="word" placeholder="Enter a starting word">
      </div>
  
      <button @click="fetchOrderedList">Submit</button>
  
      <div class="visualisation-container" v-if="orderedList">
        <ul>
          <li v-for="item in orderedList">{{ item }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    setup() {
      const count = ref(1);
      const word = ref('');
      const orderedList = ref([]);
  
      async function fetchOrderedList() {
        try {
          console.log('word.value : ' + word.value)
          const response = await fetch('http://localhost:5000/generate?length=' + count.value + '&startingWord=' + (word.value));

          const statusCode =  response.status;
          console.log('Response Code : ' + statusCode)
          //console.log('Response json : ' + await response.json())
          orderedList.value = await response.json();
          console.log('OrderedList : ' + orderedList.value)
        }
        catch (error) {
            console.log(error.message)
        }
      }
  
      return {
        count,
        word, 
        orderedList,
        fetchOrderedList,
      };
    },
  };
  </script>
  
  <style scoped>
  .ordered-list-component {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin: 20px;
  }
  
  .input-container {
    margin-bottom: 20px;
  }
  
  .label {
    margin-bottom: 5px;
  }
  
  input[type="number"] {
    width: 50px;
  }
  
  button {
    padding: 10px 20px;
    cursor: pointer;
  }
  
  .visualisation-container {
    margin-top: 20px;
  }
  
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  
  ul li {
    margin-bottom: 10px;
  }
  </style>