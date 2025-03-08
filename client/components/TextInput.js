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
  };

  async function onSubmit(event) {
    event.preventDefault();
    update(sentence);

    const response = await fetch("http://127.0.0.1:8000/translations", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json", // Make sure to set the Content-Type to application/json
      },
      body: JSON.stringify({ text: sentence }),
    });

    // Handle response if necessary
    const data = await response.json();

    console.log(data);

    router.push("translation");
  }

  return (
    <form className="flex gap-2 w-3/4" onSubmit={onSubmit}>
      <input
        type="text"
        name="term"
        onChange={textChange}
        placeholder="Text to translate here"
        className="p-2 outline flex-3/4 rounded-md"
        value={sentence}
        required
      />
      <button
        className="border rounded-md border-[#F3571D] text-[#F3571D] py-2 px-4"
        type="submit"
      >
        Translate
      </button>
    </form>
  );
}
