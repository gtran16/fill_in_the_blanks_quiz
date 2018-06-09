easy_questions = [
    '''We write code to tell the (1)_____ what to do. In this course we write code in (2)_____, which has its own (3)_____, just like a native language such as English or Mandarin. To write a good (4)_____ we must give the computer a very precise set of instructions, which is our code.
    '''
]

easy_answers = [ "computer", "python", "syntax", "program"]

blank_list = ["(1)_____", "(2)_____", "(3)_____", "(4)_____"]

level_index = 0

# def play_level(level_index)

#still need choose game difficulty + max guesses here

def test_for_blank(level_paragraph):
    if level_paragraph.find("(") >= 0:
        return True
    else:
        return False

def replace_blank(user_guess):
    user_answer = []
    split_level_paragraph = easy_questions[level_index].split(" ")
    for word in split_level_paragraph:
        if word == blank:
            word = word.replace(word, user_guess)
            user_answer.append(word)
        else:
            user_answer.append(word)
    user_answer = " ".join(user_answer)
    print user_answer

level_paragraph = easy_questions[level_index]

guesses = 0
guesses_allowed = 5

for level in easy_questions:
    while test_for_blank(level_paragraph) == True and guesses < guesses_allowed:
        blank_start = level_paragraph.find("(")
        blank_end = blank_start + 8
        blank = level_paragraph[blank_start:blank_end]
        answer_index = 0
        user_guess = raw_input("What should replace " + blank + "? ")
        question_answer = easy_answers[answer_index]
        if user_guess.lower() == question_answer:
            replace_blank(user_guess)
        else:
            guesses += 1
            print "Try again." + str(guesses) + "/" + str(guesses_allowed)
    print "next level"
    level_index += 1
#return "You won! Good job!"
