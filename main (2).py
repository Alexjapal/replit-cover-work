tally = 0
x = ['hot', 'summer', 'hard', 'dry', 'simple', 'light', 'weak', 'male', 'sad', 'win', 'small', 'ignore', 'buy', 'succeed', 'reject', 'prevent', 'exclude']
y = ['cold', 'winter', 'soft', 'wet', 'complex', 'darkness', 'strong', 'female', 'happy', 'lose', 'big', 'pay fasiattention', 'sell', 'fail', 'accept', 'allow', 'include']
import random
n = random.sample(range(1,16),10)
m = random.sample(range(1,16),10)
for e in range(10):
  print(x[n[e]],"is to",y[n[e]], ", as" ,x[m[e]], "is to ...")
  answer = input("what is the answer ")
  if answer == y[m[e]]:
    print("correct")
    tally = tally + 1
  else:
    print("wrong the answer is", y[m[e]])
print(x)
print("you got", tally,"10")
