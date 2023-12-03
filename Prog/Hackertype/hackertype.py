import requests

url = "https://hacker-typer.tuctf.com/"
s = requests.Session() # Initiate the session

for i in range(151):
    mot = str(s.get(url).text).split('<strong name="word-title">')[1].split("</strong>")[0] # Get the word
    page = s.post(url + 'check_word', data={'word' : mot}).text
    print(page)
