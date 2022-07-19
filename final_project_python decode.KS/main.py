import math


logo='''
██╗░░░░░███████╗████████╗██╗░██████╗  ██╗░░██╗███╗░░██╗░█████╗░░██╗░░░░░░░██╗
██║░░░░░██╔════╝╚══██╔══╝╚█║██╔════╝  ██║░██╔╝████╗░██║██╔══██╗░██║░░██╗░░██║
██║░░░░░█████╗░░░░░██║░░░░╚╝╚█████╗░  █████═╝░██╔██╗██║██║░░██║░╚██╗████╗██╔╝
██║░░░░░██╔══╝░░░░░██║░░░░░░░╚═══██╗  ██╔═██╗░██║╚████║██║░░██║░░████╔═████║░
███████╗███████╗░░░██║░░░░░░██████╔╝  ██║░╚██╗██║░╚███║╚█████╔╝░░╚██╔╝░╚██╔╝░
╚══════╝╚══════╝░░░╚═╝░░░░░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░

░█████╗░██████╗░███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██║██████╔╝█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░██║██╔═══╝░██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░░░░███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝'''



logo2='''
▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█'''



#---------------------CODE STARTS HERE---------------------------!!!!!


print(logo)
print(".................................WELCOME USER....................................")

def func(str,a,b):
  if str=="Addition":
    return a+b
  elif str=="Substraction":
    no=a-b
    return abs(no)
  elif str=="Division":
    return a/b
  elif str=="Multiplication":
    return a*b    
  elif str=="Exponent":
    print(f'By default {a} is taken as base and {b} is taken to be exponent')
    return a**b 
  elif str=="Logarithm":
    print(f'By default {a} is taken as base and {b} is taken to be argument')
    return math.log(b,a)
  


game=True 
while game:
  a,b=map(int,input("Enter two nos:").split())
  print("Operations u can choose \n 1.Addition\n2.Substraction\n3.Division\n4.Multiplication\n5.Exponent\n6.Logarithm\n...exit")
  str=input("\nOPERATION TO BE PERFORM:")
  if(str=="exit"):
    game=False
    print("Oaky, You can leave now")  
  else:
    print(func(str,a,b))


print(logo2)


