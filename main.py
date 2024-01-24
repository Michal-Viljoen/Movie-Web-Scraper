import requests
from bs4 import BeautifulSoup

f = open("movies.txt", "a",encoding="utf-8")
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 
response=requests.get(URL).text

soup=BeautifulSoup(response, "html.parser")
result=soup.find_all(name="h3",class_="title")
for movie in result:
    
    final=movie.getText()
    finals=final.encode("utf-8").decode('ascii','ignore')
    
    f.write(f"{finals} \n")


f.close()