<template>
  <div class="container">
    <textarea cols="80" rows="10" placeholder="Your review to the hotel" v-model.lazy.trim='text'></textarea>
  </div>
  <div class="container with-flex">
    <div class="inner-container">
      <select v-model="trained_model">
        <option v-for="model in all_models" :key="model.id" :value="model.file_name">
          {{model.label}}
        </option>
      </select>
    </div>
    <div class="inner-container">
      <button @click="fireFunction()" class="easy-buttons">Analyze 🔍</button>
    </div>
  </div>
  <div class="container">
    <p v-if="result !== null" class="emojiResult">{{result.sentiment === 1 ? '👍' : '👎'}}</p>
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
      all_models: [],
      trained_model: 'log_trained.sav',
    }
  },
  methods: {
    getAllModels() {
      axios({
        method: 'get',
        url: 'http://localhost:3000/models',
      }).then(response => {
        this.all_models = response.data;
        this.trained_model = this.all_models[0].file_name;
      });
    },
    fireFunction() {
      axios({
        method: 'post',
        url: 'http://localhost:5006/get_trained_data',
        headers: {
          'Content-type' : 'application/json',
        },
        data: {text: this.text, model: this.trained_model},
      }).then(response => {
        this.result = response.data
        return this.result.sentiment;
      });
      this.text = '';
    },
  },
  mounted() {
    this.getAllModels();
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
    box-shadow: 0px 5px 25px #000;
  }

  .emojiResult {
    font-size: 52px;
  }

  .with-flex {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column-reverse;
  }

  .with-flex .inner-container{
    margin: 16px 0px;
  }

  select {
    padding: 8px 8px;
    border-radius: 8px;
    outline: none;
    box-shadow: 0px 5px 15px;
  }

  textarea { 
    outline: none;
    border-radius: 8px;
    padding: 16px;
    font-size: 16px;
    box-shadow: 0px 5px 15px;
  }
</style>
