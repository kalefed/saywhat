import TextInput from "../components/TextInput";

export default function Home() {
  return (
    <div className="flex flex-col my-20 mx-20 items-center">
      <div>
        <h1 className="text-center text-3xl py-4 font-bold">
          Texty Translatey
        </h1>
      </div>
      <TextInput />
    </div>
  );
}
