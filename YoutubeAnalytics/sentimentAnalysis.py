# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def sentiment_analyse(comment):
	# Instantiates a client
	try:
		client = language.LanguageServiceClient()

		# The text to analyze
		text = comment
		document = types.Document(
	   		content=text,
	    	type=enums.Document.Type.PLAIN_TEXT)

		# Detects the sentiment of the text
		sentiment = client.analyze_sentiment(document=document).document_sentiment
	except:
		return 0
	print('Text: {}'.format(text))
	print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
	if sentiment.score < -0.5:
		return -1
	if sentiment.score > -0.5 and sentiment.score <0.5:
		return 0
	if sentiment.score > 0.5:
		return 1


