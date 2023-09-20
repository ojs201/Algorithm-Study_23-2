def solution(s):
    words = s.split(" ")
    new_words = []
    for word in words:
        new_words.append(word.capitalize())
    return ' '.join(new_words)