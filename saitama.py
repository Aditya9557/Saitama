import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import turtle  
import random  
import time

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("HEY, I am Saitama BOOS. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def draw_heart():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("red")
    t.begin_fill()
    t.fillcolor("red")
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()
    t.penup()
    t.goto(0, -50)
    t.write("I Love You", align="center", font=("Arial", 24, "normal"))
    t.hideturtle()
    turtle.done()


def draw_spiral():
    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for i in range(100):
        t.color(random.choice(colors))
        t.forward(i * 2)
        t.left(91)
    t.hideturtle()
    turtle.done()


def draw_starry_sky():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    for _ in range(50):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.goto(x, y)
        t.color(random.choice(["yellow", "white", "gold"]))
        t.begin_fill()
        t.circle(random.randint(1, 3))
        t.end_fill()
    t.hideturtle()
    turtle.done()

def draw_fractal_tree():
    def tree(branch_len, t):
        if branch_len > 5:
            t.forward(branch_len)
            t.right(20)
            tree(branch_len - 15, t)
            t.left(40)
            tree(branch_len - 15, t)
            t.right(20)
            t.backward(branch_len)

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    t.color("brown")
    tree(75, t)
    t.hideturtle()
    turtle.done()


def draw_rainbow():
    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    t.pensize(3)
    for i in range(360):
        t.pencolor(colors[i % 7])
        t.width(i // 100 + 1)
        t.forward(i)
        t.left(59)
    t.hideturtle()
    turtle.done()


def draw_crazy_pattern():
    t = turtle.Turtle()
    t.speed(0)
    for _ in range(100):
        t.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
        t.forward(random.randint(50, 200))
        t.left(random.randint(0, 360))
    t.hideturtle()
    turtle.done()
def draw_clock():

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=600, height=600)
    screen.title("Graphical Clock")
    screen.tracer(0) 
    clock_turtle = turtle.Turtle()
    clock_turtle.hideturtle()
    clock_turtle.speed(0)
    clock_turtle.pensize(3)

    def draw_clock_face():
       
        clock_turtle.penup()
        clock_turtle.goto(0, -200)
        clock_turtle.setheading(0)
        clock_turtle.pendown()
        clock_turtle.circle(200)

     
        for hour in range(12):
            clock_turtle.penup()
            clock_turtle.goto(0, 0)
            clock_turtle.setheading(90 - (hour * 30))
            clock_turtle.forward(180)
            clock_turtle.pendown()
            clock_turtle.forward(20)
            clock_turtle.penup()
            clock_turtle.forward(10)
            clock_turtle.write(str(hour + 1), align="center", font=("Arial", 12, "normal"))

    def draw_clock_hands():
     
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

    
        clock_turtle.penup()
        clock_turtle.goto(0, 0)
        clock_turtle.setheading(90 - (hour * 30 + minute * 0.5))
        clock_turtle.pendown()
        clock_turtle.forward(100)

      
        clock_turtle.penup()
        clock_turtle.goto(0, 0)
        clock_turtle.setheading(90 - (minute * 6))
        clock_turtle.pendown()
        clock_turtle.forward(150)

   
        clock_turtle.penup()
        clock_turtle.goto(0, 0)
        clock_turtle.setheading(90 - (second * 6))
        clock_turtle.pendown()
        clock_turtle.forward(180)

    def update_clock():
       
        clock_turtle.clear()

      
        draw_clock_face()
        draw_clock_hands()

       
        screen.update()

        screen.ontimer(update_clock, 1000)


    update_clock()


    turtle.done()
if __name__ == "__main__":
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
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'email to aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adityachaubeychess@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Aditya bhai. I am not able to send this email")
        elif 'shutdown' in query:
            speak("Shutting down Saitama BOOS. Goodbye Sir!")
            break
        elif 'meri' in query:  
            speak("Drawing a heart for Himanshi!")
            draw_heart()
        elif 'spiral' in query:  
            speak("Drawing a colorful spiral!")
            draw_spiral()
        elif 'stars' in query:  
            speak("Drawing a starry sky!")
            draw_starry_sky()
        elif 'tree' in query:  
            speak("Drawing a fractal tree!")
            draw_fractal_tree()
        elif 'rainbow' in query:  
            speak("Drawing a rainbow!")
            draw_rainbow()
        elif 'crazy' in query:  
            speak("Drawing a crazy pattern!")
            draw_crazy_pattern()
        elif 'clock' in query:  
            speak("Displaying a graphical clock!")
            draw_clock()