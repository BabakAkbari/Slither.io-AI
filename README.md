# slither.io-v0

`slither.io-v0` is an openAI [gym](https://gym.openai.com/) enviroment for testing and evaluating reinforcment learning algorithms in a popular classic snake game such as [slither.io](http://slither.io/). The enviroment has a reasonably large field with multiple snakes. snakes grow when eating randomly-appearing fruit a snake dies when colliding with another snake, itself, or the wall and the game ends when all snakes die.   

Getting started
===============

Installation
------------


Supported systems
We currently support Linux and OSX running Python 2.7 or 3.5.
Install Universe

To get started, first install ``slither.io-v0``:

<h3>Supported systems:</h3>
We currently support Linux and OSX running Python 2.7 or 3.5.
Install slither.io-v0
To get started, first install ``slither.io-v0``:

~~~~~~~~~~~~~~~~~
    git clone https://github.com/BabakAkbari/Slither.io-AI.git
    cd Slither.io-AI/
    pip install -e gym-slitherio				
~~~~~~~~~~~~~~~~~~

Now install the latest version of [docker](https://docs.docker.com/install/) and then:

~~~~~~~~~~~~~~~~~~
docker build -t slitherio .
docker run --name=slither -v $(pwd):/home/apps -p 5005:5005 -p 5900:5900 -it --rm --user apps --privileged slitherio bash -l
~~~~~~~~~~~~~~~~~~

In the docker container's bash run the following commands:

~~~~~~~~~~~~~~~~~~
export DISPLAY=:0
vncserver :0
cd /home/apps
python remote.py
~~~~~~~~~~~~~~~~~~


You will be asked to setup a password for your vnc enviroment. By default the password `secure` is hardcoded. You can change it whenever you want.
Now your vncserver is ready. You can use a vncclient software with the given password to view the following screen.  
<img src="http://s6.picofile.com/file/8389207684/Screenshot_from_2020_02_24_22_33_30.png">
