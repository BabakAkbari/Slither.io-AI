**This repository has been deprecated in favor of the Retro (https://github.com/openai/retro) library. See our Retro Contest (https://blog.openai.com/retro-contest) blog post for detalis.**

#universe
***************

`slither.io-v0 <https://openai.com/blog/universe/>`_ is a software
platform for measuring and training an AI's general intelligence
across the world's supply of games, websites and other
applications. This is the ``universe`` open-source library, which
provides a simple `Gym <https://github.com/openai/gym>`__
interface to each Universe environment.

Universe allows anyone to train and evaluate AI agents on an extremely
wide range of real-time, complex environments.

Universe makes it possible for any existing program to become an
OpenAI Gym environment, without needing special access to the
program's internals, source code, or APIs. It does this by packaging
the program into a Docker container, and presenting the AI with the
same interface a human uses: sending keyboard and mouse events, and
receiving screen pixels. Our initial release contains over 1,000
environments in which an AI agent can take actions and gather
observations.

Additionally, some environments include a reward signal sent to the
agent, to guide reinforcement learning. We've included a few hundred
environments with reward signals. These environments also include
automated start menu clickthroughs, allowing your agent to skip to the
interesting part of the environment.

We'd like the community's `help <https://openai.com/blog/universe/#help>`_
to grow the number of available environments, including integrating
increasingly large and complex games.

The following classes of tasks are packaged inside of
publicly-available Docker containers, and can be run today with no
work on your part:

- Atari and CartPole environments over VNC: ``gym-core.Pong-v3``, ``gym-core.CartPole-v0``, etc.
- Flashgames over VNC: ``flashgames.DuskDrive-v0``, etc.
- Browser tasks ("World of Bits") over VNC: ``wob.mini.TicTacToe-v0``, etc.

We've scoped out integrations for many other games, including
completing a high-quality GTA V integration (thanks to `Craig Quiter <http://deepdrive.io/>`_ and NVIDIA), but these aren't included in today's release.

.. contents:: **Contents of this document**
   :depth: 2


Getting started
===============

Installation
------------

Supported systems
~~~~~~~~~~~~~~~~~

We currently support Linux and OSX running Python 2.7 or 3.5.
