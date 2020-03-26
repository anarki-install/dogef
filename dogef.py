from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest
from time import sleep
import json,sys,os,time,re,random
  
if not os.path.exists("session"):
    os.makedirs("session")
   
if len(sys.argv)<2:
   print ("\n\n\n\033[1;32mUsage : python main.py +62")
   sys.exit(1)
   
banner = f"""\033[1;35m
                                              
eeeee  eeeee e    e eeee eeeee       e  eeeee 
8   8  8   8 8    8 8    "   8       8  8   8 
8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 
88   8 88  8   88   88   88          88 88  8 
88   8 88  8   88   88ee 88ee8       88 88ee8 
                               eeeee
\033[1;36m=============================================
\033[1;32m - anthesphong1998@gmail.com - t.me/rayez_id
\033[1;36m=============================================          
"""

os.system('clear')
print(banner)
  
def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    while x:
       mins, secs = divmod(x, 60)
       timeformat = '{:02d}:{:02d}'.format(mins, secs)
       sys.stdout.write("\r")
       sys.stdout.write(f"\033[1;30m[\033[1;32m|\033[1;30m] \033[1;32mClaim after \033[1;0m{timeformat} \033[1;32mseconds")
       sys.stdout.flush()
       sleep(1)
       x -= 1
       
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)      
        
ua={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
api_id = 800812
api_hash = "db55ad67a98df35667ca788b97f771f5"
phone_number = sys.argv[1]

client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
  client.send_code_request(phone_number)
  me = client.sign_in(phone_number, input('\n\n\n\033[1;0mEnter Your Code Code : '))
  sleep(1)
  
myself = client.get_me()
os.system('clear')
print(banner)
mengetik(f"\033[1;35mWELCOME TO THE BOT (v01) \033[1;36m- {myself.first_name}\n\033[1;35mSCRIPT INI UNTUK NUYUL \033[1;36m- @Faucet_Doge_Master_bot\n\n")

try:
  channel_entity=client.get_entity("@Faucet_Doge_Master_bot")
  channel_username="@Faucet_Doge_Master_bot"
  for i in range(50000):
    sys.stdout.write("\r")
    sys.stdout.write("                                                              ")
    sys.stdout.write("\r")
    sys.stdout.write("\033[1;30m[\033[1;33m|\033[1;30m] \033[1;33mClaim the bonus ... !")
    sys.stdout.flush()
    client.send_message(entity=channel_entity,message="♋ Bonus")
    sleep(2)
    client.send_message(entity=channel_entity,message="Ⓜ️ Account")
    sleep(1)
    posts = client(GetHistoryRequest(peer=channel_entity,limit=5,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    posts_ = posts.messages[3].message
    posts__ = posts.messages[0].message
    posts___ = re.findall(r'([\d.]*\d+) DOGECOIN', posts__)
    if "You Get a" in posts_:
      sys.stdout.write(f"\r\033[1;30m[\033[1;32m|\033[1;30m] \033[1;32mSucces Collect bonus | 0.0012 DOGE\n")
      sleep(1)
      sys.stdout.write(f"\r\033[1;30m[\033[1;32m|\033[1;30m] \033[1;32mYour balance has been updated : {posts___[0]} DOGE\n")
      tunggu(310)
    else:
      sys.stdout.write(f"\r\033[1;30m[\033[1;31m|\033[1;30m] \033[1;31m Gagal claim bonus\n")
      sys.exit()
    
finally:
   client.disconnect()
    