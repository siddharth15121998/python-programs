import json
import  requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
ExtractedData=data.json()       #json parsing
#print(ExtractedData)
articles=ExtractedData["articles"]
vowel="aeiou"
# print(len(articles))
for i in articles:
    title=i["title"]

    
    
    count={}.fromkeys(vowel,0)
    #print(count)
    print(title)

    for x in title.lower():
        if x in  count:
            count[x]=count[x]+1
    print(count)
     



    
    
