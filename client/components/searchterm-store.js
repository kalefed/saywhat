import { create } from "zustand";

const useSearchStore = create((set, get) => ({
  search_term: null,
  update: (search_term) =>
    set(() => ({
      search_term,
    })),
}));

export default useSearchStore;
