"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import useSearchStore from "@/components/searchterm-store";

export default function TextInput() {
  const router = useRouter();
  const { search_term, update } = useSearchStore();
  const [sentence, setSentence] = useState("");

  const translateClick = (event) => {
    event.preventDefault();
    update(sentence);
    router.push("translation");
  };

  const textChange = (event) => {
    setSentence(event.target.value);
    // update(event.target.value);
  };

  return (
    <form className="flex gap-2 w-3/4">
      <input
        type="text"
        onChange={textChange}
        placeholder="Text to translate here"
        className="p-2 outline flex-3/4 rounded-md"
        value={sentence}
        required
      />
      <button
        className="border rounded-md border-[#F3571D] text-[#F3571D] py-2 px-4"
        onClick={translateClick}
      >
        Translate
      </button>
    </form>
  );
}
