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

  if sentiment>0.75:
   positive_count+=1
   return f"\n{Fore.GREEN} Very positive sendiment detected...Agent {user_name}! Score:{sentiment}"
  elif 0.25< sentiment <=0.75:
   positive_count+=1
   return f"\n{Fore.GREEN} Positive sendiment detected...Agent {user_name}! Score:{sentiment}"
  elif -0.25<= sentiment < 0.25:
   neutral_count+=1
   return f"\n{Fore.YELLOW} Neutral sendiment detected...Agent {user_name}! Score:{sentiment}"
  elif -0.75<= sentiment < 0.25:
   negative_count+=1
   return f"\n{Fore.RED} Negative sendiment detected...Agent {user_name}! Score:{sentiment}"
  else:
   negative_count+=1
   return f"\n{Fore.RED} Very Negative sendiment detected...Agent {user_name}! Score:{sentiment}"
  
def execute_command(command):
 
 global conversation_history, positive_count, negative_count, neutral_count
 if command=="summary":
  return( f"{Fore.CYAN} Mission Repost: \n" 
     f"{Fore.Green} Positive Messages Detected:{positive_count}"
     f"{Fore.RED} Negative Messages Detected:{negative_count}"
     f"{Fore.YELLOW} Neutral Messages Detected:{neutral_count}"    
         )
  
 elif commant=="reset":
  conversation_history.clear()
  positive_count=negative_count=neutral_count=0
  return f"{Fore.CYAN} Mission Reset! All prevoius messages has been deleted"
 elif command=="history":
  return"\n".join([f"{Fore.Cyan}Message{i+1}:{msg}" for i,msg in enumerate(conversation_history)])
 elif commnad=="help":
  return(f"{Fore.CYAN} Availble commands: \n"
 f"-Type any sentence to analyze its sentiment. \n"
 f"-Type 'summary' to get a amission report on analayzed sentiments.  \n"
 f"-Type 'reset' to clear all mission data and start fresh. \n"
 f"-Type 'history' to view all previous messages and analyzes. \n"
 f"-Type 'exit' to conclude yor mission and leave the chat. \n"
  )
 
 else:
  return f"{Fore.RED} Unknown command. Type 'help' for a lost of commands"