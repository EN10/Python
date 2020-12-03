import requests
res = requests.get('https://www.marketbeat.com/stocks/NYSE/IBM/')
start = res.text.find("<strong>")
end = res.text.find("</strong>")
print(res.text[start+8:end])
