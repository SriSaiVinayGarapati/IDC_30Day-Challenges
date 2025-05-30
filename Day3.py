#Let's say this is a store selling pencils , erasers , sharpeners , boxes , bags
#Initial Stock
items = {
    "Pencil" : 200,
    "Eraser" : 250,
    "Sharpener" : 250,
    "Box" : 100,
    "Bag" : 0
}

#User arrived to the store...this is how the conversation goes..
#shopkeeper
print("Welcome to the store....")
required_items = input("Specify what items you want : ").split()
available_items = []
for i in required_items:
    if items[i] == 0:
        print(f"{i} will be available in stock by tomorrow")
    else:
        items[i] -= 1
        available_items.append(i)

if len(required_items) == len(available_items):
    print(f'These were the items {available_items} , pay the amount at counter and collect them..')
else:
    print(f'These were the available items {available_items} , pay the amount at counter and collect them..')
