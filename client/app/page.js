import Image from "next/image";
import TextInput from "../components/TextInput";
import Fadein from "@/components/fadein";

export default function Home() {
  return (
    <Fadein>
      <div className="flex flex-col my-20 mx-20 items-center">
        <Image
          src="/titleArt.png"
          width={500}
          height={500}
          alt="Picture of the author"
          className="my-10"
        />
        <p className="text-[#F3571D]">
          Confused by a message you received? Put it in the box below to
          translate from slang to plain language
        </p>
        <p className="text-[#b3b3b3] mb-10">
          Bonus: we’ll let you know if the connotation was positive or negative
          overall.
        </p>
        <TextInput />
      </div>
    </Fadein>
  );
}
