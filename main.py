from languages import guess_languages

if __name__ == '__main__':
    txt = "Svenskar älskar sitt kaffe. Det kommer vara lätt att hitta ett fik att köpa en färsk kopp kaffe för det finns kaféer överallt i de stora städerna i Sverige."
    lan = guess_languages(txt)
    print("The language of the text is :", lan)