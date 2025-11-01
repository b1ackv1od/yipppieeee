def make_odd_number_list (min_number, max_number):
  number = min_number
  if min_number%2==0:
    number +=1
  odd_list = []
  while number<= Max_number:
    odd_list.append(number)
    number += 2
    return odd_list

print(make_odd_number_list(1,13))
