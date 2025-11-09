def main(stringinquestion : str) -> bool:
    brackets_dictionary = { ")": "(",  "]": "["}
    brackets_stack = []

    for char in stringinquestion:
        if char in brackets_dictionary.values():
           brackets_stack.append(char)
        if char in brackets_dictionary.keys():
            if brackets_stack:
                if brackets_stack.pop() != brackets_dictionary[char]:
                    return False
            else:
                return False

    return not brackets_stack

if __name__ == "__main__":
    main("hello[]")
