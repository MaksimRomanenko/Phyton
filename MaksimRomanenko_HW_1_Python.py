# 1.Create variable String type
name = 'Maksim'

# 2.Create variable Integer type
age = 49

# 3.Create variable Float type
coca_cola = 33e-2

# 4.Create variable Bytes type
bytes_string = bytes('Python, bytes', 'utf-8')

# 5.Create variable List type
name_list = ['Stanislav', 'Maksim', 'Denis']

# 6.Create variable Tuple type
cars = ('Mercedes', 'BMW', 'Audi')

# 7. variable Set type
fruits = {'mango', 'pineapple', 'durian'}

# 8.Create variable FrozenSet type
parents = frozenset({'Mom', 'Dad'})

# 9.Create variable Dict type
dict_kawa = {
  "Company": "Kawasaki",
  "model": "Ninja 636",
  "year": 2019
}
# 10.Print to the console all variables with the addition of the data type.
print('Name is', name, '_',type(name))
print('Age is', age, '_', type(age))
print('Volume of bottle of coca_cola is', coca_cola, '_', type(coca_cola))
print('bytes_string is ', bytes_string, '_', type(bytes_string))
print('Name list is', name_list, '_', type(name_list))
print("Germany's Big Three is", cars, '_', type(cars))
print('My favorite thai fruits are', fruits, '_', type(fruits))
print('Parents -',parents, '_', type(parents))
print('Kawasaki dictionary -', dict_kawa, '_', type(dict_kawa))

# 11.Create two variables String type. To concatenate into new variable
first = 'Hello, '
second = 'World!'
together = first + second
print(together)

# 12.Print variables of type String and Integer in one line using “,”
print(name, age)

# 13.Print variables of type String and Integer in one line using “+”
print(name + ' ' + str(age))
