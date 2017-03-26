import markovify

def generateMemeText():
    with open("../corpus2.txt") as f:
        text = f.read()
        text_model = markovify.Text(text)
        text = text_model.make_sentence(tries=1000)
        return text