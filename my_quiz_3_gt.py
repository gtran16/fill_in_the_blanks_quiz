easy_questions = [
    '''We write code to tell the (1)_____ what to do. In this course we write code in (2)_____, which has its own (3)_____, just like a native language such as English or Mandarin. To write a good (4)_____ we must give the computer a very precise set of instructions, which is our code.
    '''
]

easy_answers = [ "computer", "python", "syntax", "program"]

level_index = 0

level_paragraph = easy_questions[level_index]

def play_level(level_index):
    guesses_allowed = 5
    question_number = 0
    number_of_guesses = 0
    blank_start = level_paragraph.find("(")
    blank_end = blank_start + 8
    blank = level_paragraph[blank_start:blank_end]
    while question_number < 4:
        user_guess = raw_input("What should replace " + blank + "?")
        question_answer = easy_answers[question_number]
        if user_guess.lower() == question_answer:
            print "yes"
            user_answer = []
            lvl_question_split = easy_questions[level_index].split(" ")
            for word in lvl_question_split:
                if word == blank:
                    word = word.replace(word, user_guess)
                    user_answer.append(word)
                else:
                    user_answer.append(word)
            user_answer = " ".join(user_answer)
            question_number += 1
            return user_answer
        else:
            number_of_guesses += 1
            return str(number_of_guesses) + "/" + str(guesses_allowed)

######## TESTING ########

print play_level(level_index)

#####
#####
#####
# START! PROMPT USER FOR DIFFICULTY!
#
# define lists based off difficulty (one crazy huge list?)
#
# prompt player to choose how many choices they have per question
#
# play game
#
# level_index = 0
# for level in quiz:
#     play_level(level_index)
#     level_index += 1
