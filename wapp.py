import requests
# This is my api key
api_key="f13751912e916ba48399de96f5dddf6c"
# Ask the user input
user=input("enter the city name: ")
#import the data from weather api
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user}&appid={api_key}")
# we check that user chose a valid city
if weather_data.json()['cod']=="404":
    print("Select a valid city")
#print(weather_data.json())   
else:
    T=(weather_data.json()["main"]["temp"])
    #convert calvin to celcious
    print("The temperature of",user,"is","{:6.2f}".format(T-273.15),str(u'\N{DEGREE SIGN}')+"C"+"  🌡️")
#checking for repeting time
while True :
    # this is my api key
    api_key="f13751912e916ba48399de96f5dddf6c"
    # Ask the user you want to check other city temperature
    print("Do you want to check the temperature of another city? please type : yes")
    print("Don't you want to check the temperature of another city? please type : no")
    # Ask the user input
    user1=input()
    # Check input
    if user1=="yes" or user1=="YES" or user1=="Yes":
        user=input("enter the city name: ")
        #import the data from weather api
        weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user}&appid={api_key}")
        # we check that user chose a valid city
        if weather_data.json()['cod']=="404":
            print("Select a valid city")
        
        else:
            T=(weather_data.json()["main"]["temp"])
            print("The temperature of",user,"is","{:6.2f}".format(T-273.15),str(u'\N{DEGREE SIGN}')+"C"+"  🌡️") 
    # If user chose something else instead "Yes" then the code exit        
    else:
        print("Thankyou fore giving us a chance to serve you")      
        break