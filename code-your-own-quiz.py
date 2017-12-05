#!/usr/bin/python
# coding=utf-8

"""This is Udacity Code your own quiz project."""
# multiple level of quiz difficulty
# 2 subject quiz. Unable to increase at this time
# User decides how many wrong guesses before they lose
# Quiz type: Fill in the blanks
# Quiz level: 1 ~ 4 with 5 question in each level
import random
# ====Global Variable====
num_question_per_level = 4
# Questions per level
min_number = 1
# Used to specify lowest number for range functions
# Do not add subject on list in this current version
subjects = ["Chemistry", "Geography"]
# Dictionary and keyword for the quiz
# dictionary can be inceased manually to increase quiz level
# Increase by 4 or the num_question_per_level to add 1 level
# Entry for subject Chemistry, max level 5
chemistry_keyword = "chemical symbol"
checmical_symbol = {"Hydrogen": "H",
                    "Helium": "He",
                    "Lithium": "L",
                    "Beryllium": "Be",
                    "Boron": "B",
                    "Carbon": "C",
                    "Nitrogen": "N",
                    "Oxygen": "O",
                    "Fluorine": "F",
                    "Neon": "Ne",
                    "Sodium": "Na",
                    "Magnesium": "Mg",
                    "Aluminium": "Al",
                    "Silicon": "Si",
                    "Phosphorus": "P",
                    "Sulfur": "S",
                    "Chlorine": "Cl",
                    "Argon": "Ar",
                    "Potassium": "K",
                    "Calcium": "Ca"
                    }
# Entry for subject Geography, max level 4
geography_keyword = "capital"
country_capital = {"Australia": "Canberra",
                   "Austria": "Vienna",
                   "Belgium": "Brussels",
                   "Botswana": "Gaborone",
                   "Canada": "Ottawa",
                   "Cyprus": "Nicosia",
                   "Honduras": "Tegucigalpa",
                   "Indonesia": "Jakarta",
                   "Ireland": "Dublin",
                   "Japan": "Tokyo",
                   "North Korea": "Pyongyang",
                   "Latvia": "Riga",
                   "Morocco": "Rabat",
                   "Philippines": "Manila",
                   "Singapore": "Singapore",
                   "Vietnam": "Hanoi"
                   }
generic_question = "What is the {} of "
generic_answer = "{} is the {} of {}"
generic_wrong_answer = "{} is not the {} of {}"
generic_banner = "This is a quiz for {}"
# =======================


def pause(pause_message):
    """Add pause to the quiz with correct message."""
    printbox(pause_message)
    raw_input()


def bar(n, ch="-"):
    """Horizontal bar on text."""
    # lesson 9 udacity
    return ch * n


def printbox(message):
    """Box bar around text."""
    # lesson 9 udacity
    # prints dashes equal to length of variable message
    print "+-" + bar(len(message)) + "-+"
    print "| " + message + " |"
    print "+-" + bar(len(message)) + "-+"


def ask_question(question, target_range):
    """Do ask the generic question and return an integer."""
    # re-use the function to ask question
    # Infinite loop to validates input to required parameter
    while True:
        answer_to_question = raw_input(question)
        # check if input is a digit and within range min-max
        if answer_to_question.isdigit():
            answer_to_question = int(answer_to_question)
            if answer_to_question in range(min_number, target_range):
                return answer_to_question
            else:
                printbox("Out of range, it needs to be less than " + str(target_range))
                # User will need to press enter to re-enter answer to question
                pause("Press Enter to continue....")
        else:
            # Return invalid answer and ask again
            printbox(answer_to_question + " is not a digit")
            pause("Press Enter to continue....")


def quiz_subject(subject_selection):
    """Return the user selected subject."""
    print "Please select subject for the quiz"
    # For visual reference only, counter is initialized
    counter = 0
    # Present the subject in list subjects[]
    for subject in subject_selection:
        counter += 1
        print str(counter) + ". " + subject
    # User input for corresponding digit of the subject
    selected_subject = ask_question("Select subject 1 or 2: ", (len(subject_selection)) + 1)
    return selected_subject - 1


def quiz_settings():
    """Return the quiz level and mistakes allowed."""
    # Defines user preferred quiz level
    # Defines user preferred number of guesses
    print "Choose the quiz level"
    # +1 is for range purpose only
    quiz_level = ask_question("Choose quiz level from " + str(min_number) +
                              " to " + str(max_quiz_level) + " : ", (max_quiz_level + 1))
    print "Total number of question is " + str(num_question_per_level) + " times the quiz difficulty"
    number_of_mistakes = ask_question("How many mistake(s) allowed before the quiz ends? ",
                                      ((num_question_per_level * quiz_level) + 1))
    # Range is multiple of quiz level
    return quiz_level, number_of_mistakes


def create_questions(question_multiplier, generic_pool):
    """Return a random list of dictionary entry."""
    # No duplciate entry allowed
    counter = 0
    while counter < question_multiplier * num_question_per_level:
        # Generate random Countries for questionaire
        add_generic_question = random.sample(generic_pool, 1)
        # Check for duplicate
        if add_generic_question not in generic_question_list:
            generic_question_list.append(add_generic_question)
            counter += 1
    return generic_question_list


def questionaire(generic_question_list, generic_keyword, number_of_mistakes, generic_dictionary):
    """Do present user for a question related to selected subject."""
    # This function has 16 lines but 2 long lines were split to 2 lines
    # Uses the generic question/answer format to present the I/O to user
    # Number of question is dependent on user selected level
    for question_counter in range(0, len(generic_question_list)):
        while True:
            if number_of_mistakes != 0:
                print generic_question.format(generic_keyword) + "".join(generic_question_list[question_counter]) + " ?"
                user_answer = raw_input("Answer: ")
                if check_answer(generic_question_list[question_counter], user_answer, generic_dictionary) is False:
                    # User loses 1 chance
                    number_of_mistakes -= 1
                    # Presents the incorrect answer
                    printbox("Incorrect! " + generic_wrong_answer.format(user_answer.title(), generic_keyword,
                             "".join(generic_question_list[question_counter])))
                    print number_of_mistakes, "more chance(s)"
                else:
                    printbox("Correct! " + generic_answer.format(user_answer.title(), generic_keyword,
                             "".join(generic_question_list[question_counter])))
                    # break the while loop and returns to the first for loop
                    break
            else:
                printbox("Quiz Over")
                # Quiz is terminate program ends
                exit()
    return number_of_mistakes


def check_answer(question_key, user_answer, ref_dictionary):
    """Do check the user input to the dictionary."""
    # Verify user answer is correct compared to quiz dictionary used
    if user_answer.title() == ref_dictionary.get("".join(question_key)):
        return True
    return False


# User selects the subject
selected_quiz_subject = subjects[quiz_subject(subjects)]
# Only 2 subject can be selected in this version
if selected_quiz_subject == "Chemistry":
    max_quiz_level = len(checmical_symbol) / num_question_per_level
    # Sets max selectable quiz level depending of entries in dictionary checmical_symbol
    printbox(generic_banner.format(selected_quiz_subject))
    # Selects the appropritate dictionary
    generic_dictionary = checmical_symbol
    # Sets the generic word for questionaire
    generic_keyword = chemistry_keyword
elif selected_quiz_subject == "Geography":
    max_quiz_level = len(country_capital) / num_question_per_level
    # Sets max selectable quiz level depending of entries in dictionary country_capital
    printbox(generic_banner.format(selected_quiz_subject))
    # Selects the appropritate dictionary
    generic_dictionary = country_capital
    # Sets the generic word for questionaire
    generic_keyword = geography_keyword
# Initiate list for countries during quiz
generic_question_list = []
# Request user to input quiz difficulty and max errors
question_multiplier, number_of_errors = quiz_settings()
# Runs the quiz
grade_of_quiz = number_of_errors - questionaire(create_questions(question_multiplier, generic_dictionary),
                                                generic_keyword, number_of_errors, generic_dictionary)
# it will only reach this point of user mistake did not reach number_of_errors
printbox("Good Job!")
# Gives feedback to user regarding the number of mistakes
printbox(str(grade_of_quiz) + " mistakes made")
