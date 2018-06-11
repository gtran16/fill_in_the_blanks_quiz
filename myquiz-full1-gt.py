easy_questions = [
    #LVL E-1
    '''\nLEVEL ONE:\nWe write code to tell the (1)_____ what to do. In this course we write code in (2)_____, which has its own (3)_____, just like a native language such as English or Mandarin. To write a good (4)_____ we must give the computer a very precise set of instructions, which is our code.
    ''',
    #LVL E-2
    '''\nLEVEL TWO:\nWe can run Python code using a (1)_____, like Sublime or Atom. We can also run Python code using a (2)_____. When you open a CLI, you enter a (3)_____, where you can type a (4)_____ and hit RETURN to tell the computer what to do or navigate through the computer.
    ''',
    #LVL E-3
    '''\nLEVEL THREE:\nIn the CLI, the (1)_____ command outputs the absolute path to where you are in the computer's file structure. In other words, it shows you where home is. (2)_____ shows the contents of a directory, while (3)_____ is for changing your home location to another directry. You can even create files with the (4)_____ command.
    ''']

easy_answers = [["computer", "python", "syntax", "program"],
                ["text editor", "command line interface", "shell", "command"],
                ["pwd", "ls", "cd", "touch"]]

medium_questions = [
    #LVL M-1
    '''\nLEVEL ONE:\nProgramming is the core of (1)_____. A program tells a (2)_____ what to do. In fact, a computer can is a universal machine that can be programmed to run any (3)_____. Python is just one (4)_____ you can write programs in.
    ''',
    #LVL M-2
    '''\nLEVEL TWO:\nYou assign values to different (1)_____, a key component of programming. For instance, in the statement 'myCat = 'Logan'', (2)_____ is the variable and (3)_____ is the value. Variables are not only a key part of programming, they can also make your code more (4)_____ if named wisely.
    ''',
    #LVL M-3
    '''\nLEVEL THREE:\nIn Python, a sequence of characters surrounded by quotes is a (1)_____. You can use either single or double quotes to create one, but you should be (2)_____. You can (3)_____ a string to select a (4)_____, which can be helpful for splitting strings.
    ''']

medium_answers = [["computer science", "computer", "computation", "language"],
                ["variables", "mycat", "logan", "usable"],
                ["string", "consistent", "index", "substring"]]

hard_questions = [
    #LVL H-1
    '''\nLEVEL ONE:\nPython is a (1)_____ language that gets (2)_____ by the Python program to run the code. A key rule in Python is that the first character on each line cannot be a (3)_____. The Python program has its own (4)_____ because it needs a very strict, precise set of instructions that could be easily misinterpreted in a natural language such as English or Mandarin.
    ''',
    #LVL H-2
    '''\nLEVEL TWO:\nIn Python, you can create (1)_____, or procedures, to run a set of instructions. The instructions can include anything from a simple print statement, to more complex code such as (2)_____, which only run a set of instructions if the given condition is true. To write these conditions, it's useful to use (3)_____, such as <, >, ==, !=, and so on. Functions can also contain (4)_____, which repeat a a set of instructions.
    ''',
    #LVL H-3
    '''\nLEVEL THREE:\nThere are two different types of loops: (1)_____, which repeat a set of instructions until the condition is no longer true or there is a break, and (2)_____, which iterate through each item in a list until the end of the list. When you write a loop statement, you want to avoid an (3)_____ loop, which is most common in while loops. To avoid this, it's best to either use a for loop or add a (4)_____ variable to end the loop at a reasonable time.
    ''']

hard_answers = [["high-level", "interpreted", "space", "syntax"],
                ["functions", "if statements", "operators", "loops"],
                ["while loops", "for loops", "infinite", "count"]]

blank_list = ["(1)_____", "(2)_____", "(3)_____", "(4)_____"]
difficulty_options = ["easy", "medium", "hard"]

# DOESNT GENERATE OR CHANGE LISTS AS DESIRED
# def get_quiz(user_difficulty):
#     if user_difficulty.lower() == "easy":
#         quiz_questions = easy_questions
#         quiz_answers = easy_answers
#         return quiz_questions and quiz_answers
#     if user_difficulty.lower() == "medium":
#         quiz_questions = medium_questions
#         quiz_answers = medium_answers
#         return quiz_questions and quiz_answers
#     if user_difficulty.lower() == "hard":
#         quiz_questions = hard_questions
#         quiz_answers = hard_answers
#         return quiz_questions and quiz_answers
#
# BOTH OF THESE DON'T LOOP OR EVEN CHECK FOR THE COUNTER FOR SOME REASON? AM I MISUNDERSTANDING WHILE LOOPS?
# validity_check = 0
# def choose_difficulty(validity_check):
#     while validity_check = 0:
#         user_difficulty = raw_input("Easy, medium, or hard? ")
#         if user_difficulty.lower() in difficulty_options:
#             get_quiz(user_difficulty)
#             validity_check += 1
#         else:
#             print "Try again."
#
# def guesses_allowed(validity_check):
#     while validity_check = 0:
#         guesses_allowed = raw_input("Choose how many guesses you get per question/level before you lose. Be sure to enter a positive integer. ")
#         if guesses_allowed.isdigit() == True and guesses_allowed > 0:
#             print "You'll have " + str(guesses_allowed) + " guesses per level."
#             validity_check += 1
#         else:
#             print "Enter a positive integer."
#             guesses_allowed = raw_input("Choose how many guesses you get per question/level before you lose. Be sure to enter a positive integer. ")


def replace_blank(user_guess, level_paragraph):
    index = 0
    for word in level_paragraph:
        if blank in word:
             level_paragraph[index] = word.replace(word, user_guess)
        else:
            index += 1
    level_paragraph = " ".join(level_paragraph)
    user_answer = level_paragraph
    print "\nCorrect!\n" + user_answer

def test_for_blank(word):
    if word.find("(") >= 0:
        return True
    else:
        return False

# DOESNT WORK -- CANT ACCESS VARIABLES -- answer_index, guesses, blank..
# def play_level(level_index):
#     for word in level_paragraph:
#         while test_for_blank(word) == True:
#             max_answer_index = 3
#             if answer_index > max_answer_index:
#                 break
#             if guesses < guesses_allowed:
#                 user_answer = []
#                 blank = blank_list[answer_index]
#                 question_answer = level_answers[answer_index]
#                 user_guess = raw_input("What should replace " + blank + "? ")
#                 if user_guess == question_answer:
#                     replace_blank(user_guess, level_paragraph)
#                     answer_index += 1
#                 else:
#                     guesses += 1
#                     print "Try again." + "\n" +"Guesses: " + str(guesses) + "/" + str(guesses_allowed)
#             else:
#                 print "Game over. :( Study harder."
#                 break

#################################################################
#                                                               #
#                           START GAME                          #
#                                                               #
#################################################################
quiz_questions = []
quiz_answers = []
#opener
print '''
|--------------------------------------------|
|          PYTHON STUDY REVIEW QUIZ          |
|--------------------------------------------|
'''

#quiz difficulty prompt -- CANT GET THIS TO LOOP IN WHILE LOOP TO REPROMPT IF ANSWER IS WRONG
user_difficulty = raw_input("Easy, medium, or hard? ")
if user_difficulty.lower() in difficulty_options:
    if user_difficulty.lower() == "easy":
        quiz_questions = easy_questions
        quiz_answers = easy_answers
    if user_difficulty.lower() == "medium":
        quiz_questions = medium_questions
        quiz_answers = medium_answers
    if user_difficulty.lower() == "hard":
        quiz_questions = hard_questions
        quiz_answers = hard_answers
# else: -- does nothing to reassign currently.
#     print "Try again."
#     user_difficulty = raw_input("Easy, medium, or hard? ")


#prompt user to choose guessed allowed -- CANT GET THIS TO LOOP IN WHILE LOOP TO REPROMPT IF ANSWER IS WRONG
guesses_allowed = raw_input("Choose how many guesses you get per level before you lose. Be sure to enter a positive integer. ")
if guesses_allowed > 0:
    print "You'll have " + str(guesses_allowed) + " guesses per qustion."
else:
    print "Enter a positive integer."
    guesses_allowed = raw_input("Choose how many guesses you get per level before you lose. Be sure to enter a positive integer. ")

max_answer_index = 3
level_index = 0
level_paragraph = quiz_questions[level_index].split(" ")
level_answers = quiz_answers[level_index]

#START GAME! (23-line function. anytime i break into helper functions, i lose access to key variables...)
for level in quiz_questions:
    print ' '.join(level_paragraph)
    answer_index = 0
    #START LEVEL!
    for word in level_paragraph:
        guesses = 0
        while test_for_blank(word) == True:
            #BREAKS IF LEVEL IS FINISHED (for some reason, for loop doesn't end this while loop, the level is complete.)
            if answer_index > max_answer_index:
                break
            blank = blank_list[answer_index]
            user_answer = [] #keeps track of user answer as it goes
            question_answer = level_answers[answer_index]
            if guesses < guesses_allowed: #THIS DOESNT SEEM TO STOP MY LOOP AT ALL =[
                #ANSWER QUETION!
                user_guess = raw_input("What should replace " + blank + "? ")
                if user_guess.lower() == question_answer:
                    replace_blank(user_guess, level_paragraph)
                    answer_index += 1
                else:
                    guesses += 1
                    print "\nTry again. " + str(guesses) + "/" + str(guesses_allowed) + "\n"
            else: # DOESNT BREAK LOOP BASED OFF CONDITION =[
                #END OF GAME IF YOU RAN OUT OF GUESSES.
                print "You lost! Study harder."
                break
    level_index += 1

#END OF GAME IF YOU WON!
print "You won! You're so smart! :D"
