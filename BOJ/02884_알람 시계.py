hour, minute = input().split()
hour, minute = int(hour), int(minute)

if minute<45:
  hour -= 1
  if(hour<0):
    hour = 23
  minute = minute + 15
else:
  minute -= 45

print(hour, minute)
