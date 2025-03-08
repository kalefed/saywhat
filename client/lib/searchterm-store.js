import { create } from "zustand";

const useStore = create((set, get) => ({
  search_term: "",
}));

export default useStore;
