from src import guess_languages
from tests import *

if __name__ == '__main__':
    lan = guess_languages(txt_swedish)
    print("The language of the text is :", lan)