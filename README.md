#Cisco Web Portal

Cisco portal to display and shut/no shut interfaces 

This project was created after watching the video created by Dmitry Figol:
https://www.youtube.com/watch?v=7bhTyCCASPo

It is recommended you run this in virtual environment.

virtualenv Cisco_Web_Portal_TEST

cd Cisco_Web_Portal_TEST/bin

source activate

git clone https://github.com/aresik/Cisco_Web_Portal.git

cd Cisco_Web_Portal

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

Browse to http://127.0.0.1:8000/ - Notice there is no device in the list.

Browse to http://127.0.0.1:8000/admin - Login with the user/pass set above.

Go to Devices -> ADD DEVICE+ -> Fill in the details of your device and click SAVE.

Browse to http://127.0.0.1:8000/ and notice the newly added device. Click on it and wait a few seconds.

In the background a python script fetches the interfaces and will be displayed back on the Portal.

Select an interface in the list (not your Uplink; pick a Loopback) and click Switch to shut or no shut it.

This take a few seconds for the script to go to the device and perform the shut or no shut. 

When completed the "Enabled?" checkbox will be changed.

That's all for now.




