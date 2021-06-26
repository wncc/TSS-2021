## Functions
Functions are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you’ve defined in a function, you call the name of the function responsible for it. If you need to perform that task multiple times throughout your program, you don't need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function. You’ll find that using functions makes your programs easier to write, read, test, and fix.
You can see [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-1/Functions.ipynb) which covers some details about the functions.  
If you prefer to watch videos to learn you can head over to [this link](https://www.youtube.com/watch?v=1OuRhD7FmTA&list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm&index=12).

## Scope of Variables
The location where we can find a variable and also access it if required is called the scope of a variable. Variables that are defined inside a function body have a local scope, and those defined outside have a global scope. This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions.

If you want to learn more about functions and scope you can visit [this](https://automatetheboringstuff.com/2e/chapter3/) link.

## Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
You can go through [this link]( to learn about recursion and see some implementations of recursion. 

If you prefer to watch videos you can go through [this video](https://www.youtube.com/watch?v=zbfRgC3kukk).

## Modules and Packages
One advantage of functions is the way they separate blocks of code from your main program. By using descriptive names for your functions, your main program will be much easier to follow. You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program.
Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. It also allows you to reuse functions in many different programs. When you store your functions in separate files, you can share those files with other programmers without having to share your entire program. Knowing how to import functions also allows you to use libraries of functions that other programmers have written.

You can go through [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-1/Modules_and_Packages.ipynb) to learn about modules and packages.

## Classes and Objects
**Object-oriented programming** is one of the most effective approaches to writing software. In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes. You can think of a class as a collection of many different functions and attributes (variables) that can be accessed by an object of that class. These methods inside a class are defined almost in the same way normal Python functions are defined, with a major difference being the '_self_' argument and some special methods only found in a class body, for example:- the '_\_\_init___' method, '_\_\_add___' method, etc.

When you write a class, you define the general behavior that a whole category of objects can have. When you create individual objects from the class, each object is automatically equipped with this general behavior; you can then give each object whatever unique traits you desire.

Making an object from a class is called _instantiation_, and you work with _instances_ of a class. You’ll specify the kind of information that can be stored in instances, and you’ll define the actions that can be taken with these _instances_.

You can visit [this notebook](https://github.com/Karrthik-Arya/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-1/Classes.ipynb) to learn about classes and objects.   
You can also go through [this video](https://www.youtube.com/watch?v=jQiUOV15IRI&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt&index=2).

## Some Standard libraries of python

In python, a collection of predefined modules and packages is called a library. There are a lot of useful and interesting libraries available in python. Using such libraries often helps in reducing the effort and saves time in a number of places. Here, we will learn about some of the standard library modules:

_Note: Don’t forget to first import the module using statements like “import math” which was covered in modules and packages!!!!_ 
- The math Library: Python has a built-in module that you can use for mathematical tasks.The math module has a set of methods and constants. Some of these methods often come in handy. You go to [this](https://docs.python.org/3/library/math.html) link to learn about the methods and constants in the math module. It's beneficial to know about some of the basic trigonometric, exponential, logarithmic functions and some numeric ones like factorial, fabs, floor, ceil etc. They are used quite frequently.  
- The random library:  This module implements pseudo-random number generators for various distributions. Some of the functions that you should be familiar with are seed(), randrange(), randint(), choice(), choices(), sample(), random(), uniform(). You head over to [this](https://docs.python.org/3/library/random.html) link to learn about this library.
- The time library: This module provides various time-related functions. You should know about the terms epoch, seconds since epoch, local time, UTC, struct_time and also  about functions used in conversions from struct_time to seconds since epoch etc. You can head over to [this](https://realpython.com/python-time-module/) link and learn about these. 
- The datetime library:  The datetime module supplies classes for manipulating dates and times.You should have a basic idea about creating a date and datetime objects and know about some of the methods. You can head over to [this](https://www.geeksforgeeks.org/python-datetime-module-with-examples/) link to learn about them. 

Important thing to note here is you don’t really need to remember all of these functions/methods. Instead you should just be familiar with the module, know about what kind of methods and constants are there in it. Whenever you are working and need to use any function/method from a module but don’t remember the exact syntax you can just head over to that module’s documentation.


## Assignment

You should now be able to complete the snippet of code designed to read a particular piece of text and answer user's queries about certain words by printing the context in which these words appeared in the text. You can find it as a Jupyter Notebook [here](https://github.com/thevaliantthird/Python-TSS/blob/main/Week1/AssignmentForSnippetCompletion.ipynb).

**Optional Assignment** : Think Completing the Snippet was a piece of cake for you? Learn about the Goodstein Function from [here](https://en.wikipedia.org/wiki/Goodstein%27s_theorem#Goodstein_sequences), then try to implement a function which calculates the the kth term of G(m). 

We will upload the solutions to both Assignments after this week!


