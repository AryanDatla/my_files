#do-while mimic

i = j = 1

while True:
    while True:
          print(i*'*')
          i += 1
          if i==6:
              break;
    while True:
          print(i*'*')
          i -= 1
          if i==-1:
              break;
    j += 1          
    if j == 3:
        break;
print ("done")