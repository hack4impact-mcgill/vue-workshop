<template>
  <div>
    <center>
      <h3>My Shows</h3>
      <div id="input-container" class="container">
        <div class="row">
          <div class="col-6">
            <input
              class="form-control"
              type="text"
              placeholder="Show Name"
              v-model="newShowName"
            />
          </div>
          <div class="col-4">
            <input
              class="form-control"
              type="text"
              placeholder="Episodes Seen"
              v-model="newShowEpisodesWatched"
            />
          </div>
          <div class="col-2">
            <!-- TODO: call createShow when this button is clicked -->
            <button
              type="button"
              class="btn btn-md btn-outline-primary"
              @click="createShow"
            >
              Add
            </button>
          </div>
        </div>
      </div>

      <hr />
      <!-- TODO: Render a list of ShowItem components here -->
      <!-- TODO: Capture the show-clicked event -->
      <!-- TODO: Capture the show-removed event -->
      <ShowItem
        v-for="show in shows"
        v-bind:key="show.id"
        v-bind:showName="show.name"
        v-bind:episodesWatched="show.episodes_seen"
        @show-clicked="goToShow(show.id)"
        @show-removed="removeShow(show.id)"
      />
    </center>
  </div>
</template>

<script>
import * as mockdb from "@/mockdb";
import Router from "@/router";
import ShowItem from "./ShowItem.vue";

export default {
  components: {
    ShowItem
  },
  // TODO: add data variables for shows, newShowName and newShowEpisodesWatched
  data() {
    return {
      shows: mockdb.shows,
      newShowName: "",
      newShowEpisodesWatched: null
    };
  },
  methods: {
    goToShow: function(id) {
      Router.push({ path: "/shows/" + id });
    },
    // TODO: add the createShow and removeShow functions
    createShow: function() {
      mockdb.createShow(
        this.newShowName,
        parseInt(this.newShowEpisodesWatched)
      );
    },
    removeShow: function(id) {
      mockdb.deleteShowById(id);
    }
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
