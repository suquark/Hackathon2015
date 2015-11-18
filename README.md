# Hackathon2015

This is our project for this year's Hackathon. Open-sourced for everyone to enjoy it.

This project is IOT-oriented. We use a RaspberryPi and a computer to provide service. 

First we start a Tornado server(`TornadoServer.py`) and a daemon process(`pi_surveillance.py`) to capture the picture. We also start the client server on a computer.

In this case, the RaspberryPi will automatically captures picture if it has detected a environment change for sometime. The detection uses OpenCV for real-time performance, which was inspired by several cases on the Internet (The code has been heavily changed by us. This is much more than just read and copy). You can refer to `pi_surveillance.py` for details.

After a picture was captured, `pi_surveillance.py` will make use of the Oxford Project to gain more information about the picture(Notice: we drop the oxford key-file into the .gitignore. It shouldn't be public. Do not hack it!). Then it'll send the result to `TornadoServer.py`. `TornadoServer.py` will keep the result.

At about the same time, the client keeps polling messages from the RaspberryPi. `TornadoServer.py` will response with a string if the the result comes. Then the computer will alert a warning window about the changes. 

By the way, we also realize a remote control system for you to control your computer with your phone.

That's all. There may exist serveral bugs and there should be something with the configuration. But we do not have enough time. We just hack it. Then it will be improved in the future if supported.

Thank u for reading the doc.
