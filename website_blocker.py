#! /bin/python3
# Run this script as root
  
import time
import datetime as dt
from signal import signal, SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM, SIGHUP
import sys
  
# change hosts path according to your OS
hosts_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"

start_time = "08:15" #hh:mm 24-hour format
end_time = "18:00" #hh:mm 24-hour format
  
# websites That you want to block
website_list = ["www.facebook.com",
                "www.youtube.com"]


def blocker():
    with open(hosts_path, "r+") as f:
        content = f.read()
        for website in website_list:
            if website in content:
                pass
            else:
                # mapping hostnames to your localhost IP address
                f.write(redirect + " " + website + "\n")

def unblocker():
    with open(hosts_path, 'r+') as f:
            content=f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
                else:
                    # removing hostnmes from host file
                    f.truncate()

def clean(*args):
    unblocker()
    sys.exit(0)


if __name__=="__main__":
    work_start_time = dt.time(*map(int, start_time.split(":")))
    work_end_time = dt.time(*map(int, end_time.split(":")))

    signals = (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM, SIGHUP)

    for sig in signals:
        print(sig)
        signal(sig, clean)

    while True:
        now = dt.datetime.now().time()
        if work_start_time < now < work_end_time:
            blocker()
        else:
            unblocker()
            
        time.sleep(5)  
