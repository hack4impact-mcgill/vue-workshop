var shows = [
  { id: 1, name: "Game of Thrones", episodes_seen: 0 },
  { id: 2, name: "Naruto", episodes_seen: 220 },
  { id: 3, name: "Black Mirror", episodes_seen: 3 }
];

let id = 4;

/* Mock DB API Functions */

function getShowById(id) {
  return shows.find(show => show.id == id);
}

function createShow(name, episodesSeen) {
  let show = { id: id, name: name, episodes_seen: episodesSeen };
  shows.push(show);
  id++;
}

function updateShowById(id, name, episodesSeen) {
  for (var i = 0; i < shows.length; i++) {
    if (shows[i].id === id) {
      shows[i].name = name;
      shows[i].episodes_seen = episodesSeen;
      break;
    }
  }
}

function deleteShowById(id) {
  for (var i = 0; i < shows.length; i++) {
    if (shows[i].id === id) {
      shows.splice(i, 1);
      break;
    }
  }
}

export { shows, getShowById, createShow, updateShowById, deleteShowById };
