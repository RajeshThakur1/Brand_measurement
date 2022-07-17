s = input("Enter the main string")
sub = input("Enter your sub string")
flag = False
pos = -1
n = len(s)
while True:
  pos = s.find(sub,pos+1, n)
  if pos == -1:
    break

  print("found at position", pos)
  flag= True
if flag == False:
  print("Not Found")