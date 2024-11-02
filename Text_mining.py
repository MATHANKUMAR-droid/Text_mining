from textblob import TextBlob
def predict_sentiment(text):
  blob=TextBlob(text)
  polarity=blob.sentiment.polarity
  if polarity >0:
    return "good"
  elif polarity <0:
    return "bad"
  else:
    return "neutral"

def main():
  text = input("Enter a sentence :")
  sentiment=predict_sentiment(text)
  print("Sentiment found :",sentiment)
main()
_______________________________________________________________________________________________________________________________________________________________________________________________
Output:
Enter a sentence :i am feeling good today
Sentiment found : good
_______________________________________________________________________________________________________________________________________________________________________________________________
from textblob import TextBlob
def predict_sentiment(text):
  blob=TextBlob(text)
  polarity=blob.sentiment.polarity
  if polarity >0:
    return "good"
  elif polarity <0:
    return "bad"
  else:
    return "neutral"

def main():
  text = input("Enter a sentence :")
  sentiment=predict_sentiment(text)
  print("Sentiment found :",sentiment)
main()
_______________________________________________________________________________________________________________________________________________________________________________________________
Output:
Enter a sentence :this is the worst day i have experience
Sentiment found : bad
_____________________________________________________________________________________________________________________________________________________________________________________________
from textblob import TextBlob
def predict_sentiment(text):
  blob=TextBlob(text)
  polarity=blob.sentiment.polarity
  if polarity >0:
    return "good"
  elif polarity <0:
    return "bad"
  else:
    return "neutral"

def main():
  text = input("Enter a sentence :")
  sentiment=predict_sentiment(text)
  print("Sentiment found :",sentiment)
main()
_____________________________________________________________________________________________________________________________________________________________________________________________
Output:
Enter a sentence :madhavan is a boy 
Sentiment found : neutral
_____________________________________________________________________________________________________________________________________________________________________________________________
