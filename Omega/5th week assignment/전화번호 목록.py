phone_books = ["119", "97674223", "1195524421"]

def solution(phone_book):
    answer = True
    phone_book.sort() # 사전순으로 정렬하여 비슷한 부분이 인접하게 만들기
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i + 1]: # 현재 번호가 다음 번호의 접두어인지 확인
            answer = False
    return  answer


