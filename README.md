# Website-Blocker :no_entry_sign: :no-entry:

## This is a repository for debian linux website blocker using Python.

### Files

- `website_blocker.py`

This is the *python script* file for the website blocker.

- `website-blocker.service`

This is the *unit file* for running the python script as a system service and loading it at startup.

### Installation Instructions

- Download the repository by executing following commands

```
cd ~/Downloads
git clone https://github.com/ornkkk/Website-Blocker.git
cd Website-Blocker
```

- Open the `website_blocker.py` file and edit the following lines.

~~~
start_time = "08:15" # HH:MM in 24-hour format
end_time = "18:00" # HH:MM in 24-hour format
  
# websites that you want to block
website_list = ["www.facebook.com",
                "www.youtube.com"]
~~~

- Change the `start_time`, `end_time`accordingly. Add the website you want to be blocked to `website_list`.
- Open `website-blocker.service` and add the absolute path to the python script file to `ExecStart` parameter. By default the absolute path is `/home/<user>/Downloads/Website-Blocker/website_blocker.py`

  ~~~
  ExecStart=/home/<user>/Downloads/Website-Blocker/website_blocker.py
  ~~~
  Note: Replace `<user>` with your username.
 
 - Give execute permissions to the script file
 ```
 sudo chmod +x website_blocker.py
 ```
 - Add the unit file to the system services to automatically load at every startup
 ```
 sudo cp website-blocker.service /etc/systemd/system/
 sudo systemctl daemon-reload
 reboot
 ```
 - After reboot you can see that the script file will be running automatically. To verify visit any of the blocked websites. They should be unreachable.
 - To manually start/stop the service use following commands:
 ```
 sudo systemctl start website-blocker
 sudo systemctl stop website-blocker
 ```
