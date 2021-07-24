# Welcome to Week-3 of Learner's Space

This week we are going to learn to use Pygame, a collection of fun, powerful Python modules 
that manage graphics, animation, and even sound, making it easier for you to build sophisticated games. With Pygame, handling tasks like drawing images on the screen, you can skip much of the tedious, difficult coding and focus on the higher-level logic of game dynamics.

Making games is an ideal way to have fun while learning a language. It’s deeply satisfying to watch others play a game you wrote, and writing a simple game 
will help you understand how professional games are written.  

To learn about the pygame library we will be taking a more practical approach. We will be making an *Alien invasion game* (somewhat like *asteroids*) and while doing that explore various aspects of the Pygame library. We will not just learn about the functions in Pygame but learn about some general concepts of GameDev as well like sprites, events, collisions which will be used in quite a similar way with whatever language you use. 

You will also get to learn about some good programming practices such as **refactoring**. This is how we are going to be procedding with making this game:

- [Setup Pygame](#Setting-up-Pygame)
- [Initial Setup](#Starting-the-Game-Project)
- [Piloting the ship](#Making-the-ship-function)
- [Creating the aliens](#Creating-Aliens)
- [Making the aliens function](#Making-the-Aliens-Function)
- [Assignment](#Assignment)


Note the game will span a number of different files, so make a new folder called alien_invasion. Be sure to save all files for the game to this folder so *import* statements will work correctly.  Do not run the notebooks, save the files as per instructions and thereafter test the code.


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
After building the basic setup, the next setup is to make the ship respond to user's inputs. In this section we will work on making the ship move according to input from the keyboard. Through this you will learn more about events. Another concept you will be introduced to is refactoring. Refactoring restructures the code so as to make it easier for you as well as other people to understand it and develop it further. You can go through [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Ship_Function.ipynb) to learn about refactoring and piloting the ship.

To learn more about events in Pygame you can go through [this](https://www.youtube.com/watch?v=umHZ6wnQTyQ) and [this](https://www.youtube.com/watch?v=nE5EeQPiznU) video.  You can also go through the [documentation](https://www.pygame.org/docs/ref/event.html) for this, especially to get to know about what kinds of events does pygame support. You can take input from mouse or even joystick.

Next thing to do would be to give the ship the ability to shoot bullets. To do this you will learn about the concept of *sprites*. A sprite is a two dimensional image that is part of the larger graphical scene. Typically a sprite will be some kind of object in the scene that will be interacted with. You can learn about that in [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Bullets.ipynb).

You can vist [this link](https://www.pythoninformer.com/python-libraries/pygame/sprite-class/) if you would like to know more about the sprite class and you can always go to the [documentation](https://www.pygame.org/docs/ref/sprite.html). 

## Creating Aliens
Creating aliens is going to be quite similar to creating the ship. However, the difference is that while there was only a single ship, there is a fleet of aliens. So we will be creating rows of aliens that will move sideways as well as downward. You can learn about this in [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Creating_Aliens.ipynb).

## Making the Aliens Function
We have created the fleet of aliens. Now we will program those aliens to move in a specific pattern while heading down (just to make it a bit more interesting). We will also code the bullets to shoot down the aliens. In doing so you will learn about **collisions**. To detect collisions we just have to check whether 2 objects(sprites, rects...) overlap. Pygame makes this pretty easy to check. With this we will also code for ending our game. The game ends if any of the aliens hit the ship or reach the bottom. We will again use **collision detetction** for this. You can go through [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/Alien_Function.ipynb) to see how we do all this. 

To learn more about collisions you can go through [this](https://www.youtube.com/watch?v=bQnEQvyS1Ns) video.

With this we now have a somewhat completely working game. You look into the [alien_invasion folder](https://github.com/Karrthik-Arya/TSS-2021/tree/main/Python%20%26%20its%20Applications/Week-3/alien_invasion) for the complete game files that we just made. 

If you'd like to explore more there are a lot many modifications you can do. You can add sounds to the game (about which you can learn [here](https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/)) as well. You can add **Play**, **Restart** etc. buttons to the game (You will have to take input from the mouse using MOUSEBUTTONDOWN event and check the position of the point where the user clicked). You can add a scoreboard( each time an alien is shot you will have to update the score). These are some possible modifications but you can do a lot more. You can definitely look into the [documentation](https://www.pygame.org/docs/), its written pretty well and through that you can learn about any function in Pygame.  

## Assignment
This week you have a choice of doing either of the 2 assignments. The snake game is a bit easier than the flappy bird. However the flappy bird looks a bit more interesting in the end. Depending on the time you have available you can do any of them.
### Snake Game
In this, you will be making the classic snake game which you must have played sometime in your life. You will be making the snake, apple out of rectangles in pygame. A basic outline of the code along with some initializations has been given in the file [snake.py](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/snake.py). You are supposed to fill these functions:
- **check_for_events()** : This should contain the main for loop (listening for events). You hsould have code for responding when someone quits or presses the arrow keys. Also make sure that snake cannot reverse direction abruptly i.e. if its moving right it cannot change directly change its direction to left.
- **create_food()**: This should generate new position for the food if its eaten by the snake. You can use [randrange() function](https://docs.python.org/3/library/random.html#random.randrange) from the random module. 
- **update_snake()**: This function should make the snake move in the appropriate direction. Think how the snake's body and head moves when you change the direction. Here you are also supposed to code for responding if the snake eats the food. You also have to code for detetcing if it collides with the walls or with itself(the **game_over** function will be used). However you cannot directly use the functions for detecting collisions since we are not making specific sprites or surfaces for snake or food.
- **show_score()**: It simply shows the score at the given pos according to the color, font and size. 
- **update_screen()**: In the above functions we have only specified or updated the positions of the various objects/surfaces. Here we draw them on the screen.
- **game_over()**: Its the function to call in the end. It should write game over on the screen, show your score(Use **show_score()** function, wait for 3 seconds and then exit
After completing these functions, you will have to complete the main *while* loop which will involve calls to these functions. 

The descriptions of functions as well as the way variables have been intialized can give hints to how you are supposed to proceed. However these are just to guide you, in the end its all upto you. If you think any other method works use that approach.

After finshing your game should look somewhat like this:

<p align = 'center'>
<img src = 'https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/snake.gif'>
</p>

### Flappy Bird
For those of you looking to make a bit more advanced game can work on this. You will be making the classic flappy bird game. The basic outline of the code along with some initializations has been provided in the file [flappy.py](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/flappy.py). The images given in [flappy_assets](https://github.com/Karrthik-Arya/TSS-2021/tree/main/Python%20%26%20its%20Applications/Week-3/flappy_assets) folder have been used. You will haave to complete the functions given in the file and some part of the main while loop. Appropriate descriptions of what the functions are supposed to do have been given in the file.

After finshing your game should somewhat look like this:
<p align='center'>
<img src = 'https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/flappy.gif'>
 </p>

### Solutions to the assignments
You can find the solution for the snake assignment [here](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/snake_solutions.py) and for the flappy bird assignment [here](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-3/flappy_solutions.py).

