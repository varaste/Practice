def fileWordsCount():
    wordsFile = open("file.txt", "r")
    wordsFileList = wordsFile.read().split(" ")
    print(len(wordsFileList))
    print(wordsFile.read())
fileWordsCount()