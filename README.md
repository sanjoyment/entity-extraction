# entity-extraction

Steps:

$ cd entity-extraction
$ python3 -m venv test_env

$ source test_env/bin/activate

(venv) $ pip install -r requirements.txt

(venv) $ python3 acquire_chatterbot_old.py
OR
$ ./test_env/bin/python3 acquire_chatterbot_old.py

(venv) $ deactivate

$ forever start -c ./test_env/bin/python3 acquire_chatterbot_old.py

Ref for Screen: https://linuxize.com/post/how-to-use-linux-screen/

IP/PORT: http://147.135.37.191:9978

---------------------

$ screen -S <NAME> #to create a new screen
 
$ screen -ls #to list all screens

$ screen -r <NAME> #open any screen

$ ctrl+AD #close current screen

$ ctrl+AX #delete any screen

working screen: 23921.mktf.acquire.io

$ screen -X -S [session # you want to kill] quit

---------------------
