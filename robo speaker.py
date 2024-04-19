#robo speaker
import pyttsx3
robo=pyttsx3.init()
print("welcome to RoboSpeker 1.1")
while True:
        x=input("Enter what you pronounce")
        if x=="q":
            robo.say("goodbye")
            robo.runAndWait()
            break
        robo.say(x)
        robo.runAndWait()