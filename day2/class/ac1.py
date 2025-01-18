from textblob import textblob
import colorama
from colorama Fore, Style
import sys
import time

colorama.init(autoreset=True)

user_name=""
conversation_history=[]
positive_count=0
negative_count=0
neutral_count=0

def processing_animation():
 print(f"{Fore.GREEN} Detecting sentiment clues",end="")
 for _ in range(3):
  time.sleep(0.5)
  print(".",end="")

def analyze_sentiemnt(text):
 """
 Polarity:
 --positive: polarity> -0.25
 --negative:polarity< -0.25
 """

 global positive_count,negative_count,neutral_count

 try:
  blob= Textblob(text)
  sentiment=blob.sentiment.polarity
  conversation_history.append(text)
