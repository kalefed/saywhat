"use client";

import useSearchStore from "@/components/searchterm-store";

export default function Page() {
  const { search_term, trans_term } = useSearchStore();
  return (
    <div className="flex flex-col my-20 mx-20 items-center">
      <h1 className="text-center text-3xl py-4 font-bold">translate page</h1>
      <p>{JSON.stringify(search_term)}</p>
      <p>{JSON.stringify(trans_term)}</p>
    </div>
  );
}
