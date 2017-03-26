import markovify

def generateMemeText(top, bottom):
	with open("./joke_corpus.txt") as f:
		text = f.read()
		text_model = markovify.Text(text)
		top = text_model.make_sentence()
		bottom = text_model.make_sentence()
		return [top, bottom]

t = raw_input("Enter top text keyword: ")
b = raw_input("Enter bottom text keyword: ")
res = generateMemeText(t,b)
print res[0]
print res[1]
