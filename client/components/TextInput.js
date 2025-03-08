"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { sendTranslation } from "@/lib/action";
import useStore from "@/lib/searchterm-store";

export default function TextInput() {
  const router = useRouter();
  const [sentence, setSentence] = useState("");

  const translateClick = (event) => {
    event.preventDefault();
    router.push("translation");
  };

  const textChange = (event) => {
    setSentence(event.target.value);
  };

  return (
    <form className="flex gap-2 w-3/4">
      <input
        type="text"
        onChange={textChange}
        placeholder="Text to translate here"
        className="p-2 outline flex-3/4 rounded-md"
        value={sentence}
      />
      <button onClick={translateClick}>Translate</button>
    </form>
  );
}
