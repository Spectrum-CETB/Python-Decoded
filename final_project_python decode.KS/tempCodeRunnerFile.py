
  elif str=="Exponent":
    print(f'By default {a} is taken as base and {b} is taken to be exponent')
    return a**b 
  elif str=="Logarithm":
    return math.log(b,a)




a,b=input("Enter two nos:").split(",",2)
str=input("OPERATION TO BE PERFORM:")
print(func(str,a,b))


