# Custom encoder:
# Write a function called "custom_encoder" that accepts a string text as parameter and for each char of the text it calculates its 0-based position in the following reference string:
# reference_string = 'abcdefghijklmnopqrstuvwxyz'
# The function should return a list that contains all the positions. If a char is not found in the reference_string, its position should be -1

def custom_encoder(text):                                   # [a, b, c, d, e, f, g, h, i, j, k,  l,  m,  n,  o,  p,  q,  r,  s,  t,  u,  v,  w,  x,  y,  z ] المرجع للنص وقيمته ك رقم
    reference_string = 'abcdefghijklmnopqrstuvwxyz'         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] .find() will return the number of the char position

    result = []

    for char in text:
        position = reference_string.find(char.lower())
        result.append(position)
    return result 

print(custom_encoder('My house is beautiful'))
print(custom_encoder('Test!'))
print(custom_encoder(''))	
print(custom_encoder('ä'))