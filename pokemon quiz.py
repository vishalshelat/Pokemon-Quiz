Python 3.6.3 |Anaconda custom (64-bit)| (default, Nov  8 2017, 15:10:56) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print('welcome to the Pokemon Multiple choice test\n')
welcome to the Pokemon Multiple choice test

>>> name = input ('What is your name?')
What is your name?curry
>>> print ('\nHi there' + name+ '!' Let''s Play a game!\n')
  File "<stdin>", line 1
    print ('\nHi there' + name+ '!' Let''s Play a game!\n')
                                      ^
SyntaxError: invalid syntax
>>> print ('\nHi there' + name+ '!' Let's Play a game!\n')
  File "<stdin>", line 1
    print ('\nHi there' + name+ '!' Let's Play a game!\n')
                                      ^
SyntaxError: invalid syntax
>>> print ('\nHI THERE ' + name + '! LET''S PLAY A GAME!\n')

HI THERE curry! LETS PLAY A GAME!

>>> print (' I will ask you 10 questions and give you three choices for each question. \n\n You select which choice is the correct answer\n')
 I will ask you 10 questions and give you three choices for each question.

 You select which choice is the correct answer

>>> print (' I will ask you 10 questions and give you three choices for each question. \n\n You select which choice is the correct answer\n')
 I will ask you 10 questions and give you three choices for each question.

 You select which choice is the correct answer

>>> print('\n-----------------------------------------------------------------\n')

-----------------------------------------------------------------

>>> score = 0
>>> score = int(score) #convert the 0 into a number so we can add scores
>>> print("question 1: what stat influeced critical strike chance in generation 1?\n")
question 1: what stat influeced critical strike chance in generation 1?

>>> print('A. Attack')
A. Attack
>>> print('B. Speed')
B. Speed
>>> print('C. Evasivness')
C. Evasivness
>>> Q1answer = "B,b"
>>> Q1response = input('Your Answer: ')
Your Answer: B
>>> if Q1response != Q1answer):
  File "<stdin>", line 1
    if Q1response != Q1answer):
                             ^
SyntaxError: invalid syntax
>>> if Q1response != Q1answer)
  File "<stdin>", line 1
    if Q1response != Q1answer)
                             ^
SyntaxError: invalid syntax
>>> if (Q1response != Q1answer):
... print('Sorry, that is incorrect!')
  File "<stdin>", line 2
    print('Sorry, that is incorrect!')
        ^
IndentationError: expected an indented block
>>> print ('Sorry, that is incorrect!')
Sorry, that is incorrect!
>>> else:
  File "<stdin>", line 1
    else:
       ^
SyntaxError: invalid syntax
>>> else
  File "<stdin>", line 1
    else
       ^
SyntaxError: invalid syntax
>>> else:
  File "<stdin>", line 1
    else:
       ^
SyntaxError: invalid syntax
>>> else:
  File "<stdin>", line 1
    else:
       ^
SyntaxError: invalid syntax
>>>     print ('Well done! ' + Q1response + ' is correct!')
  File "<stdin>", line 1
    print ('Well done! ' + Q1response + ' is correct!')
    ^
IndentationError: unexpected indent
>>>     score = score + 1
  File "<stdin>", line 1
    score = score + 1
    ^
IndentationError: unexpected indent
>>> score = score + 1
>>> q1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'q1' is not defined
>>> Q1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Q1' is not defined
>>>