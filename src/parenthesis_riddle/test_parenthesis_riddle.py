from .parenthesis_riddle import main

def test_main():
    test_dictionary : dict = {
        "()" : True,
        "[]" : True,
        "()(" : False,
        "1(b)6(7" : False,
        "v(b)n" : True
    }

    for testcase, testresult in test_dictionary.items():
        assert main(testcase) == testresult
