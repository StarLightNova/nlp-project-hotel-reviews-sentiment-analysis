<template>
  <div class="container">
    <textarea cols="80" rows="10" placeholder="Your review to the hotel" v-model.lazy.trim='text'></textarea>
  </div>
  <button @click="fireFunction()" class="easy-buttons">Analyze 🔍</button>
  <div class="container">
    <p v-if="result !== null" class="emojiResult">{{result === '1' ? '😍' : '😥'}}</p>
  </div>
</template>

<script>


import axios from 'axios';
export default {
  name: 'EasyForm',
  data() {
    return {
      text: '',
      result: null,
    }
  },
  methods: {
    fireFunction() {
      axios({
        method: 'post',
        url: 'http://localhost:3000/training',
        data: {'input_x_train' : this.text}
      });
      this.text = '';
    },
    anySentiment() {
      axios({
        method: 'get',
        url: 'http://localhost:3000/sentiments',
      }).then(response => response.data)
        .then(obj => this.result = obj[obj.length - 1].sentiment);
    }
  },
  mounted() {
    this.anySentiment();
  }
}
</script>

<style scoped>
  .easy-buttons {
    width: 256px;
    height: 64px;
    background-color: rgba(142, 207, 132, 1);
    cursor: pointer;
    border: none;
    color: #fff;
    font-size: 42px;
    border-radius: 8px;
  }

  .emojiResult {
    font-size: 52px;
  }
</style>
