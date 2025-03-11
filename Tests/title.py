
r = requests.get("")
soup = BeautifulSoup(r.text)

link = soup.find_all(name="title")[0]
title = str(link)
title = title.replace("<title>","")
title = title.replace("</title>","")

print(title)