<template>
  <div>
    <h1>Socket Example</h1>
    <input v-model="message" type="text" placeholder="Type a message" />
    <button @click="sendMessage">Send</button>
    <ul>
      <li v-for="msg in messages" :key="msg">{{ msg }}</li>
    </ul>
  </div>
</template>

<script>
import { io } from 'socket.io-client';

export default {
  data() {
    return {
      message: '',
      messages: [],
    };
  },
  created() {
    const socket = io(process.env.VUE_APP_SOCKET_ENDPOINT);

    socket.on('connect', () => {
      console.log('Connected to server');
    });

    socket.on('message', (message) => {
      console.log('Received message from server:', message);
      this.messages.push(message);
    });

    this.socket = socket;
  },
  beforeUnmount() {
    this.socket.disconnect();
  },
  methods: {
    sendMessage() {
      this.socket.emit('message', this.message);
      this.message = '';
    },
  },
};
</script>
