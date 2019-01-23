#Dennis Ho

R = int(input("Enter the length of the row in feet: "))
E = int(input("Enter the amount of space used by an end-post assembly in feet: "))
S = int(input("Enter the amount of space between the vines in feet: "))
V = (R-2*E)/S

print("The number of grapevines that will fit in the row will be", V, "feet.") 
