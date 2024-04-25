import { defineStore, acceptHMRUpdate } from "pinia";

import type { TokenResponse } from "@/api/types/auth";

type AuthState = {
  token?: string;
  username?: string;
};

const useAuthStore = defineStore("auth", {
  state: (): AuthState => ({ token: undefined, username: undefined }),

  getters: {
    isAuthenticated(): boolean {
      return !!this.token;
    },
  },

  actions: {
    logout() {
      this.$reset();
    },

    login(tokenResponse: TokenResponse, username: string) {
      this.username = username;
      this.token = tokenResponse.token;
    },
  },
  persist: true,
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAuthStore, import.meta.hot));
}

export default useAuthStore;
