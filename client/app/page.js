import Image from "next/image";
import TextInput from "../components/TextInput";
import Fadein from "@/components/fadein";

export default function Home() {
  return (
    <Fadein>
      <div className="flex flex-col my-20 mx-20 items-center">
        {/* <div>
        <h1 className="text-center text-3xl py-4 font-bold">What was that?</h1>
      </div> */}
        <Image
          src="/titleArt.png"
          width={500}
          height={500}
          alt="Picture of the author"
          className="my-10"
        />
        <TextInput />
      </div>
    </Fadein>
  );
}
