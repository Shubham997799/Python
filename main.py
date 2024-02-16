Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def check_spell(correct_word, contest_word):
    if len(correct_word) != len(contest_word):
        return "WRONG"

    count_wrong = 0

    for a, b in zip(correct_word, contest_word):
        if a != b:
            count_wrong += 1

        if count_wrong > 2:
            return "CORRECT"

    return "ALMOST CORRECT"

def main():
    correct_word = input("Enter the correct word: ")
    contest_word = input("Enter the contest word: ")

    result = check_spell(correct_word, contest_word)
    print(f"The contest word '{contest_word}' is {result}.")

main()