# SI 507 - Lab Assignment 3
This week we will practise using regular expressions.

#### Objectives
* Use regular expressions
* Revise Git commands

We are reusing most of a lab assignment developed by Prof. Susan Rodgers at Duke University. See http://www.cs.duke.edu/courses/compsci101/fall16/labs/lab11/ for original.

Week 3 Lab Assignment Goals
● Use regular expressions1
● Revise Git commands
Step 1 : Create a GitHub repository
● Go to
https://classroom.github.com/assignment-invitations/12785d7afd8ed6ea5e131a5a8b30b
ff4
● Accept the assignment invite
Step 2 : Get starter code onto your machine
● Like last week, clone the assignment repository onto your machine
● ‘cd’ to the cloned directory
Step 3 : Regular Expressions - Part 1
● part1.py accepts regular expressions and prints the list of words from ‘words.txt’ that match the expression. Type Ctrl+C to exit the program.
● Answerthefollowingquestionsusingpart1.pyandr​egexdocumentation.​
● Enter your answers in ‘part1_answers.txt’
1. How many words end in the letter ‘a’?
2. The regex [aeiou]$ indicates there are 6988 words that end with a vowel. How
many words start and end with a vowel?
3. How many words start and end with the same vowel? Extreme and aorta are two
such words.
4. The words obsequious and pharmacopoeia each contain four vowels in a row.
How many words contain four consecutive vowels?
Step 4 : Regular Expressions - Part 2
● Look at littlebrother.txt. We will be using this file in this section. If you are running into an encoding error when opening the file, use: f​ = open('littlebrother.txt', encoding = "ISO-8859-1")
● Create a separate file part2.py, and write code to:
1. Calculate how many web sites start with ‘http:’ are in littlebrother.txt.
2. Calculate how many words in littlebrother.txt have a number in them (examples:
68, 6A, word2).
3. Calculate how many numbers are in littlebrother.txt (Don't count words that have
any symbols that are not digits. 456 is good, but 786-3452 and 6A would not
count)
4. Calculate how many words in littlebrother.txt have at least one digit and at least
one letter (examples: 63A, word26).
● Enter your answers into part2_answers.txt
Step 5 : Commit your changes
● Commit and push all your changes to the remote repository
