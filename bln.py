import requests
#شحن واحدات كرات الكبير
num=input("Enter Your Number: ")
print()
pas=input("Enter Your password:")
print("*"*40)
card=input("Enter Your card==>\n")
url="https://services.orange.eg/GetToken.svc/GenerateToken"

header={
"net-msg-id": "038ed645020304d16929078427951007",

"x-microservice-name":"APMS",

"Content-Type":"application/json; charset=UTF-8",
"Content-Length":"78",

"Host": "services.orange.eg",

"Connection":"Keep-Alive"
,
"Accept-Encoding":"gzip",
"User-Agent":"okhttp/3.14.9"


}

data='{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'

e=requests.post(url, headers=header, data=data).json()
#print(e)

ctv=e["GenerateTokenResult"]["Token"]
#print(ctv)
import hashlib

def encrypt_string(hash_string):
    htv = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return htv
hash_string = ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
h= encrypt_string(hash_string)
htv=h.upper()

#print(htv)
#===============================
url2="https://services.orange.eg/SignIn.svc/SignInUser"

headers={
"_ctv": ctv,
"_htv": htv,
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "165",
"Host": "services.orange.eg",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.14.9"
}

data2='{"appVersion":"6.9.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"'+num+'","isAndroid":true,"password":"'+pas+'"}'

res=requests.post(url2, headers=headers, data=data2).json()

#print(res)

userid=res["SignInUserResult"]["UserData"]["UserID"]

#print(userid)
#================================
url_card="https://services.orange.eg/MyOrange/api/Recharge/SuperRechargeViaScratchCard"

header_card={
"ChannelName":"MobinilAndMe",
"ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF",
"_ctv": ctv,
"_htv": htv,

"isEasyLogin":"false",
"UserId": userid,
"net-net-msg-id":"db61dfde020930d16931223873261072",
"x-microservice-name":"APMS",
"Content-Type":"application/json; charset=UTF-8",
"Content-Length":"108",

"Host":"services.orange.eg",

"Connection":"Keep-Alive",
"Accept-Encoding":"gzip",
"User-Agent":"okhttp/3.14.9",

 }
print(header_card) 
 
data_card={
  "Mode": 1,
  "Card": {
    "Number": card,
  },
  "Language": "ar",
  "dial": num,
  "password": pas
}
print(data_card)
r_card=requests.post(url_card, headers=header_card, json=data_card).json()
print(r_card) 
