# def profile(name, age, main_lang):
#   print(f"이름 : {name}\t나이 : {age}\t주 사용 언어: {main_lang}")


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age=17, main_lang="파이썬"):
  print(f"이름 : {name}\t나이 : {age}\t주 사용 언어: {main_lang}")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#   print(f"이름 : {name}\t나이 : {age}\t", end="")
#   print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
  print(f"이름 : {name}\t나이 : {age}\t", end=" ")
  for lang in language:
    print(lang, end=" ")
  print()

gun = 10

def checkpoint(soldiers): #경계근무
  global gun #전역 공간에 있는 gun 사용
  gun = gun - soldiers
  print(f"[함수 내] 남은 총 : {gun}")

def checkpoint_ret(gun, soldiers):
  gun = gun - soldiers
  print(f"[함수 내] 남은 총 : {gun}")
  return gun

print(f"전체 총 : {gun}")
# checkpoint(2)
gun = checkpoint_ret(gun,2)
print(f"남은 총 : {gun}")

profile("유재석",20,"python","java","c","c++","c#") 
profile("김태호",25,"python","java") 

profile("유재석")
profile("김태호")