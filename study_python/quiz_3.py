url = "http://naver.com"

url = url.replace("http://", "")
url = url[:url.index(".")]   
countUrl = len(url)
findE = url.count("e")
url = url[:3]
print(f"{url}{countUrl}{findE}!")