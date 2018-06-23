# The following lists represent the quiz questions and quiz answers depending on the difficulty the user chooses.
# Each difficulty has three levels with four blanks each. The user gueses and answer, and if the answer is correct, the blank is replaced with the correct answer.

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

# Represents the blank spaces in the questions. It's used for strings to present to the user in the answer_question function.
blank_list = ["(1)_____", "(2)_____", "(3)_____", "(4)_____"]

# Prompts the user to choose a quiz difficulty, then gets the appropriate quiz questions and quiz answers. If the user chooses a wrong difficulty, it reprompts the user to choose again.
# Passes along the quiz_questions and quiz_answers to the choose_guesses_allowed function so that the start_game function has the appropriate access to the variables.
def choose_difficulty():
    user_difficulty = raw_input("Easy, medium, or hard? ")
    if user_difficulty.lower() == "easy":
        quiz_questions = easy_questions
        quiz_answers = easy_answers
    elif user_difficulty.lower() == "medium":
        quiz_questions = medium_questions
        quiz_answers = medium_answers
    elif user_difficulty.lower() == "hard":
        quiz_questions = hard_questions
        quiz_answers = hard_answers
    else:
        print "Try again."
        choose_difficulty()
    choose_guesses_allowed(quiz_questions, quiz_answers)

# Prompts the user to choose the number of guesses they get per questionself.
# Takes quiz_questions and quiz_answers as inputs to pass to the start_game function so it has access to these variables. Also passes its output, guesses_allowed, to the start_game function.
def choose_guesses_allowed(quiz_questions, quiz_answers):
    guesses_allowed = raw_input("Choose how many guesses you get per question per level. Be sure to enter a positive integer. ")
    if check_for_integer(int(guesses_allowed)) == True:
        print "You'll have " + guesses_allowed + " guesses per question."
    else:
        print "Enter a positive integer."
        choose_guesses_allowed(quiz_questions, quiz_answers)
    start_game(quiz_questions, quiz_answers, guesses_allowed)

# Ensures that the users enters an appropriate value for guesses_allowed in the function choose_guesses_allowed.
# It's necessary because raw_input is always a string type, which means users were previously able to enter anything such as "apple" and start counting 1/apple, which made no sense.
def check_for_integer(guesses_allowed):
    try:
        int(guesses_allowed)
    except ValueError:
        return False
    else:
        return True

# After the user has chosen their difficulty and their guesses allowed, this function takes the quiz_questions, quiz_answers, and guesses_allowed to start the real part of the game, the quiz!
# This function iterates through each level in the relevant quiz_questions, setting the level_index which determines the level_paragraph and level_answers.
# Passes level_paragraph, level_answers, and guesses_allowed to the play_level function.
# Once the game is done, this function gives the user the option to play again.
def start_game(quiz_questions, quiz_answers, guesses_allowed):
    level_index = 0
    for level in quiz_questions:
        level_paragraph = quiz_questions[level_index].split(" ")
        level_answers = quiz_answers[level_index]
        print quiz_questions[level_index]
        play_level(level_paragraph, level_answers, guesses_allowed)
        level_index += 1
    print "You won! You're so smart! :D\n" #End of game if the user wins
    play_again = raw_input("Do you want to play again?")
    if play_again.lower() == "yes":
        choose_difficulty()
    else:
        return "Have a nice day!"

# Takes the level_paragraph, level_answers, and guesses_allowed from the start_game function and iterates through each word in the level_paragraph.
# Also sets the guesses, which represent current guesses, as well as the answer_index and max_answer_index for the answer_question function.
# Passes answer_index, max_answer_index, gueses, guesses_allowed, level_paragraph, level_answers, and word to the answer_question function.
def play_level (level_paragraph, level_answers, guesses_allowed):
    for word in level_paragraph:
        guesses = 0
        guesses_allowed = int(guesses_allowed)
        answer_index = 0
        max_answer_index = 3
        answer_question (answer_index, max_answer_index, guesses, guesses_allowed, level_paragraph, level_answers, word)

# Takes answer_index, max_answer_index, gueses, guesses_allowed, level_paragraph, level_answers, and word to answer the current question.
# Checks for a blank in the word.
# Checks to ensure guesses is less than guesses_allowed
# prompts the user to answer the question
# if the users answer the quesiton correctly, calls the replace_blank function to replace the blank in the level_paragraph, then goes to the next question
# otherwise, it adds a guess to guesses / guesses_allowed. prints Try again with guesses / guesses_allowed until the user is out of guesses.
def answer_question (answer_index, max_answer_index, guesses, guesses_allowed, level_paragraph, level_answers, word):
    while word.find("_____") > 0: # this tests for a blank. it looks for the _____ space in the word. If it's there, then it is greater than 0 and the loop proceeds
        if answer_index > max_answer_index:
            break
        blank = blank_list[answer_index]
        user_answer = []
        question_answer = level_answers[answer_index]
        if guesses < guesses_allowed:
            user_guess = raw_input("What should replace " + blank + "? ")
            if user_guess.lower() == question_answer:
                replace_blank(user_guess, level_paragraph, user_answer, blank)
                answer_index += 1
            else:
                guesses += 1
                print "\nTry again. " + str(guesses) + "/" + str(guesses_allowed) + "\n"
        else:
            return "You lost! Study harder."

# Replaces the blank space in the paragraph with the user's guess in the level_paragraph.
# Keeps track of the user's complete answer in the user_answer variable from level to level.
# Prints the user's answer for them to see.
def replace_blank(user_guess, level_paragraph, user_answer, blank):
    index = 0
    for word in level_paragraph:
        if blank in word:
             level_paragraph[index] = word.replace(word, user_guess)
        else:
            index += 1
    level_paragraph = " ".join(level_paragraph)
    user_answer = level_paragraph
    print "\nCorrect!\n" + user_answer

#################################################################
#                                                               #
#                           START GAME                          #
#                                                               #
#################################################################

print '''
|--------------------------------------------|
|          PYTHON STUDY REVIEW QUIZ          |
|--------------------------------------------|
'''
choose_difficulty()
