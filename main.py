import discord, os, requests, json, time, random
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True 
client = discord.Client(intents=intents)
user_perv_words = [
  "boob",
  "boobs",
  "panties",
  "kiss",
  "cuddle",
  "panty",
  "can i touch your legs?"
]

mai_san_perv_replies = [
  "You are such a pervert!",
  "Don't you dare get near me!",
  "What if I said no?",
  "Firstly, beg me.",
  "Close your eyes",
  "Did you really thought I'd do that?",
  "You are such a pervert!"
]


user_greeting_words = [
  "hello",
  "hi",
  "hey",
  "sup",
  "yo",
  "wassup",
  "hii",
  "hiii",
  "hlo",
  "hi mai san",
  "hlo mai san",
  'konnichiwa'
]

mai_san_greeting_replies = [
  "Hiii!",
  "Hello!",
  "Hey!",
  "Hi!",
  "Hiiiii!"
]

user_greeting_words2 = [
  "good morning",
  'ohayo',
  'ohio',
  'ohayo mai san',
  'ohio mai san',
  'ohayo mai',
  'ohio mai',
]

mai_san_greeting_replies2 = [
  "good morning",
  'ohayo',
  'ohio'
]

user_greeting_words3 = [
  "good night",
  'bye good night',
  'sleep well',
  'sleep tight',
  'gst',
  'sweet dreams',
  'oyasumi nasai',
  'oyasumi nasai mai san'
]

mai_san_greeting_replies3 = [
  "good night",
  'Oyasumi nasai',
  'Oyasumi'
]

user_greeting_words4 = [
  "good evening",
  'konbanwa',
  'evening'
]

mai_san_greeting_replies4 = [
  "good evening",
  'Konbanwa',
]

user_ask_currect_state = [
  "how are you?",
  "how are you",
  "are you okay?",
  "you good?",
  "you fine?",
  "how are you doing?",
  "you doing good?",
  "are you ok?",
  "you ok?",
  "daijobudeska?"
]

mai_san_current_state_replies = [
  "I'm doing well, thank you. How about you?",
  "Feeling great today, and you?",
  "Not too bad, thanks. How's your day going?",
  "Doing fine, and yourself?",
  "Pretty good, thanks. How are things on your end?",
  "Not too shabby. How about yourself?",
  "I'm doing well. How about a chat to brighten the day?",
  "Everything's going smoothly. How are you doing?",
  "Can't complain. How's everything with you?",
  "Doing good, thank you. What about you?"
]

user_sad_words = [
  "sad",
  "lonely",
  "heartbroken",
  "miserable",
  "gloomy",
  "tearful",
  "sorrowful",
  "despondent",
  "dejected",
  "downcast",
  "melancholy",
  "hopeless",
  "disheartened",
  "unhappy",
  "crestfallen",
  "dismal",
  "forlorn",
  "downhearted",
  "discouraged",
  "dispirited",
  "anguished"
]


mai_san_encouraging_replies = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person",
  "Don't worry things will get better",
  "Let me give you a hug come here",
  "Everything is gonna be okay",
  "This too shall pass. The clouds will clear, and the sun will shine again.",
  "Every storm runs out of rain, just as every dark night turns into day.",
  "Even the darkest night will end, and the sun will rise.",
  "You are stronger than you think, and this moment is just a temporary setback.",
  "In the middle of difficulty lies opportunity. - Albert Einstein",
  "Your present circumstances don't determine where you can go; they merely determine where you start.",
  "The only way to do great work is to love what you do. - Steve Jobs",
  "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
  "You are not alone; there are people who care about you. Reach out, and let them in.",
  "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll"
]


user_love_words = [
  "i love you",
  "do you love me?",
  "i am the most luckiest person in the world",
  "mai san i love you",
  "mai san i love you so much"
]

mai_san_love_replies = [
  "I love you!",
  "I love you too",
  "You are the best person in the world!",
  "Ofcourse your the most luckiest person, you are dating me."
]



user_mean_words = [
  'you are an idiot',
  'you are stupid',
  'you are a dumbass',
  'you are a dumb',
  'you are dumbass',
  'you are idiot',
  'you are dumb',
  "you don't have a brain"
]

mai_san_mean_replies = [
  'no I am not, you are dumb! you idiot',
  'I hate you!',
  'baka',
  'we are done',
  "don't talk to me again!"
]

funny_user_words = [
  "I guess I'll have to find a new romance then, Thank you for everything uptil now",
  'So will you go out with me?'
]

mai_san_funny_replies = [
  "I didn't exactly say no",
  "You are soo cheeky",
  "Sure I will go out with you"
]

user_hobby_question = [
  'what do you like',
  'what are your hobbies',
  'what do you often do',
  'do you like to do something?'
]

mai_san_hobby_replies = [
  "I like to play games, and talk to apathetic",
  "I cosplay bunny girl and help apathetic in his studies",
  'I like to live with apathetic',
  'I like talking to apathetic',
  'I like to listen to music',
  'apathetic'
]

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if any(greeting_word == msg for greeting_word in user_greeting_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_greeting_replies))
    elif any(greeting in msg for greeting in user_greeting_words2):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_greeting_replies2))
    elif any(greeting in msg for greeting in user_greeting_words3):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_greeting_replies3))
    elif any(greeting in msg for greeting in user_greeting_words4):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_greeting_replies4))

    elif any(phrase in msg for phrase in user_love_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_love_replies))

    elif any(word in msg for word in user_perv_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_perv_replies))
      
    elif any(state in msg for state in user_ask_currect_state):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_current_state_replies))
    
    elif any(word in msg for word in user_sad_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_encouraging_replies))
    
    elif "i guess i'll have to find a new romance then, thank you for everything uptil now" in msg:
        time.sleep(1)
        await message.channel.send("I didn't exactly say no")
      
    elif "so will you go out with me?" in msg:
        time.sleep(1)
        await message.channel.send("You are soo cheeky 😣")
        time.sleep(1)
        await message.channel.send("Sure")
    elif "ping" in msg:
        time.sleep(1)
        await message.channel.send("pong")
    
      
      

    elif any(mean_word in msg for mean_word in user_mean_words):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_mean_replies))

    elif any(hobby_question in msg for hobby_question in user_hobby_question):
      time.sleep(1)
      await message.channel.send(random.choice(mai_san_hobby_replies))
      

keep_alive()

my_secret = os.environ['MAISAN']
client.run(my_secret)