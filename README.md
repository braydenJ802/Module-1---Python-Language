# Overview

I wrote this small program so that I might increase in my skill as a software engineer. This was my first attempt at using threads. 

This program represents a small fictional race between a group of animals. It uses classes, inheritance, and threading to demonstarate the Python language. 
Every animal object contains a set speed characteristic that determines their starting position in the race. Those positions are then used to determine which threads
execute first, or the order of execution. A thread represents an animal's place in the race, and/or the animal's chance at winning the race.

My hope in writing this software was to get started with using threading. I used the sleep function from the time module to cause the threads to progressively execute more slowly, thus giving a more accurate representation of a race, where the animals are slower and slower.


Feel free to click through this video if you would like, as it is a bit long:

[Software Demo Video](https://youtu.be/9JNOW0TMqAs)


# Development Environment
### Tools
* Microsoft Visual Sudio Code
* Python 3.10.1
* Git 2.34.1
* GitHub

### Libraries
* time
* random 
* threading

# Useful Websites

* [https://www.geeksforgeeks.org/python-call-parent-class-method/](https://www.geeksforgeeks.org/python-call-parent-class-method/)
* [https://careerkarma.com/blog/python-sort-a-dictionary-by-value/](https://careerkarma.com/blog/python-sort-a-dictionary-by-value/)
* [https://realpython.com/intro-to-python-threading/](https://realpython.com/intro-to-python-threading/)
* [https://docs.python.org/3/library/threading.html](https://docs.python.org/3/library/threading.html)

# Future Work
In the future, if I revisited this program, I could:
* Add more animal subclasses
* Allow the user to choose which animals should be in the race
* Add more class attributes to animal subclasses
* Go more in-depth with threading