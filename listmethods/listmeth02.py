#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

# Challenge Portion

# example using append, pop, and clear
rainbow = ["red", "yellow", "green", "blue"]

# print to check 
print(rainbow)

# add purple and grey to the rainbow
rainbow.append("purple")
rainbow.append("grey")

# print to check
print(rainbow)

# remove grey and assign it to a variable
rouge_color = rainbow.pop()

# print to check
print(rainbow, rouge_color)

# clear the rainbow
rainbow.clear()

#print to check
print(rainbow)
