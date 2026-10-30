# Pi Splicer
You've probably heard that every possible combination of numbers is in pi. And if we convert them into letters, you'll be able to find peoples' name, the complete works of William Shakespeare, even your entire life story! its the classic "infinite monkey theorem".
This code does exactly that.

It uses a specified number of digits of pi and splits them into 2 digit segments, 00 being A, 01 being B and so on. 
You input a phrase, sentence or paragraph, that you want to find and it'll search for the string. In theory, every single possible combination of letters should be in this, and searchable with the script! (if the searched string is too long, it may take a very long time to find it)
It was first coded in Python by Rishit, and then translated into js (and heavily optimised) by Nathan. Theres a basic html/css interface to input and output from.

## Usage
Install the python .exe release listed on github and run! enter the digits of pi you would like to evaluate, under 1,000,000 due to processing power limitations, and then the phrase you would like to search. For the JS, you have to manually install the html, css and js folder and locally host it, and follow the instructions included.

watch it working here! https://youtu.be/31ge5brMioM

## Requirements

It uses 10 main libraries, some of which are included with python on install. The rest can be easily installed using pip in the terminal.

~~~
import sys
import time
from colorama import Fore, Style, init
import random
from rich.progress import Progress
from plyer import notification
from win11toast import toast
import winsound
import os
import mpmath
~~~

### Credits

Thanks to Hack Club for organising the YSWS event, [Dyad](https://dyad.hackclub.com/dashboard) , and allowing me to create this, and recieve ***PEAK and Lethal Company!!!***

### AI transparency
I have used minimal amounts of AI within this project, only a few lines which required debugging, and only for things I was too lazy to do, rather than things I didn't know how to do

<img width="1115" height="605" alt="image" src="https://github.com/user-attachments/assets/1905dfe1-e77a-4f91-986c-34554bd9fd7e" />

