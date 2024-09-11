from src import guess_languages
from tests import *

if __name__ == '__main__':
    txt = input("Enter the text: ")
    lan = guess_languages(txt)
    print("The language of the text is :", lan)