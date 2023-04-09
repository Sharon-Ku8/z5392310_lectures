lst1 = ['a']
print(f'This is lst1: {lst1}')

lst2 = ['b', lst1]
print(f'This is lst2: {lst2}')

lst2[1].append('c')



print(1 == True)
print(1 is True)

var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']

print(var1 ==var2)
print(var1 is var2)


name = input('Who are you?')
print(type(name))
print('Welcome to the class,', name)

hours = input('30')
#Python 3 output numeric value as a string in input () function
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9

if hours > 35 :
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
    pay = hours * normal_rate

print(f'this weekly payment is: {pay}')




for i in range(1,4):
    for j in range(1,4):
        print(i,j)

