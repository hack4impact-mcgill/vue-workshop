<template>
  <div>
    <p>I'm a Counter!</p>
    <p>Current count: {{ count }}</p>
    <button type="button" v-on:click="count += 1">Add 1</button>
    <button type="button" v-on:click="count -= 1">Subtract 1</button>
  </div>
</template>

<script>
export default {
  props: {
    initialCount: Number
  },
  data() {
    return {
      count: this.initialCount
    };
  }
};
</script>

<style>
</style>

