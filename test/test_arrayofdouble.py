

import arrayofdouble as a

a1 = a.ArrayOfDouble(3, 17) # dimension = 3, all values = 17.0
print ("a1 = " + str(a1.display()))

# Change value at index 1
a2 = a1
a2[1] = -3.3
print ("a2 = " + str(a2))

a3 = a.ArrayOfDouble(4) # dimension = 4, uninitialized
print ("a3 has 4 uninitiialized values: " + str(a3))

a4 = a.ArrayOfDouble() # dimension = 0
print ("a4 is uninitialized: " + str(a4))
