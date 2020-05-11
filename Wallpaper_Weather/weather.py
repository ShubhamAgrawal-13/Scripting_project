from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os
import random
import time
import json

while True:
    # number=random.randint(1,4)
    # os.system("gsettings set org.gnome.desktop.background picture-uri /home/kittu/Desktop/wall_q2/"+x+"/%d"%number)
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=1fd25426b51779bb40a08907e4f55d1f&q=Hyderabad"

    url="https://openweathermap.org/find?q=hyderabad"

    response = requests.get(base_url) 
    x = response.json() 

    if x["cod"] == "404":
        print(" City Not Found ")
    else:
        y = x["main"]  
        z = x["weather"] 
        print(z)
        weather_description = z[0]["description"]  
        #print(str(weather_description)) 
        x1=str(weather_description)
        x=x1.lower()
    current_time=(int)((datetime.time(datetime.now())).hour)
    if((current_time >= 5)and(current_time < 12)):
        day="morning"
    elif((current_time >= 12)and(current_time < 4)):
        day="afternoon"
    elif((current_time > 4)and(current_time < 7)):
        day="evening"
    else:
        day="night"
    print(x)
    if((x=='overcast')or(x=='partly cloudy')or(x=='mostly cloudy')or(x=='cloudy')or(x=='fog')or(x,'smoke')or(x=='haze')or(x=='few clouds')):
        cli="overcast"
    elif((x=='sunny')or(x=='mostly sunny')or(x=='windy')or(x=='dusty')or(x=='partly sunny')):
        cli="sun"
    elif((x=='rain and snow')or(x=='freezing drizzle')or(x=='chance of snow')or(x=='hail')or(x=='flurries')or(x=='icy')or(x=='chance of storm')or(x=='light snow')or(x=='sleet')or(x=='snow showers')or(x=='snow')):
        cli="snow"    
    elif((x=='scattered thunderstorm')or(x=='scattered showers')or(x=='light rain')or(x=='showers')or(x=='thunderstorm')or(x=='chance of rain')or(x=='storm')or(x=='chance of tStorm')or(x=='mist')or(x=='rain')):   
        cli="rain"

    s="_"
    print(x)
    climate=s.join([cli,day])    
    print(climate)
    p=os.getcwd()
    print(p)
    filename="\'"+p+"/"+climate+"\'"
    print(filename)
    os.system("gsettings set org.gnome.desktop.background picture-uri "+filename)
    # print("wallpaper changed to%d"%number)
    time.sleep(100)

  


 
	 
