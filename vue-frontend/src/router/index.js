import Vue from "vue";
import Router from "vue-router";
import HomePage from "@/components/HomePage";
import ShowPage from "@/components/ShowPage";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage
    },
    {
      path: "/shows/:id",
      name: "ShowPage",
      component: ShowPage
    }
  ]
});
