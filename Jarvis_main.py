import datetime
from email import message
import webbrowser
from numpy import tile
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

#from INTRO import play_gif
#play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        speak("Say that again")
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                
                

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("D:\\Coding\\Youtube\\Jarvis\\FocusMode.py")
                        exit()

                    
                    else:
                        pass

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

                


                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")                       
                     
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                    

                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )
                
                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                
                

                ############################################################
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=E3jOYQGu1uw&t=1246s&ab_channel=scientificoder")
                    

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                
                elif 'open facebook' in query:
                    webbrowser.open("facebook.com")

                elif 'open twitter' in query:
                    webbrowser.open("twitter.com") 

                elif 'open whatsapp' in query:
                    webbrowser.open("whatsapp.com")      

                elif 'open instagram' in query:
                    webbrowser.open("instagram.com")

                elif 'open wikipedia' in query:
                    webbrowser.open("wikipedia.com")

                elif 'open google map' in query:
                    webbrowser.open("google.com/maps")

                elif 'open car dekho' in query:
                    webbrowser.open("www.cardekho.com")

                elif 'open cars 24' in query:
                    webbrowser.open("www.cars24.com")

                elif 'open dude perfect' in query:
                    webbrowser.open("dudeperfect.com")

                elif 'open etv' in query:
                    webbrowser.open("www.etv.co.in")

                elif 'open amazon' in query:
                    webbrowser.open("www.amazon.in")        
 
                elif 'open zoom' in query:
                    webbrowser.open("zoom.us")
                elif 'open flipkart' in query:
                    webbrowser.open("flipkart.com")
                
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "temperature" in query:
                    search = "temperature in hyderabad"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in hyderabad"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                           
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "go handsfree" in query:
                    speak("Ok sir")
                    print("Ok sir")
                    cap = cv2.VideoCapture(0)
                    hand_detector = mp.solutions.hands.Hands()
                    drawing_utils = mp.solutions.drawing_utils
                    screen_width, screen_height = pyautogui.size()
                    index_y = 0
                    while True:
                        _, frame = cap.read()
                        frame = cv2.flip(frame, 1)
                        frame_height, frame_width, _ = frame.shape
                        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        output = hand_detector.process(rgb_frame)
                        hands = output.multi_hand_landmarks
                        if hands:
                            for hand in hands:
                                drawing_utils.draw_landmarks(frame, hand)
                                landmarks = hand.landmark
                                for id, landmark in enumerate(landmarks):
                                    x = int(landmark.x*frame_width)
                                    y = int(landmark.y*frame_height)
                                    if id == 8:
                                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                                        index_x = screen_width/frame_width*x
                                        index_y = screen_height/frame_height*y

                                    if id == 4:
                                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                                        thumb_x = screen_width/frame_width*x
                                        thumb_y = screen_height/frame_height*y
                                        print('outside', abs(index_y - thumb_y))
                                        if abs(index_y - thumb_y) < 20:
                                            pyautogui.click()
                                            pyautogui.sleep(1)
                                        elif abs(index_y - thumb_y) < 100:
                                            pyautogui.moveTo(index_x, index_y)
                        cv2.imshow('Virtual Mouse', frame)
                        cv2.waitKey(1)

                elif "send email" in query:
                    speak("sending email")
                    html = '''
                        <html>
                            <body>
                                <h1>Here is your Report</h1>
                                <p>Hello, welcome to your report!</p>
                                
                            </body>
                        </html>
                        '''
                    def attach_file_to_email(email_message, filename, extra_headers=None):
                        with open(filename, "rb") as f:
                            file_attachment = MIMEApplication(f.read())  
                        file_attachment.add_header(
                            "Content-Disposition",
                            f"attachment; filename= {filename}",
                        )
                        if extra_headers is not None:
                            for name, value in extra_headers.items():
                                file_attachment.add_header(name, value)
                        email_message.attach(file_attachment)
                    email_from = 'shaiksaheer.ahmed2020@vitstudent.ac.in'
                    password = 'jninxoynkfspwbge'
                    email_to = 'shaiksaheer.ahmed2020@vitstudent.ac.in'
                    date_str = pd.Timestamp.today().strftime('%Y-%M-%D')
                    email_message = MIMEMultipart()
                    email_message['From'] = email_from
                    email_message['To'] = email_to
                    email_message['Subject'] = f'Report email - {date_str}'
                    email_message.attach(MIMEText(html, "html"))
                    attach_file_to_email(email_message, "C:\\Users\\SHAIK SAHEER AHMED\\Desktop\\jarvis\\zira.py")
                    attach_file_to_email(email_message, "C:\\Users\\SHAIK SAHEER AHMED\\Downloads\\Resume-Saheer-Ahmed-Shaik.pdf")
                    email_string = email_message.as_string()
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(email_from, password)
                        server.sendmail(email_from, email_to, email_string) 

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break


                




                


 