<template>
  <!-- PART 4: Add your code here -->
  <div>
    <p>Show name: {{ name }}</p>
    <Counter v-bind:initialCount="episodes_seen" />
  </div>
</template>

<script>
import Counter from "./Counter.vue";

// PART 4: Add your code here
export default {
  components: {
    Counter
  },
  props: {
    id: Number,
    name: String,
    episodes_seen: Number
  }
};
</script>

<style>
</style>
