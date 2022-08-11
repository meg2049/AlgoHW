# unique character in string

def unique(string):
    for i in range(len(string)):
      for j in range(i + 1, len(string)):
    if(string[i] == string[j]):
        return False
    return True

string = 'aabcde'
if(unique(string)):
  print(True)
else:
  print(False)






