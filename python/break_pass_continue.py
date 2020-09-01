number = 0
for number in range(8):
    #if number == 5:
      #  break
    #print(number)
   # if number > 5:
    #    continue
    #print(number)
    if number%2 == 0:
        pass
    else:
        print(number)



nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)



nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)


nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        pass
    else:
        print(num)
