import { create } from "zustand";

const useSearchStore = create((set, get) => ({
  search_term: null,
  trans_term: null,
  sentiment: null,
  update_search_term: (search_term) =>
    set(() => ({
      search_term,
    })),
  update_trans_term: (trans_term) =>
    set(() => ({
      trans_term,
    })),
  update_sentiment: (sentiment) =>
    set(() => ({
      sentiment,
    })),
}));

export default useSearchStore;
