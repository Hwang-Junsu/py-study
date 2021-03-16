import random
client = [_ for _ in range(1,51)]
ride_client = 0

for i in client:
  ride_time = random.randrange(5,51)
  if ride_time < 5 or ride_time > 15:
    print(f"[ ] {i}번째 손님 (소요시간 : {ride_time}분)")
  else:
    print(f"[O] {i}번째 손님 (소요시간 : {ride_time}분)")
    ride_client = ride_client + 1
    
print (f"총 탑승 승객 : {ride_client}분")