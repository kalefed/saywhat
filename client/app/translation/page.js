"use client";

import useSearchStore from "@/components/searchterm-store";
import Image from "next/image";

export default function Page() {
  const { search_term, trans_term, sentiment } = useSearchStore();

  return (
    <div className="flex flex-col my-20 mx-20 items-center">
      {/* <h1 className="text-3xl py-4 font-bold text-center">Your Translation</h1>
       */}
      <div className="w-full flex items-center justify-center">
        <Image
          src="/translation.png"
          width={500}
          height={500}
          alt="Picture of the author"
          className="mt-10"
        />
      </div>
      <div className="flex flex-row gap-4 w-4/6">
        <div className="flex flex-col gap-4 justify-center">
          <div className="flex flex-row gap-2">
            <p className="font-bold">Original Phrase:</p>
            <p className="text-[#757575]">{search_term}</p>
          </div>

          <div className="flex flex-row gap-2">
            <p className="font-bold whitespace-nowrap">Translated Phrase:</p>
            <p className="text-[#757575]">{trans_term}</p>
          </div>
        </div>
        <Image
          src={`/${sentiment}.png`}
          width={300}
          height={300}
          alt="Picture of the author"
          className="my-10"
        />
      </div>
    </div>
  );
}
