easy_questions = [
    '''We write code to tell the (1)_____ what to do. In this course we write code in (2)_____, which has its own (3)_____, just like a native language such as English or Mandarin. To write a good (4)_____ we must give the computer a very precise set of instructions, which is our code.
    '''
]

easy_answers = [ "computer", "python", "syntax", "program"]

blank_list = ["(1)_____", "(2)_____", "(3)_____", "(4)_____"]

level_index = 0
level_paragraph = easy_questions[level_index]
split_level_paragraph = easy_questions[level_index].split(" ")
guesses_allowed = 5
guesses = 0
answer_index = 0

def test_for_blank(word):
    if word.find("(") >= 0:
        return True
    else:
        return False

def replace_blank(user_guess, split_level_paragraph):
    user_answer = []
    for word in split_level_paragraph:
        if blank in word:
            word = word.replace(word, user_guess)
            user_answer.append(word)
        else:
            user_answer.append(word)
    user_answer = " ".join(user_answer)
    print user_answer

print level_paragraph + "\n"

for word in split_level_paragraph:
    while test_for_blank(word) == True:
        if guesses < guesses_allowed:
            blank = blank_list[answer_index]
            question_answer = easy_answers[answer_index]
            user_guess = raw_input("What should replace " + blank + "? ")
            if user_guess == question_answer:
                replace_blank(user_guess, split_level_paragraph)
                answer_index += 1
            else:
                guesses += 1
                print "Try again." + str(guesses) + "/" + str(guesses_allowed)
        else:
            print "Game over. Study harder."
            break
    level_index += 1
