import requests
import smtplib

EMAIL_ID = input("Please enter your email: ")
key = "d9e9ccd7c29d24c16e7e82a6e1f56fb5"
weather_params = {
    "lat" : "38.846226",
    "lon": "-77.306374",
    "appid": key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()


weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    


    




if will_rain == True:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user="simbathelion987@gmail.com", password="jwybkqgnliqpdxbe")
        connection.sendmail(from_addr="simbathelion987@gmail.com", to_addrs=EMAIL_ID,msg="Bring your umbrella")





          




