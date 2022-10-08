
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.getcwd(), "GCloud.json")
from google.cloud import language_v1

client = language_v1.LanguageServiceClient()

# The text to analyze
text = "Hello, world!"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print(sentiment.score)
print(sentiment.magnitude)