# Welcome to Week-3 of Learner's Space

This week we are going to learn to use Pygame, a collection of fun, powerful Python modules
that manage graphics, animation, and even sound, making it easier for you to build sophis-
ticated games. With Pygame handling tasks like drawing images to the screen, you can skip much of the
tedious, difficult coding and focus on the higher-level logic of game dynamics.

Making games is an ideal way to have fun while learning a language. It’s deeply satisfying to watch others play a game you wrote, and writing a simple game 
will help you understand how professional games are written.  

To learn about the pygame library we will be taking a more practical approach. We will be making an *Alien invasion game* (somewhat like *asteroids*) and while doing that explore various aspects of the Pygame library. We will not just learn about the functions in Pygame but learn about some general concepts of GameDev as well like sprites, events, collisions which will be used in quite a similar way with whatever language you use. 

You will also get to learn about some good programming practices such as **refactoring**. This is how we are going to be procedding with making this game:

- [Setup Pygame](#Setting-up-Pygame)
- [Initial Setup](#Starting-the-Game-Project)
- [Piloting the ship](#Making-the-ship-function)
- [Creating the aliens](#Creating-Aliens)
- [Making the aliens function](#Making-the-Aliens-Function)


Note the game will span a number of different files, so make a new folder called alien_invasion. Be sure to save all files for the game to this folder so *import* statements will work correctly.


## Setting up Pygame
Before we begin coding, we must install Pygame. Here’s how to do so on Linux, MacOS X, and Microsoft Windows:  
To install on Windows you can go through [this](https://www.youngwonks.com/blog/How-to-Install-PyGame-on-Windows) link.  
To install on Mac you can go through [this](https://www.youngwonks.com/blog/How-to-Install-PyGame-on-a-Mac) link.
### Installing Pygame on Linux
To install Pygame using the package manager.
Open a terminal window and run the following command, which will
download and install Pygame onto your system:  
```
 sudo apt-get install python-pygame
```
If you are using pyhton 3 just replace `python-pygame` with `python3-pygame`.  
To make sure its been installed correctly open the python interpreter by runnning `python` or `python3` on the terminal depending on your version of python.
Then try running `import pygame`. If it runs without any error then pygame is successfully installed.

## Starting the Game Project
Now to begin building our game we will first make the pygame window where we will add the various elements of the game like ship and aliens, setup the background etc. You will learn how to create *surfaces* with pygame which refer to a part of the screen where you display a game element. Each element in the game is a *surface*. You will also learn about *events* which is an action that the user performs while playing the game, such as pressing a key or moving the mouse.  
You can go through [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Initial_Setup.ipynb) to learn about these things. 

You can go through [this video](https://www.youtube.com/watch?v=Wdyn1uGkRAU) if you want to learn more about making **surfaces** in Pygame.

## Making the ship function
After building the basic setup, the next setup is to make the ship respond to user's inputs. In this section we will work on making the ship move according to input from the keyboard. Through this you will learn more about events. Another concept you will be introduced to is refactoring. Refactoring restructures the code so as to make it easier for you as well as other people to understand it as welss as develop it further. You can go through [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Ship_Function.ipynb) to learn about refactoring and piloting the ship.

To learn more about events in Pygame you can go through [this](https://www.youtube.com/watch?v=umHZ6wnQTyQ) and [this](https://www.youtube.com/watch?v=nE5EeQPiznU) video.  You can also go through the [documentation](https://www.pygame.org/docs/ref/event.html) for this especially to get to know about what kinds of events does pygame support. You can tak input from mouse even joystick.

Next thing to do would be to give the ship the ability to shoot bullets. To do this you will learn about the concept of *sprites*. A sprite is a two dimensional image that is part of the larger graphical scene. Typically a sprite will be some kind of object in the scene that will be interacted with. You can learn about that in [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Bullets.ipynb).

## Creating Aliens
Creating aliens is going to be quite similar to creating the ship. However, the difference is that while there was only a single ship, but there is a fleet of aliens. So we will be creating rows of aliens that will move sideways as well as downward. You can learn about this in [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Creating_Aliens.ipynb).

## Making the Aliens Function
We have created the fleet of aliens. Now we will program those aliens to move in a specific pattern while heading down (just to make it a bit more interesting). We will also code the bullets to shoot down the aliens. In doing so you will learn about **collisions**. To detect collisions we just have to check whether 2 objects(sprites, rects...) overlap. Pygame makes this pretty easy to check. With this we will also code for ending our game. The game ends if any of the aliens hit the ship or reach the bottom. We will again use **collision detetction** for this. You can go through [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Alien_Function.ipynb) to see how we do all this. 

To learn more about collisions you can go through [this](https://www.youtube.com/watch?v=bQnEQvyS1Ns) video.

With this we now have a somewhat completely working game. You look into the [alien_invasion folder](https://github.com/Karrthik-Arya/TSS-2021/tree/main/Python%20%26%20its%20Applications/Week-3/alien_invasion) for the complete game files that we just made. 

If you'd like to explore more there are a lot many modifications you can do. You can add sounds to the game (about which you can learn [here](https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/)) as well. You can add **Play**, **Restart** etc. buttons to the game (You will have to take input from the mouse using MOUSEBUTTONDOWN event and check the position of the point where the user clicked). You can add a scoreboard( each time an alien is shot you will have to update the score). These are some possible modifications but you can do a lot more. You can definitely look into the [documentation](https://www.pygame.org/docs/), its written pretty well and though that you can learn about any function in Pygame.  
