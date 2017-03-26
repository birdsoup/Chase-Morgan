import markovify

def generateMemeText:
	with open("./corpus.txt") as f:
    text = f.read()
	text_model = markovify.Text(text)
	top = text_model.make_sentence()
	bottom = text_model.make_sentence()
	return [top, bottom]