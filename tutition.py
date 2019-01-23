#Dennis Ho

tuition = 8000
interest = .03

for i in range(5):
  tuition = tuition * interest + tuition
  print("Year", i + 1, "tuition is", format(tuition, ".2f"))
