<template>
  <div
    class="card"
    @click="emitShowClicked"
  >
    <!-- TODO: display show name and episodes watched -->
    <p><strong>Show Name: </strong>{{ showName }}</p>
    <p><strong>Episodes Watched: </strong>{{ episodesWatched }}</p>
    <button
      type="button"
      id="remove-button"
      class="btn btn-sm btn-outline-danger"
      @click="emitShowDeleted"
    >Remove</button>
  </div>
</template>

<script>
export default {
  // TODO: add props for showName and episodesWatched
  props: {
    showName: String,
    episodesWatched: Number
  },
  methods: {
    emitShowClicked: function () {
      this.$emit('show-clicked')
    },
    emitShowDeleted: function () {
      this.$emit('show-removed')
    }
  }
}
</script>

<style scoped>
div {
  width: 50%;
  text-align: left;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 25px;
  padding-right: 25px;
  margin: 10px;
}

div:hover {
  background-color: rgb(241, 241, 241);
}

#remove-button {
  width: 75px;
}
</style>