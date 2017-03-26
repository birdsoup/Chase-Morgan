import markovify

def generateMemeText(input):
    with open("../meme_corpus.txt") as f:
        text = f.read()
        text_model = markovify.NewlineText(text)
        try:
            text = text_model.make_sentence_with_start(input)
        except KeyError:
            text = text_model.make_sentence(tries=100)
        return text