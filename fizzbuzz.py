#!/usr/bin/env python3.3

#User defined requirements.
#(These are subject to change.)

count = 100;
to_fizz = 3;
to_buzz = 5;

#Additional requirements. These should be empty data types.
result_array=[];

#Actual code.
for integer in range(1, count + 1):
  result = '';
  if integer % to_fizz == 0:
    result += "FIZZ";
  if integer % to_buzz == 0:
    result += "BUZZ";
  if result == '':
    result += str(integer);
  result_array.append(result);   #If the count is over a million, it may
print("\n".join(result_array));  #be less resource heavy to just print each result instead
                                 #of appending it to an array. (Another option is to write to a file,
                                 #and print that file.)
