# Hackathon2015


This is our project for this year's Hackathon. Open-sourced for everyone to enjoy it.

This project is IoT-oriented. We use a RaspberryPi(raspdebian or windows IoT, with python2.7) and a computer to provide service.

First we start a Tornado server(`TornadoServer.py`) and a daemon process(`pi_surveillance.py`) to capture the picture. We also start the client server on a computer.

In this case, the RaspberryPi will automatically captures picture if it has detected a environment change for sometime. The detection uses OpenCV for real-time performance, which was inspired by several cases on the Internet (The code has been heavily changed by us. This is much more than just read and copy). You can refer to `pi_surveillance.py` for details.

After a picture was captured, `pi_surveillance.py` will make use of the Oxford Project to gain more information about the picture(Notice: we drop the oxford key-file into the .gitignore. It shouldn't be public. Do not hack it!). Then it'll send the result to `TornadoServer.py`. `TornadoServer.py` will keep the result.

At about the same time, the client keeps polling messages from the RaspberryPi. `TornadoServer.py` will response with a string if the the result comes. Then the computer will alert a warning window about the changes. 

By the way, we also realize a remote control system `Hackathon2015_Addition` for you to control your computer with your phone (something also cool). I used it for a lecture about web security and it works well.

That's all. There may exist serveral bugs and there should be something with the configuration. But we do not have enough time. We just hack it. Then it will be improved in the future if supported.

Thank u for reading the doc.

## Here are something technical:

### Requirements : RaspberryPi with Python2.7.9+ but not Python3.*, a computer with wireless network device and has windows installed. The raspberrypi has a fixed IP 192.168.43.161. You should also configure it with imaging libraries (libjpeg, imutils, opencv and more). Frankly speaking, we find it very hard with configuration, for different computers varies a lot from their environment. So it is OK that you find it cannot work inside your computer, for you need to deal with your environment.
Take raspdebian system as an example, you may need to:
1. Set your wifi connected to a router correctly. (/etc/network/interface)
2. ssh to login
3. sudo apt-get update
4. sudo apt-get upgrade (it'll take a long time)
5. wget ... to download the latest python2 version (python2.7.9/10)
6. configure the downloaded version
7. make install to compile it for ARM Architecture
8. Check if it works fine, if not try step 6
9. try sudo apt-get install to get librarys like libjpeg and so on to support different image types
10. as step 5-8, try to get pip.
11. Check if the pip is the pip you get in the last step. If not try something like pip-2.7.9
12. sudo pip install opencv(or may cv2)
13. sudo pip install imutils
14. sudo pip install certifi
15. sudo pip install tornado
16. sudo pip install requests
17. sudo pip install picamera
...Then you may start our project.

If you are in windows-IoT,
1. Use powershell to start the Remote Management Server
2. Use powershell to add raspberrypi into the known hosts
3. Use powershell to login. If fail you may check your parameters in step 1-3.
4. [in the raspberrypi] Try to make your Pi recognize the wireless network card. It is proved to be very hard. You may find dirvers and try to install it.
5. Use netsh to connect to your wifi.
6. Refer to ipconfig to find whether it is well configured.
7. Try to get a C/C++ compile which configured to support CPython (We find it difficult. It is optional).
8. Use pip to install different libraries as follow. You need to set environment for pip by yourself.
9. Follow guides on Microsoft's website to get ideas about how to deal with python projects.

## Programmer's advice to big companies and anyone devoted to IoT platform

### As a matter of fact, we find IoT devices very hard to configure. We hope companies like Microsoft to provide more user-friendly and programmable IoT-related devices and platforms.
### Or most of our time will be wasted in configuring and find solutions on the Internet but not a guide. And then we can devoted to real IoT developing.