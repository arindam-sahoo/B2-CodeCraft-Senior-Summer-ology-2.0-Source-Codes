'''
1.  Phonebook: Create a dictionary to store phone numbers of your friends and family. Keys should be names, and values should be phone numbers. Write code to add new entries, search for a phone number by name, and delete entries. (Myra's Task)
'''
contacts = {'A': 1234567890, 'B': 5432167890}
# adding new entries
contacts['C'] = 9876543210
print(contacts)
# searching for a phone number by name
print(contacts['B'])
# deleting entries
del contacts['A']
print(contacts)
'''
2.  Word Counter: Write a program that takes sentences as input and counts the frequency of each word. Use a dictionary to store word counts, where the key is the word and the value is its count. (Reyansh's Task)
'''
sentence = input("Enter a sentence:")
words = sentence.split()
freq = {}
for word in words:
  if word in freq:
    freq[word] += 1
  else:
    freq[word] = 1
print(freq)
'''  
3.  Inventory Management: Create a dictionary to represent a store's inventory. Keys should be product names, and values should be dictionaries with information like quantity and price. Write functions to add new items, update stock levels, and calculate the total value of the inventory. (Niranjan's Task)
'''
data = {
    'Laptop': {
        'quantity': 10,
        'price': 1000
    },
    'Mobile': {
        'quantity': 20,
        'price': 500
    },
    'Tablet': {
        'quantity': 15,
        'price': 800
    },
    'Charger': {
        'quantity': 5,
        'price': 200
    },
    'Headphones': {
        'quantity': 8,
        'price': 150
    }
}

print(data)


def add_new_product(name, quantity, price):
  global data
  data[name] = {'quantity': quantity, 'price': price}


def update_stock(name, quantity):
  global data
  data[name]['quantity'] = quantity

def calc_total():
  global data
  total = 0
  for item, info in data.items():
    print(f"{item}: {info['quantity']} x {info['price']} = {info['quantity']*info['price']}")
    total += info['quantity'] * info['price']
  print("Total inventory:", total)


add_new_product('Camera', 12, 800)
add_new_product('Earphones', 22, 100)
print(data)

update_stock(name='Laptop', quantity=12)
print(data)

calc_total()