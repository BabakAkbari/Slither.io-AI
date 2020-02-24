# slither.io-v0

`slither.io-v0` is an openAI [gym](https://gym.openai.com/) enviroment for testing and evaluating reinforcment learning algorithms in a popular classic snake game such as [slither.io](http://slither.io/). The enviroment has a reasonably large field with multiple snakes. snakes grow when eating randomly-appearing fruit a snake dies when colliding with another snake, itself, or the wall and the game ends when all snakes die.   

Getting started
===============

Installation
------------

Supported systems:
We currently support Linux and OSX running Python 2.7 or 3.5.
Install Universe
To get started, first install ``slither.io-v0``:
~~~~~~~~~~~~~~~~~
    https://github.com/BabakAkbari/Slither.io-AI.git
    cd Slither.io-AI/
    pip install -e gym-slitherio				
~~~~~~~~~~~~~~~~~~
Now install the latest version of [docker](https://docs.docker.com/install/)
~~~~~~~~~~~~~~~~~~
docker build -t slitherio .
docker run --name=slither -v $pwd:/home/apps -p 5005:5005 -p 5900:5900 -it --rm --user apps --privileged slitherio bash -l
~~~~~~~~~~~~~~~~~~
