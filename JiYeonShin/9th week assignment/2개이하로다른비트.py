def solution(numbers):
  answer = []
  for number in numbers:
      answer.append(f(number))
  return answer

def f(number):
  if(number%2 == 0): #짝수
      return number+1
  else: #홀수
      bit = numberToBit(number)
      for i in range(len(bit)):
          if(bit[len(bit)-i-1] == '0'):
              bit = bit[:len(bit)-i-1] + "10" + bit[len(bit)-i+1:]
              break
      else: #bit가 싹 다 1
          bit = "10" + bit[1:]
      return bitToNumber(bit)

def numberToBit(number):
  bit = ""
  while(number > 0):
      sware, remain = divmod(number, 2)
      number = sware
      bit = str(remain) + bit
  return bit

def bitToNumber(bit):
  number = 0
  for i in range(len(bit)):
      number += int(bit[len(bit)-1-i])*2**(i)
  return number

#짝수는 무조건 제일 뒤에꺼를 1로 바꾼 수. 즉, 그냥 +1을 한 수
#홀수일 경우 가장 뒤쪽에 있는 0을 1로 바꿔주고 그다음 비트를 0으로 바꿔주면 된다.