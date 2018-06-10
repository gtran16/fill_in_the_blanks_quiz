easy_questions = [
    '''We write code to tell the (1)_____ what to do. In this course we write code in (2)_____, which has its own (3)_____, just like a native language such as English or Mandarin. To write a good (4)_____ we must give the computer a very precise set of instructions, which is our code.
    ''',
    '''We write code to tell the (1)_____ what to do. In this course we write code in (2)_____, which has its own (3)_____, just like a native language such as English or Mandarin. To write a good (4)_____ we must give the computer a very precise set of instructions, which is our code.
    ''',
    '''We write code to tell the (1)_____ what to do. In this course we write code in (2)_____, which has its own (3)_____, just like a native language such as English or Mandarin. To write a good (4)_____ we must give the computer a very precise set of instructions, which is our code.
    ''']

easy_answers = [["computer", "python", "syntax", "program"],
                ["computer", "python", "syntax", "program"],
                ["computer", "python", "syntax", "program"]]

blank_list = ["(1)_____", "(2)_____", "(3)_____", "(4)_____"]

guesses_allowed = 5
quiz_questions = easy_questions
quiz_answers = easy_answers

def test_for_blank(word):
    if word.find("(") >= 0:
        return True
    else:
        return False

def replace_blank(user_guess, level_paragraph):
    index = 0
    for word in level_paragraph:
        if blank in word:
             level_paragraph[index] = word.replace(word, user_guess)
        else:
            index += 1
    level_paragraph = " ".join(level_paragraph)
    user_answer = level_paragraph
    print user_answer



guesses = 0
answer_index = 0

for level in quiz_questions:
    level_index = 0
    level_paragraph = quiz_questions[level_index].split(" ")
    level_answers = quiz_answers[level_index]
    print ' '.join(level_paragraph)
    for word in level_paragraph:
        while test_for_blank(word) == True:
            max_answer_index = 3
            if answer_index > max_answer_index:
                break
            if guesses < guesses_allowed:
                user_answer = []
                blank = blank_list[answer_index]
                question_answer = level_answers[answer_index]
                user_guess = raw_input("What should replace " + blank + "? ")
                if user_guess == question_answer:
                    replace_blank(user_guess, level_paragraph)
                    answer_index += 1
                else:
                    guesses += 1
                    print "Try again." + "\n" +"Guesses: " + str(guesses) + "/" + str(guesses_allowed)
            else:
                print "Game over. :( Study harder."
                break
        level_index += 1
