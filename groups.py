class teach_groups:
  intro = "A group is a set on which there is a binary operation. An operation on two elements of a set that results in an element of the same set forms an algebra over that set"
  
  q1 = input("Which of the following doesn't form an algebra over R? A: multiplication B: exponentiation C: addition D: integration with respect to x") 
  
  if q1 == "B":
    print("Correct!")
  else:
    print("Incorrect! The correct answer is B, since raising any negative number to the one half power results in an imaginary number, which is not an element of the real numbers")
