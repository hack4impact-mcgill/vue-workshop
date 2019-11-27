<template>
  <div>
    <center>
      <h3>My Shows</h3>
      <div
        id="input-container"
        class="container"
      >
        <div class="row">
          <div class="col-6">
            <input
              class="form-control"
              type="text"
              placeholder="Show Name"
              v-model="newShowName"
            >
          </div>
          <div class="col-4">
            <input
              class="form-control"
              type="text"
              placeholder="Episodes Seen"
              v-model="newShowEpisodesWatched"
            >
          </div>
          <div class="col-2">
            <!-- TODO: call createShow when this button is clicked -->
            <button
              type="button"
              class="btn btn-md btn-outline-primary"
            >Add</button>
          </div>
        </div>
      </div>

      <hr>
      <!-- TODO: Render a list of ShowItem components here -->
      <!-- TODO: Capture the show-clicked event -->
      <!-- TODO: Capture the show-removed event -->

    </center>
  </div>
</template>

<script>
import * as mockdb from '@/mockdb'
import Router from '@/router'
import ShowItem from './ShowItem.vue'

export default {
  components: {
    ShowItem
  },
  // TODO: add data variables for shows, newShowName and newShowEpisodesWatched

  methods: {
    goToShow: function (id) {
      Router.push({ path: '/shows/' + id })
    },
    // TODO: add the createShow and removeShow functions

  }
};
</script>

<style scoped>
h3 {
  margin: 35px;
}

hr {
  margin-top: 1rem;
  margin-bottom: 1rem;
  border: 0;
  width: 50%;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

#input-container {
  width: 50%;
}
</style>


