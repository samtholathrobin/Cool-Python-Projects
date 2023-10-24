import requests

base_url = "https://www.1mg.com/drugs-all-medicines"
labels = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

page = 1
start_char = '"itemListElement"'
stop_char = '</script>'

for i in labels:

    r = requests.get(f'{base_url}?page={page}&label={i}')
    start = r.text.find(start_char)+19

    f = open(f"medicines-{i}.txt",'w',encoding="utf-8")

    while r.text[start]!=']' and page<=334:
        stop = r.text[start:].find(stop_char)+start-1

        l = r.text[start:stop].split(',')
        
        for j in range(len(l)):
            if l[j].startswith('"name"'):
                f.write(l[j]+", ")
            elif l[j].startswith('"url"'):
                f.write(l[j]+", ")
            elif l[j].startswith('"image"'):
                f.write(l[j]+','+l[j+1]+','+l[j+2]+','+l[j+3]+','+l[j+4]+','+l[j+5][:len(l[j+5])-1]+"\n")
        
        r = requests.get(f"{base_url}?page={page}&label={i}")
        start = r.text.find(start_char)+19
        print(i,page)
        page+=1

    f.close()
    page=1


