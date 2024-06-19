#defining main for the main code
def main():
# define emoji and ask user for the input needed, with emonji
    define_emonji = input("Type something with emonji")
# checking if the sentence ends with the :), hence replacing the emonji with intended emonji
#if not adding the condition needed for frown face emonji.
    print(define_emonji.replace(":)","🙂").replace(":(","🙁"))

main()







