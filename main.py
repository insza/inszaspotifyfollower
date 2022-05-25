from keyauth import api
import os
import sys
import os.path
import platform
import hashlib
import threading, os, time
from time import sleep
from datetime import datetime
from turtle import title
from follow_bot import spotify
from pystyle import Colors, Colorate
from turtle import colormode
from click import clear
from colorama import colorama_text
from follow_bot import spotify
import threading, os, time
from pystyle import Colors, Colorate
from turtle import title
import os, time

import os

# watch setup video if you need help https://www.youtube.com/watch?v=L2eAQOmuUiA
os.system("cls||clear")
os.system("title Spotify Follower Bot V1 - insza")
print(Colors.green,("Başlatılıyor."))
sleep(0.5)
os.system("cls||clear")
print(Colors.green,("Başlatılıyor.."))
sleep(0.5)
os.system("cls||clear")
print(Colors.green,("Başlatılıyor..."))
os.system("cls||clear")
sleep(0.5)
print(Colors.red,("Yazılım insza'ya Aittir, Çalınması Halinde Cezai İşlemler Başlatılıcaktır!"))
sleep(2)
os.system("cls||clear")
def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
    	path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path,"rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest
keyauthapp = api(
	name = "spotify follower bot - insza",
	ownerid = "1UX0gTCbRd",
	secret = "becb14e8c3b28b9e9ccc0ed061fb4f9a7d497721c958b7d9477ff49bdbb1ceee",
	version = "1.0",
	hash_to_check = getchecksum()
)
print(Colors.green, ("1. Giriş Yap"))
print(Colors.light_green, ("2. Kayıt Ol"))
print(Colors.red, ("3. Lisans Yenile"))
print(Colors.gray, ("4. Yalnızca Lisans Anahtarı\n\n"))
print(Colors.light_blue, (f"Data - Program Verileri:"))
print(Colors.light_blue, (f"insza - Kullanıcı Sayısı: {keyauthapp.app_data.numUsers}"))
print(Colors.light_blue, (f"insza - Çevrimiçi Kullanıcı Sayısı: {keyauthapp.app_data.onlineUsers}"))
print(Colors.light_blue, (f"insza - Lisans Sayısı: {keyauthapp.app_data.numKeys}"))
print(Colors.light_blue, (f"insza - Program Sürümü: {keyauthapp.app_data.app_ver}\n\n"))


print("---------------------------------------------------------------------------------------\n\n")
sleep(1.5) # rate limit
print(Colors.green, (f"Mevcut Oturum Doğrulama Durumu?(True= Evet, False= Hayır)\n\n Doğrulama - {keyauthapp.check()}\n"))
sleep(1.5) # rate limit
print(Colors.red, (f"Kara Listede Var Mısın?(True= Evet, False= Hayır)\n\n Doğrulama - {keyauthapp.checkblacklist()}\n\n")) # check if blacklisted, you can edit this and make it exit the program if blacklisted
sleep(1.5)
ans=input("> ")
if ans=="1": 
	user = input('Kullanıcı Adı: ')
	password = input('Şifre: ')
	keyauthapp.login(user,password)
elif ans=="2":
	user = input('Kullanıcı Adı: ')
	password = input('Şifre: ')
	license = input('Lisans Anahtarını Girin(lisans satın almak için discord: insza#0047 & Adelion#0001) ')
	keyauthapp.register(user,password,license) 
elif ans=="3":
	user = input('Kullanıcı Adı: ')
	license = input('Yeni Lisans Anahtarını Girin(lisans satın almak için discord: insza#0047 & Adelion#0001) ')
	keyauthapp.upgrade(user,license)
elif ans=="4":
	key = input('Lisans Anahtarını Girin(lisans satın almak için discord: insza#0047 & Adelion#0001) ')
	keyauthapp.license(key)
else:
	print(Colors.red, ("\nGeçerli Bir Seçenek Değil!")) 
	sys.exit()


os.system("cls||clear")
print(Colors.green, ("\nData - Kullanıcı Verisi: "))
print(Colors.light_blue, ("insza - Kullanıcı Adı: " + keyauthapp.user_data.username))
print(Colors.light_blue, ("insza - IP Adresiniz: " + keyauthapp.user_data.ip))
sleep(2.5)
os.system("cls||clear")
#print("Subcription: " + keyauthapp.user_data.subscription) ## Print Subscription "ONE" name

subs = keyauthapp.user_data.subscriptions ## Get all Subscription names, expiry, and timeleft
for i in range(len(subs)):
  sub = subs[i]["subscription"] # Subscription from every Sub
  expiry = datetime.utcfromtimestamp(int(subs[i]["expiry"])).strftime('%Y-%m-%d %H:%M:%S') ## Expiry date from every Sub
  timeleft = subs[i]["timeleft"] ## Timeleft from every Sub

print(Colors.green, ("\nData - Hesap Verisi: "))
print(Colors.light_blue, ("insza - Hesabınızın Oluşturulma Tarihi: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S')))
print(Colors.light_blue, ("insza - Hesabınıza Son Girdiğiniz Tarih: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S')))
print(Colors.light_blue, ("insza - Lisans Bitiş Tarihi: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S')))
print(Colors.light_blue, (f"insza - Mevcut Oturum Doğrulama Durumu: {keyauthapp.check()}\n"))
print(Colors.red, (f"insza - [{i + 1} / {len(subs)}] | Lisans: {sub} - Bitiş: {expiry} - Kalan Süre(dk): {timeleft}\n\n"))
time.sleep(2.5)
print(Colors.green, ("Giriş Başarıyla Yapıldı!"))
print(Colors.gray, ("Programa Yönlendiriliyorsunuz!"))
time.sleep(3)
os.system("cls||clear")

os.system("title Spotify Follower Bot V1 - insza")


lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
line = print(Colorate.Horizontal(Colors.green_to_blue, ("                              ╚╦══════════════════════════════════╦═════════════════════╦╝")))
print(Colorate.Horizontal(Colors.green_to_blue, ("""                                                         
                       
                                  ,--,                                                   
                                ,--.'|         ,---,                   ,----,            
                                |  |,      ,-+-. /  | .--.--.        .'   .`|            
                                `--'_     ,--.'|'   |/  /    '    .'   .'  .' ,--.--.    
                                ,' ,'|   |   |  ,"' |  :  /`./  ,---, '   ./ /       \   
                                '  | |   |   | /  | |  :  ;_    ;   | .'  / .--.  .-. |  
                                |  | :   |   | |  | |\  \    `. `---' /  ;--,\__\/: . .  
                                '  : |__ |   | |  |/  `----.   \  /  /  / .`|," .--.; |  
                                |  | '.'||   | |--'  /  /`--'  /./__;     .'/  /  ,.  |  
                                ;  :    ;|   |/     '--'.     / ;   |  .'  ;  :   .'   \ 
                                |  ,   / '---'        `--'---'  `---'      |  ,     .-./ 
                                ---`-'                                     `--`---'     
                                                                                                                                                                 """)))
v2 = print(Colorate.Horizontal(Colors.green_to_blue, ("                              ╚╦══════════════════════════════════╦═════════════════════╦╝")))
spotify_profile = str(input(Colorate.Horizontal(Colors.green_to_white,  ("\n\nSpotify Link: "))))
threads = int(input((Colorate.Horizontal(Colors.white_to_green, "\nHız(100 önerilir) : "))))

def load_proxies():
    if not os.path.exists("./proxy/inszaproxy.txt"):
        print(Colorate.Horizontal(Colors.red_to_white, ("\nProxy Dosyası Bulunamadı!")))
        time.sleep(10)
        os._exit(0)
    with open("./proxy/inszaproxy.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print(Colorate.Horizontal(Colors.red_to_white, ("\nProxy Dosyasında Proxy Yok!")))
            time.sleep(10)
            os._exit(0)

print(Colors.gray, ("\nProxy Generator Satın Almak İçin Discord: insza#0047 & Adelion#0001 Ulaşın!"))
print(Colors.green, ("\n[1] Proxy VAR(önerilir)"))
print(Colors.red, ("\n[2] Proxy YOK"))
print(Colors.gray, ("\n[UYARI] PROXYLER HTTPS & HTTP OLMAK ZORUNDADIR! "))
option = int(input(Colorate.Horizontal(Colors.purple_to_red, ("\n> @insza "))))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print(Colorate.Horizontal(Colors.green_to_white, ("[BAŞARILI] Takip Edildi! {}".format(counter))))
    else:
        safe_print(Colorate.Horizontal(Colors.red_to_white, (f"[BAŞARISIZ] Hata! {error}")))
            
while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: #Loops through proxy file
            proxy_counter = 0


sleep(10)
