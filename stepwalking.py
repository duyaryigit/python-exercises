def StepWalking(num):
  if num == 1:
    return 1
  elif num == 2:
    return 2
  else:
    return StepWalking(num-1) + StepWalking(num-2)
  return num
  
print(StepWalking(int(input()))
