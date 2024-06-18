
import speech_recognition as sr 
import datetime
import time
import wikipedia 
import webbrowser
import pyautogui as py
import os
import random
import pyttsx3
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import os
from pyautogui import click
import random
import pyttsx3 
import cv2
from requests import get
import pywhatkit as kit
import sys
import pyjokes
import pynews
import requests
import instaloader
import PyPDF2
from bs4 import BeautifulSoup
import pywikihow
from pywikihow import search_wikihow
import psutil
import urllib.request
import numpy as np
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.distance import great_circle
import geocoder

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")

    speak(f"the current time is {strTime}")
    speak("hello sir , welcome back")
    speak("I am Jarvis. Please tell me how may I help you")

def YouTubeAuto(command):
    query = str(command)
    if 'pause' in query:
        press('space bar')
    elif 'resume' in query:
        press('space bar')
    elif 'full screen' in query:
        press('f')
    elif 'film screen' in query:
        press('t')
    elif 'skip' in query:
        press('l')
    elif 'back' in query:
        press('j')
    elif 'increase' in query:
        press_and_release('SHIFT + .')
    elif 'decrease' in query:
        press_and_release('SHIFT + ,')
    elif 'previous' in query:
        press_and_release('SHIFT + p')
    elif 'next' in query:
        press_and_release('SHIFT + n')
    elif 'search' in query:
        click(x=667, y=146)
        speak("What To Search Sir ?")
        search = takeCommand()
        write(search)
        sleep(0.8)
        press('enter')
    elif 'mute' in query:
        press('m')
    elif 'unmute' in query:
        press('m')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold=300
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
        query=query.lower() 
    return query
    
def news():
    main_url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=9a35ac49145f4f5eb4cac67130a6f166'
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def ChromeAuto(command):
    query = str(command)
    if 'new tab' in query:
        press_and_release('ctrl + t')
    elif 'close tab' in query:
        press_and_release('ctrl + w')
    elif 'new window' in query:
        press_and_release('ctrl + n')
    elif 'history' in query:
        press_and_release('ctrl + h')
    elif 'download' in query:
        press_and_release('ctrl + j')
    elif 'bookmark' in query:
        press_and_release('ctrl + d')
        press('enter')
    elif 'incognito' in query:
        press_and_release('Ctrl + Shift + n')
    elif 'switch tab' in query:
        tab = query.replace("switch tab ", "")
        Tab = tab.replace("to","")    
        num = Tab
        bb = f'ctrl + {num}'
        press_and_release(bb)
    elif 'open' in query:
        name = query.replace("open ","")
        NameA = str(name)
        if 'youtube' in NameA:
            webbrowser.open("https://www.youtube.com/")
        elif 'instagram' in NameA:
            webbrowser.open("https://www.instagram.com/")
        else:
            string = "https://www." + NameA + ".com"
            string_2 = string.replace(" ","")
            webbrowser.open(string_2)

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=942,y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value)

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('E:\\YouTube Channel\\YouTube - Jarvis\\How To Make Jarvis In Python\\DataBase\\YouTube\\')
    Download(Link)
    speak("Done Sir , I Have Downloaded The Video .")
    speak("You Can Go And Check It Out.")
    os.startfile('E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\DataBase\\YouTube\\')

def pdf_reader():
    speak("enter your pdf file name sir ")
    name=input("enter your file name here :")
    book=open(f'{name}.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    speak(f"total number of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg=int(input("please enter the page number :"))
    page=pdfReader._get_page(pg)
    text=page.extractText()
    speak(text)

def WindiowsAuto(command):
    query = str(command)
    if 'home screen' in query:
        press_and_release('windows + m')
    elif 'minimise' in query:
        press_and_release('windows + m')
    elif 'show start' in query:
        press('windows')
    elif 'open setting' in query:
        press_and_release('windows + i')

    elif 'open search' in query:

        press_and_release('windows + s')

    elif 'screen shot' in query:

        press_and_release('windows + SHIFT + s')

    elif 'restore windows' in  query:

        press_and_release('Windows + Shift + M')

    else:
        speak("Sorry , No Command Found!")

def notepad():
    speak("tell me what you want to write")
    speak("i am ready to write")
    writes=takeCommand()
    time=datetime.datetime.now().strftime("%H:%M")
    filename=str(time).replace(":","-") + "-note.txt"
    with open(filename,"w") as file:
        file.write(writes)
    path_1 = "C:\\Users\\sanya\\OneDrive\\Desktop\\AI Jarvis bot\\" + str(filename)
    path_2 = "C:\\Users\\sanya\\OneDrive\\Desktop\\AI Jarvis bot\\database\\notepad" + str(filename)

    os.rename(path_1,path_2)
    os.startfile(path_2)

def googlemap(place):
    url_place = "https://www.google.com/maps/place/" + str(place)

    # Fix typo in geocoder
    geolocator = Nominatim(user_agent="mygeocoder")

    try:
        location = geolocator.geocode(place, addressdetails=True)
        target_location = location.latitude, location.longitude
        location = location.raw["address"]
        target = {'city': location.get('city', ''),
                  'state': location.get('state', ''),
                  'country': location.get('country', '')}

        curr_location = geocoder.ip('me')
        curr_location = curr_location.latlng

        dis = str(great_circle(curr_location, target_location))
        dis = str(dis.split(' ', 1)[0])
        dis = round(float(dis), 2)

        webbrowser.open(url=url_place)
        speak(target)
        speak(f"sir, {place} is {dis} kilometers away from your location.")
    except (AttributeError, GeocoderTimedOut):
        speak("Sorry, I couldn't find the location.")
                  

def start():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open notepad' in query:
            notepath="C:\\Windows\\notepad.exe"
            os.startfile(notepath)

        elif 'open command' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('cam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'ip address' in query:
            ip = requests.get("https://ipinfo.io/ip").text.strip()
            speak(f"Your IP address is {ip}")


        elif 'thankyou' in query:
            speak("its my pleasure sir")
        elif 'hello' in query:
            speak("hello sir, i am glad to meet you sir")

        

        elif 'send whatsapp message' in query:
            speak("tell me the no of that person sir")
            num=int(input("Enter phone number here"))
            speak("What sould i send... ")
            mess=takeCommand()
            speak("on which time you will send in hours ")
            hour=int(input("please enter hour only example 1 to 22 :"))
            speak("on which munite")
            minu=int(input("please enter minutes only example 1 to 59 :"))

            kit.sendwhatmsg(f"+91{num}",mess,hour,minu)


        elif 'play song on youtube' in query:
            speak("which song to play on youtube sir...")
            song=takeCommand()
            kit.playonyt(f"{song}")

        elif 'on youtube' in query:
            speak('Searching on youtube...')
            query = query.replace("on youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}&sp=EgIQAQ%253D%253D")

        elif 'remember that' in query:
            remember=query.replace("remember that","")
            remember=remember.replace("jarvis","")
            speak("sir tell me to remind you that :"+remember)
            rem=open('data.txt','w')
            rem.write(remember)
            rem.close()

        elif "do you remember" in query:
            rem=open('data.txt','r')
            speak("sir you tell me that"+rem.read())

        

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'on google' in query:
            speak("please wait sir, i am search on google")
            cm=takeCommand()
            goo=cm.replace("on google","")
            webbrowser.open(f"{goo}")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open music learning couse' in query:
            webbrowser.open("learn.aaftonline.com")
            speak('here you go')

        elif 'window control' in query:
            speak("what i do ")
            query=takeCommand()
            WindiowsAuto(query)

        elif 'Chrome control' in query:
            speak("what i do ")
            query=takeCommand()
            ChromeAuto(query)

        elif 'youtube control' in query:
            speak("what i do ")
            query=takeCommand()
            YouTubeAuto(query)

            
        elif 'about developer' in query:
            speak('first PLease tell me password')
            try:
                if takeCommand()=='open file':
                    speak("sanyam is my developer")
                    speak("Father name is Mr ajay kumar ")
                    speak("Mother name is Mrs Rajni bala ")
                    speak("Brother name is Vyom singla ")
                    speak("Father age is 45 years ")
                    speak("Mother age is 43 years ")
                    speak("Sanyam doing twelveth class non medical")
                    speak("His mother is a hindi teacher in government school ")
                    speak("he is professionalist in coomputer ")
                else:
                    speak("Password incorrect Try after sometime")
                    speak("Thankyou for comming")
            except Exception as e:
                speak(" sorry sir")

        elif 'activate how to do mode' in query:
            speak("how to do mod is activated ")
            while True:
                speak("please tell me what you want to know")
                how=takeCommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak("okay sir how to do mod is closed")
                        break
                    else:
                        max_results=1
                        how_to =search_wikihow(how,max_results)
                        assert len(how_to)==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir i am not able to find this")
                

        elif 'play music' in query:
            music_dir = 'C:\\Users\\sanya\\Music'
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'close music' in query:
            speak("okay sir closing music")
            os.system("taskkill /f /im Music.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\sanya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'close code' in query:
            speak("okay sir closing code")
            os.system("taskkill /f /im Code.exe")

        elif 'power left' in query or 'battery' in query:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"sir your system have {percentage} percent battery")

        elif 'open python' in query:
            idlepath="C:\\Users\\mr\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
            os.startfile(idlepath)

        elif 'close python' in query:
            speak("okay sir closing python")
            os.system("taskkill /f /im python.exe")
            
        elif 'open gallery' in query or 'photo' in query:
            photopath="C:\\Users\\sanya\\OneDrive\\Pictures"
            os.startfile(photopath)
            
        elif 'show chrome history' in query:
            webbrowser.open("www.google.com")
            py.keyDown('ctrl')
            py.press("h")
            py.keyUp("ctrl")

        elif 'open map' in query:
            speak("which location search on google maps")
            query=takeCommand()

            googlemap(query)
##############################################
##############################################
        elif 'open excel' in query:
            speak("opening excel sheet")
            excelpath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007.lnk.lnk"
            os.startfile(excelpath)

        elif 'close excel' in query:
            speak("closing sheet")
            os.system("taskkill /f /im Microsoft Office Excel 2007.exe")
##############################################
##############################################
        
            
        elif 'show source code' in query:
            speak("i am not able to show my source code")
            speak("you have to licence to my developer")
            speak("then you can see my source code")
            
        elif 'learn coding' in query:
            speak("wait i will show you some result")
            time.sleep(5)
            webbrowser.open("https://www.youtube.com/results?search_query=learn+coding")
            speak("here you go")

            
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            time.sleep(10)
            speak("on which person you have to send message")
            number=takeCommand()
            py.typewrite(number)
            
        elif 'open telegram' in query:
            webbrowser.open("web.telegram.org")
            
        elif 'shut down the system' in query:
            speak("it is not safe for computer please do this manually")
            speak("if you want to shutdown say yes or no")
            power=takeCommand()
            try:
                if power=='yes':
                    os.system("shutdown /s /t 5")
                elif power=='no':
                    speak("alright i cannot do this")
            except Exception as e :
                speak("some error to do this")
        elif 'open free fire' in query:
            freefire="C:\\Users\\mr\\Desktop\\FreeFireMAX.lnk"
            os.startfile(freefire)
            
        
        elif 'close gallery' in query:
            speak("okay sir closing gallery")
            os.system("taskkill /f /im Pictures.exe")
        

        elif 'volume up' in query:
            py.press("volumeup")

        elif 'volume down' in query:
            py.press("volumedown")

        elif 'volume mute' in query:
            py.press("volumemute")
            
        elif 'open mobile camera' in query:
            URL="http://10.26.77.87:8080/shot.jpg"
            while True:
                img_arr=np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img=cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q=cv2.waitKey(1)
                if q==ord("q"):
                    break;
            cv2.destroyAllWindows()


        elif 'tell me a joke' in query:
            joke=pyjokes.get_joke()
            speak(joke)

        elif 'write on notepad' in query:
            notepad()

        elif 'hide all files' in query or 'hide the folder' in query or 'visible for everyone' in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition=takeCommand().lower()
            if 'hide' in condition:
                os.system("attrib +h /s /d")
                speak("sir all the file in this folder are now  hidden ")


            elif 'visible' in condition:
                os.system("attrib -h /s /d")
                speak("sir all the file in this folder are now visible for everyone i wish you are taking this decision on your own")

            elif 'leave' in condition:
                speak("ok sir")
             

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        elif 'download' in query:
            DownloadYouTube()

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,SetsuspendState 0,1,0")


        elif 'switch the window' in query or 'change window' in query:
            py.keyDown("alt")
            py.press("tab")
            time.sleep(1)
            py.keyUp("alt")

        elif 'tell me the news' in query or 'news' in query:
            speak("please wait sir, searching the latest news")
            news()

        elif 'how are you' in query:
            speak("i am fime sir , and you")

        elif 'fine' in query:
            speak("ohh good sir ")
#############################################
#############################################
        elif 'open chrome' in query:
            speak("okay sir opening chrome")
            chromepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'close chrome' in query:
            speak("closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif 'close google' in query:
            speak("closing google")
            os.system("taskkill /f /im google.exe")

        elif 'close telegram' in query:
            speak("closing telegram")
            os.system("taskkill /f /im telegram.exe")
#############################################
#############################################
        elif 'open word' in query:
            speak("please wait i am opening the word")
            wordpath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\msword.exe"
            os.startfile(wordpath)

        elif 'close word' in query:
            speak("okay sir closing word")
            os.system("taskkill /f /im msword.exe")


        elif 'open recycle bin' in query:
            paintpath="SRecycle.Bin.dll"
            os.system(paintpath)

        elif 'close youtube' in query:
            os.system("taskkill /f /im chrome.exe")
        
        elif 'close paint' in query:
            speak("okay sir closing paint")
            os.system("taskkill /f /im mspaint.exe")

        elif 'open store' in query:
            os.system("start Microsoft Store")

        elif 'close store' in query:
            speak("okay sir closing microsoft store")
            os.system("taskkill /f /im Microsoft Store")

        elif 'tell me your name' in query:
            speak("i am jarvis sir how may i help you")

        elif 'play movie on youtube' in query:
            speak("which type of movies you want to play on youtube sir...")
            movie=takeCommand()
            kit.playonyt(f"{movie}")

        elif 'where i am' in query or 'where we are' in query:
            speak("wait sir let me check")
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.geojs.io/vl/ip/geo/'+ipAdd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                country=geo_data['country']
                speak(f"sir i am not sure ,but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir due to some network issue i am not able to find where we are")
                pass

        elif 'temperature' in query:
            speak("which city do you have to check wheather like kurukshetra")
            area=takeCommand()
            search=f"weather in {area}"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        

        elif 'instagram profile' in query or 'profile on instagram' in query:
            speak("Sir, please enter the username correctly.")
            name = input("Enter the username here: ")
            webbrowser.open(f"https://www.instagram.com/{name}")
            speak(f"Sir, here is the profile of the user {name}.")
            time.sleep(10)

            insta_loader = instaloader.Instaloader()
            insta_loader.download_profile(name, profile_pic_only=True)
            speak("I am done, sir. The profile picture is saved in your main folder.")

        elif 'read pdf' in query:
            pdf_reader()
        
        elif 'take a screenshot' in query or 'take screenshot' in query:
            speak("sir, please tell me the name of this screenshot file")
            name=takeCommand().lower()
            speak("sir please hold the screen for few seconds i am taking screenshot")
            time.sleep(2)
            img=py.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in your main folder")



        elif 'open setting' in query:
            os.system("start Settings")         

        elif 'you can sleep now' in query:
            speak("okay sir,i am going to sleep you can call me anytime... ")
            break
        speak("sir , do you have any other work")

if __name__ == "__main__":
    while True:
        permission=takeCommand()
        if 'wake up' in permission:
            start()
        elif 'goodbye ' in permission or 'exit' in permission:
            speak("thanks for using me sir have a good day")
            break
            
        
