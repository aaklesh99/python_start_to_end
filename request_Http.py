import requests
# p = requests.get("https://diceus.com/blog/")
# print(p)

url = "www.Akki.com"
data = {
    "p1": "9",
    "p2": "Akki"
}
r = requests.post(url=url, data=data)
print(r)