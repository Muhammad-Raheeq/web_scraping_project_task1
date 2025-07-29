import requests
def fetchandsavetofile(url,path):
    r=requests.get(url)
    with open(path,"w",encoding='utf-8')as f:
        f.write(r.text)

url="https://www.africanews.com/search/news?themes=news%2Cbusiness%2Csport%2Cculture%2Cscience_technology"

fetchandsavetofile(url,"basic/file.html")