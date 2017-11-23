import requests

files = {'uploadFile': open('../files/Python-1ogo.png', 'rb')}
r = requests.post('http://pythonscraping.com/pages/processing2.php',
                  files=files)
print(r.text)
