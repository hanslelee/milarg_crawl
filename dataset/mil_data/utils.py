def eraseSpace(sentence):
    text1 = sentence.replace("\n", "")
    text2 = text1.replace("\r", "")
    result = text2.replace("\t", "")

    return result