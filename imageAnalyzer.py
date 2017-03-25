from PIL import Image
import os
import indicoio
import operator

indicoio.config.api_key  = 'bae2f65f53a35768c0d6c90aa1d3b37b'

imageFeaturesFile = open("imageFeatures.chase","w")
memes = [Image.open("memes/"+filename) for filename in os.listdir('memes/')]#get list of meme images

imageFeatures = indicoio.image_recognition(memes)

#print(imageFeatures)
print(max(imageFeatures[0].iteritems(), key=operator.itemgetter(1))[0])




