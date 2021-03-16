def std_weight(height, gender):
  if gender == "man":
    weight = height/100 * height/100 * 22
    print(f"키 {height}cm 남자의 표준 체중은 {round(weight,2)}kg 입니다.")
  elif gender == "woman" :
    weight = height/100 * height/100 * 21
    print(f"키 {height}cm 여자의 표준 체중은 {round(weight,2)}kg 입니다.")
  else :
    print ("넌 누구냐")


std_weight(175, "man")
std_weight(165, "woman")
std_weight(1.5, "trans")