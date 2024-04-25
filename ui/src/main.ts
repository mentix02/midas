import { createApp } from "vue";

import "bootswatch/dist/lux/bootstrap.css";
import "bootstrap-icons/font/bootstrap-icons.css";

import App from "./App.vue";
import pinia from "./stores";
import router from "./router";

const app = createApp(App);

app.use(pinia);
app.use(router);

app.mount("#app");
