'''
6.5 Write code using find() and string slicing (see above) to extract
the number at the end of the line below.

text = "X-DSPAM-Confidence:    0.8475";

Convert the extracted value to a floating point number and print it out.
Desired output: 0.8475
'''
# My variables start with: s -> string; i -> integer; f -> float; b -> boolean
text = "X-DSPAM-Confidence:    0.8475"
iAtPos = text.find('0')
sNumber = text[iAtPos : ]
fNumber = float(sNumber)
print (fNumber)
