#Script for downloading multifiles 
# importing the requests library
import requests

# Multiple URLs creates dictonary key value pairs
multiple_urls = {
    "python_logo.png": "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    "python.html": "https://www.python.org/"
}
#for loop  that iterates over the key value pairs in the multipart_urls dictonary
for file_name, url in multiple_urls.items():
    #uses the get function to send HTTP GET requests to the URL
    response = requests.get(url)
    with open(file_name, "wb") as file:
        file.write(response.content)

        