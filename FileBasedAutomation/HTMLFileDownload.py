#File types contain header,data,EOF

import requests

#Download webpage to modify
web_page = "https://en.wikipedia.org/wiki/Python_(programming_language)"

#Http response object
#Send http request to the server and save

response  = requests.get(web_page)


#wb mode for writing contents binary to the file
with open("python.html","wb") as file:
    #Saving recived content
    file.write(response.content)