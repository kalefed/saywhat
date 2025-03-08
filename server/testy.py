import preprocessing

if __name__ == '__main__':

    preprocessing = preprocessing.Preprocessing()

    slang_words = preprocessing.read_csv("server/all_slangs.csv")

    example_phrase = "Slay girl you are so on fleek."

    processed_text = preprocessing.clean_text(example_phrase,slang_words)
    print(processed_text)


