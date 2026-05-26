from voice_controller import speak_dynamic, interrupt

print("Dynamic Voice Response Manager Started")

while True:
    user = input("You: ").lower()

    if user == "stop":
        interrupt()
        continue\
        
    elif "hy" in user:
        response = "Hello Kolu Rashmitha, hope your good."

    elif "how are you" in user:
        response = "I am doing well, thank you for asking."

    elif "your name" in user:
        response = "I am your dynamic voice assistant."

    elif "who created you" in user:
        response = "I was created by Rashmitha as part of an internship task."

    elif "what can you do" in user:
        response = "I can respond dynamically and manage voice flow naturally."

    elif "internship" in user:
        response = """Yes, I got this internship in UpToSkills Portal.
It is a wonderful platfrom to gain hands on experience. 
Improve your skills and can grow technically."""

    elif "time" in user:
        response = "Sorry, I cannot check live time yet."

    elif "thank you" in user:
        response = "You are welcome. Happy to help."

    elif "sing a song" in user:
        response = """Gimme, gimme, gimme some time to think
I'm in the bathroom looking at me
Face in the mirror is all I need 
Wait until the reaper takes my life
Never gonna get me out alive
I will live a thousand million lives 
My patience is waning, is this entertaining?
Our patience is waning, is this entertaining?
I got this feeling, yeah, you know
Where I'm losing all control
'Cause there's magic in my bones
I got this feeling in my soul
Go ahead and throw your stones
'Cause there's magic in my bones"""

    elif "tell me a story" in user:
        response = """Once there was a little bird.
It was afraid to fly high.
Every day it practiced with courage.
One day it opened its wings boldly.
And finally it touched the sky."""

    elif "quote" in user:
        response = """Believe in your dreams.
Stay patient through struggles.
Learn from every failure.
Keep moving forward daily.
Success will find you."""

    elif "motivate me" in user:
        response = """You are stronger than fear.
Every failure teaches success.
Keep learning and growing.
Your effort will shine soon.
Never stop believing."""

    elif "compliment me" in user:
        response = """You are creative and smart.
You solve problems beautifully.
Your dedication is inspiring.
You are capable of greatness.
Keep shining brightly."""

    elif "good morning" in user:
        response = "Good morning. Have a productive day."

    elif "good night" in user:
        response = "Good night. Sleep well."

    elif "tell me a joke" in user:
        response = "Why do programmers prefer dark mode? Because light attracts bugs."

    elif "bye" in user:
        response = "Goodbye, have a wonderful day."
        speak_dynamic(response)
        break

    else:
        response = f"You said {user}. I am processing your request."

    speak_dynamic(response)