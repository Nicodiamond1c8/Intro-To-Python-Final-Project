# import requests and json modules
import requests, json

# define variables
api_key = "5156cbb83d3a3183bf7fb3ea08ac85f7"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

while True:

	# Take user input for city
	location = input("Enter 'quit' to exit the program. \nEnter City name or ZIP Code: ")
	#allow for user to input multiple locations or quit
	if location == "quit":
		break

	# complete url address
	complete_url = base_url + "appid=" + api_key + "&q=" + location + ",US&units=imperial"

	#Test Connection and print any errors
	try:
		r = requests.get(complete_url)
		r.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print (err)
	else:
		print ("Connection Successful")

	# return response of URL
	response = requests.get(complete_url)

	# convert json format data
	data = response.json()

	# Data contains list of nested dictionaries
	# Check value of "cod" 404 means web page not found
	if data["cod"] != "404":

		city = data["name"]

		# initialize weather variable
		weather = data["main"]

		# store the value "temp"
		current_temperature = weather["temp"]

		# store the value of "feels_like"
		feels_like = weather["feels_like"]

		# store the value of "humidity"
		current_humidity = weather["humidity"]

		# store the value of "temp_min"
		temp_min = weather["temp_min"]

		# store the value of "temp_max"
		temp_max = weather["temp_max"]

		# store the value of "weather"
		weather = data["weather"]

		# store the value of "description"
		weather_description = weather[0]["description"]

		# print JSON values in readable format
		print("The Location you entered is = " +
						str(city) +
			"\nThe Current Weather is = " +
						str(weather_description) +
			"\nThe Temperature in Fahrenheit is = " +
						str(current_temperature) +
			"\nThe Temperature in Fahrenheit Feels Like = " +
						str(feels_like) +
			"\nThe Humidity Percentage is = " +
						str(current_humidity) +
			"\nThe Low Temperature Today in Fahrenheit is = " +
						str(temp_min) +
			"\nThe High Temperature Today in Fahrenheit is = " +
						str(temp_max) +
						"\n\n")


	else:
		print("City Not Found \n\n")
