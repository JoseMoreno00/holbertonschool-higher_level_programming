#!/usr/bin/python3
def multiple_returns(sentence):
    size_sentence = len(sentence)
    if size_sentence == 0:
        return 0, "None"
    else:
        return size_sentence, sentence[0]
