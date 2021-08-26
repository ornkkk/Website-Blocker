# Website-Blocker

## This is a repository for debian linux website blocker using Python.

### Files

- website_blocker.py

This is the *python script* file for the website blocker.

- website-blocker.service

This is the *unit file* for running the python script as a system service and loading it at startup.


### Installation Instructions
- Download the repository by executing following commands
```
cd ~/Downloads
git clone https://github.com/ornkkk/Website-Blocker.git
cd Website-Blocker
```
- Open the Python script file and edit the following lines
~~~
start_time = "08:15" #hh:mm 24-hour format
end_time = "18:00" #hh:mm 24-hour format
  
# websites That you want to block
website_list = ["www.facebook.com",
                "www.youtube.com"]
~~~

