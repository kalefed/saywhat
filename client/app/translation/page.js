"use client";

import useSearchStore from "@/components/searchterm-store";

export default function Page() {
  const { search_term } = useSearchStore();
  return (
    <>
      <p>translate page</p>
      <p>{JSON.stringify(search_term)}</p>
    </>
  );
}
