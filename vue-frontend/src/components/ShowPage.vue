<template>
  <center>
    <h3>Edit Show</h3>
    <div class="card">
      <p>Show Name</p>
      <input
        class="form-control"
        type="text"
        v-model="showName"
      >
      <p>Episodes Seen</p>
      <input
        class="form-control"
        type="text"
        v-model="episodesWatched"
      >
      <button
        type="button"
        class="btn btn-sm btn-outline-primary"
        @click="updateShow"
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
  created: function () {
    const show = mockdb.getShowById(this.id)
    this.showName = show.name
    this.episodesWatched = show.episodes_seen
  },
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