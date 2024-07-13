
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import os 
import pyautogui
import webbrowser
from datetime import datetime
from datetime import date
import locale
import pywhatkit
from time import sleep
import wikipedia
from googletrans import Translator
import pyjokes 
import requests
class Alexa:
    __recognizer = sr.Recognizer()
    wikipedia.set_lang("ar")
    translator = Translator()
    # Set the locale to Arabic (Egypt)
    locale.setlocale(locale.LC_ALL, 'ar_EG.UTF-8')
    def __Open_Terminal(self):
        self.Speak("حاضر يا كبير")
        pyautogui.hotkey("ctrl","alt","t")
        
    def __Open_GitHub(self):
        self.Speak("حاضر يا كبير")
        webbrowser.open_new_tab("https://github.com/")

    def __Open_MyYoutubeChannel(self):
        self.Speak("حاضر يا كبير")
        webbrowser.open_new_tab("https://www.youtube.com/@MohamedOsama-hw9hg")

    def __Open_ChatGpt(self):
        self.Speak("حاضر يا كبير")
        webbrowser.open_new_tab("https://poe.com/")

    def __Time_now(self):
        # Get the current time
        current_time = datetime.now().time()
        # Format the time as an Arabic string
        arabic_time = current_time.strftime('%I:%M:%S %p').replace('ص', 'صباحاً').replace('م', 'مساءً')
        Alexa.Speak(arabic_time)        

    def __Date_Today(self):
        # Get the current date
        today = datetime.now()
        # Format the date as an Arabic string
        arabic_date = today.strftime('%d %B %Y')        
        Alexa.Speak(arabic_date) 

    def __Whoami(self):
        Alexa.Speak("انت محمد أسامه كبير ال Embedded")   

    def __Send_to_whatsapp(self):
          Alexa.Speak("تمام قول النمره لو سمحت")
          number=""
          while not number.isnumeric():
            number = self.Recognize_Speech()
            number=number.replace(" ","")
            if(number.isnumeric()):
                break
            else:
                Alexa.Speak("مفهمتش قول تاني")
          if(number[0]!='0'):
              number = '0'+number
          Alexa.Speak("تمام قول المسدج لو سمحت")
          msg = self.Recognize_Speech()
          pywhatkit.sendwhatmsg_instantly("+2"+number,msg)
          while True:    
            try:
                pyautogui.locateOnScreen('mywhatsapp.png')
            except:
                print('image not found')
            else:
                print("image found")
                break    
          sleep(1)
          pyautogui.click(839,568)
          pyautogui.press('enter')
          
    def __Open_youtube_video(self,text):
        pywhatkit.playonyt(text)
        sleep(6)
        pyautogui.click(300,300)
        pyautogui.press('enter')     

    def __GiveMe_wikipedia_Summary(self,text):
        text= " ".join(text.split()[2:])
        wiki_text = wikipedia.summary(text, sentences = 1)
        self.Speak(wiki_text) 

    def __Tell_Me_Joke(self):
        My_joke = pyjokes.get_joke(language="en", category="neutral") 
        My_joke_ar= self.translator.translate(My_joke,dest='ar').text
        print(My_joke)
        self.Speak(My_joke_ar)

    def __Search_In_Google(self,text):
        self.Speak("حاضر يا كبير")
        text= " ".join(text.split()[3:])
        pywhatkit.search(text)

    def __Bye_Alexa(self):
        Alexa.Speak("سلام يا محمد")  
        exit()

    def __AlexaTranslator(self):
        self.Speak(" اختر اللغة التى ستترجم منهايمكنك الإخيار بين العربية او الإنجليزية")
        while True:
            text = self.Recognize_Speech()            
            if(text == "العربيه"):
                self.Speak("اتفضل اتكلم و انا هترجم للإنجليزية")
                arabic_sentence = self.Recognize_Speech()
                translated_sentence = self.translator.translate(arabic_sentence,dest="en").text
                self.Speak(translated_sentence)
                break
            elif(text == "الانجليزيه"):
                self.Speak("اتفضل اتكلم و انا هترجم للعربية")
                English_sentence = self.Recognize_Speech("en")
                translated_sentence = self.translator.translate(English_sentence,dest="ar").text
                self.Speak(translated_sentence)
                break
            else:
                Alexa.Speak(" مفهمتش قول تاني") 

    def __TakeScreenShot(self):
        self.Speak("حاضر يا كبير")
        pyautogui.hotkey("shift","prtscr")

    def __Commit_on_Github_Repo(self):
        self.Speak("حاضر يا كبير")
        os.system("cd && cd Embedded_Linux/Tasks/ && git add . && git commit -m \"Alexa Auto Comment\" && git push origin main ")
        webbrowser.open_new_tab("https://github.com/mohammedd2510/Python-Tasks/commits/main/")

    def __DollarPriceinEGP(self):
        currency_Api_key="235fd4efba806bae608a35d794d42e7a" 
        data = requests.get('http://data.fixer.io/api/latest?access_key='+currency_Api_key).json()
        DollarInEGP=round(data["rates"]["EGP"]/data["rates"]["USD"],2)
        self.Speak(f"الدولار دلوقتي عامل {DollarInEGP} جنيها")

    def __WeatherNow(self):
        city_name = "Cairo"
        # API endpoint and request parameters
        api_key = "fae4e4336c31fe86cbbcc17161fec8e5"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        Weather = response.json()
        Weather_Description_En =Weather["weather"][0]["description"]
        Weather_Description_ar =self.translator.translate(Weather_Description_En,dest="ar").text
        Temperature= Weather["main"]["temp"]
        Humidity=Weather["main"]["humidity"]
        self.Speak(f"حالة الطقس الأن {Weather_Description_ar}, و تبلغ درجة الحرارة الأن {Temperature} درجة , ايضا تبلغ درجة الرطوبة {Humidity} في المئة")

    def __CreateNewFile(self):
        self.Speak("تمام قول اسم الفايل بال English  لو سمحت")
        while True:
            file_name = self.Recognize_Speech("en")
            if (file_name == '0'):
                pass
            else : break
            Alexa.Speak("مفهمتش قول تاني")
        os.system(f"touch \"{file_name}\" ")
        Alexa.Speak("تمام عملت الفايل يا كبير")

    def __WriteFile(self):
        self.Speak("تمام قول اسم الفايل بال English  لو سمحت")
        while True:
            file_name = self.Recognize_Speech("en")
            if (file_name=='0'):
                pass
            else : break
            Alexa.Speak("مفهمتش قول تاني")
        self.Speak("اختر اللغة االلى هكتب بيها يمكنك الإختيار بين العربية او الإنجليزية")   
        while True:
            text = self.Recognize_Speech()   
            text_in_en = 0
            text_in_ar =0           
            if(text == "الانجليزيه"):
                self.Speak("اتفضل اتكلم و اناهكتب بللإنجليزية")
                with open(file_name,"w") as file:
                    while (True):
                        text_in_en = self.Recognize_Speech("en")
                        if(text_in_en):break 
                        else: self.Speak("مفهمتش قول تاني")
                    file.write(text_in_en)
                self.Speak("تمام كتبت اللي قولته يا كبير")           
                break
            elif(text == "العربيه"):
                self.Speak("اتفضل اتكلم و اناهكتب للعربية")
                with open(file_name,"w") as file:
                    while (True):
                        text_in_ar = self.Recognize_Speech()
                        if(text_in_ar):break 
                        else: self.Speak("مفهمتش قول تاني")
                    file.write(text_in_ar)
                self.Speak("تمام كتبت اللي قولته يا كبير")           
                break
            else:
                self.Speak(" مفهمتش قول تاني") 

    def __ReadFile(self):
        self.Speak("تمام قول اسم الفايل بال English  لو سمحت")
        while True:
            file_name = self.Recognize_Speech("en")
            if (file_name=='0'):
                pass
            else : break
            Alexa.Speak("مفهمتش قول تاني")
        Alexa.Speak("تمام هقرأ اللي مكتوب في الفايل دلوقتي")
        with open(file_name,"r") as file:
            file_text = file.read()
            Alexa.Speak(file_text)

    def __AdhanTiming(self,text):
        api_endpoint = "https://api.aladhan.com/v1/timings"
        latitude = 30.14656  # Your latitude
        longitude = 31.39326  # Your long
        today = date.today().strftime("%Y-%m-%d")
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "date": today,
        }
        response = requests.get(api_endpoint, params=params)
        data = response.json()
        if(self.__search_words_in_string(["الشروق"],text)):
            shrouq = data["data"]["timings"]["Sunrise"]
            self.Speak(f"موعد الشروق الساعة {shrouq} صباحا")
        elif (self.__search_words_in_string(["الظهر"],text)):
            Alduhr = data["data"]["timings"]["Dhuhr"]
            self.Speak(f"موعد صلاة الظهر الساعة {Alduhr}")
        elif (self.__search_words_in_string(["العصر"],text)):
            Alasr = data["data"]["timings"]["Asr"]
            self.Speak(f"موعد صلاة العصر الساعة {Alasr}")
        elif (self.__search_words_in_string(["المغرب"],text)):
            maghrib = data["data"]["timings"]["Maghrib"]
            self.Speak(f"موعد صلاة المغرب الساعة {maghrib}")
        elif (self.__search_words_in_string(["العشاء"],text)):
            Isha = data["data"]["timings"]["Isha"]
            self.Speak(f"موعد صلاة العشاء الساعة {Isha}")
        elif (self.__search_words_in_string(["الفجر"],text)):
            Fajr = data["data"]["timings"]["Fajr"]
            self.Speak(f"موعد صلاة الفجر الساعة {Fajr} صباحا")
        else:
            Alexa.Speak(" مفهمتش قول تاني")   

    def __DownloadLastLecture(self):
        self.Speak("حاضر يا كبير")
        os.system("EL_Down")

    def Recognize_Speech(self,lang="ar-EG"):
        with sr.Microphone() as source:
            print("Talk")
            self.__recognizer.adjust_for_ambient_noise(source)
            audio_text = self.__recognizer.listen(source)
            print("Time over, thanks")
            try:
                # using google speech recognition
                mytext= self.__recognizer.recognize_google(audio_text, language=lang)
                print(mytext)
            except:
                print("Sorry, I did not get that")
                mytext = '0'            
        return mytext
    
    def Speak(self,text):
        myobj = gTTS(text=text, lang="ar", slow=False)
        # Saving the converted audio in a mp3 file named
        # welcome 
        myobj.save("audio.mp3")
        # for playing note.mp3 file
        playsound('audio.mp3')
        os.remove("audio.mp3")
    def __search_words_in_string(self,words_list,str):
        text_found  = [word for word in words_list if word in str]
        return (len(text_found)!=0)
    
    def Respond_to_Speech(self,text):
        if (self.__search_words_in_string(["جديده","ترمنال","ترمينال"],text)):
            self.__Open_Terminal()
        elif(self.__search_words_in_string(["هاب","هب","git","hub","جيت"],text)):
            self.__Open_GitHub()
        elif(self.__search_words_in_string(["يوتيوب","قناتي","youtube","تيوب"],text)):
            self.__Open_MyYoutubeChannel()    
        elif(self.__search_words_in_string(["شات","جي بي تي"],text)):
            self.__Open_ChatGpt()       
        elif (self.__search_words_in_string(["الساعه"],text)):
            self.__Time_now()        
        elif (self.__search_words_in_string(["انهارده يوم","النهارده يوم","انهاردا يوم"," النهاردا يوم","تاريخ","يوم"],text)):
            self.__Date_Today()   
        elif (self.__search_words_in_string(["صباح","الخير"],text)):
            Alexa.Speak("صباح الخير يا كبير") 
        elif (self.__search_words_in_string(["اسمي"],text)):
            self.__Whoami()
        elif (self.__search_words_in_string(["باي يا"],text)):
            self.__Bye_Alexa()
        elif (self.__search_words_in_string(["اغنيه","شغلي"],text)):
            self.__Open_youtube_video(text)
        elif (self.__search_words_in_string(["الواتساب","الوتساب"," مسج","مسدج"],text)):
            self.__Send_to_whatsapp()
        elif(self.__search_words_in_string(["جوجل","سيرش"],text)):
            self.__Search_In_Google(text)
        elif(self.__search_words_in_string(["كلميني"],text)):
            self.__GiveMe_wikipedia_Summary(text)
        elif(self.__search_words_in_string(["نكته"],text)):
            self.__Tell_Me_Joke()

        elif(self.__search_words_in_string(["تترجملي","اترجم"],text)):
            self.__AlexaTranslator()

        elif(self.__search_words_in_string(["سكرين","شوت","خدي"],text)):
            self.__TakeScreenShot()
                    
        elif(self.__search_words_in_string(["كوميت","كومنت","ريبو"],text)):
            self.__Commit_on_Github_Repo()

        elif (self.__search_words_in_string(["دولار","سعر"],text)):
              self.__DollarPriceinEGP()

        elif (self.__search_words_in_string(["الطقس","الجو","الحراره"],text)):
              self.__WeatherNow()

        elif (self.__search_words_in_string(["فايل جديد"],text)):
               self.__CreateNewFile()

        elif (self.__search_words_in_string(["اكتب"],text)):
               self.__WriteFile()
        elif (self.__search_words_in_string(["اقرا"],text)):
               self.__ReadFile()    

        elif(self.__search_words_in_string(["اذان","صلاه","الشروق"],text)):
                self.__AdhanTiming(text)

        elif(self.__search_words_in_string(["تحملي","محاضره"],text)):
                self.__DownloadLastLecture()

        else:
            Alexa.Speak(" مفهمتش قول تاني")    
       



Alexa = Alexa()


