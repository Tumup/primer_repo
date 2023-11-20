def stringy(size):

  string = ""
  for i in range(size):
      if i%2 == 0:
        string += "1"
      else:
        string += "0"
  return(string)
stringy(6)