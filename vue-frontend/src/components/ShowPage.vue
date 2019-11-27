<template>
  <center>
    <h3>Edit Show</h3>
    <div class="card">
      <p>Show Name</p>
      <!-- TODO: add v-model for showName -->
      <input
        class="form-control"
        type="text"
      >
      <p>Episodes Seen</p>
      <!-- TODO: add v-model for episodesWatched -->
      <input
        class="form-control"
        type="text"
      >
      <!-- TODO: call updateShow on click -->
      <button
        type="button"
        class="btn btn-sm btn-outline-primary"
      >Update</button>
    </div>
  </center>
</template>

<script>
import * as mockdb from '@/mockdb'
import Router from '@/router'

export default {
  data () {
    return {
      id: parseInt(this.$route.params.id),
      showName: "",
      episodesWatched: 0
    }
  },
  // TODO: implement the created lifecycle hook
  // get the show and set showName and episodesWatched

  methods: {
    updateShow: function () {
      mockdb.updateShowById(this.id, this.showName, parseInt(this.episodesWatched))
      Router.push({ path: "/" })
    }
  }
}
</script>

<style scoped>
h3 {
  margin: 35px;
}

div {
  width: 50%;
  text-align: left;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 25px;
  padding-right: 25px;
  margin: 10px;
}

input {
  margin-bottom: 10px;
}

button {
  width: 75px;
}
</style>