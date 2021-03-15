def up_str(string):
    print(string.upper())

# up_str("hello world")
# up_str("Practice makes perfect")


def delete_str (string):
    word_list = string.split(" ")
    word_list = sorted(word_list)
    deleted = sorted(set(word_list))
    print(list(deleted))

delete_str("hello world and pricate makes perfect and hello world again")




