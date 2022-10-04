import requests                           # Import the requests module

r = requests.get("https://api.ipify.org").text # Make the request to get ur IP from api.ipify.org
print("Your IP is: " + str(r)) # Print the result

# Credits to TMS ;)
