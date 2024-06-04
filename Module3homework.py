data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(list):
    sum = 0
    for element in list:
       if isinstance(element, int):
           sum += element
       elif isinstance(element, str):
           sum += len(element)
       elif isinstance(element, dict):
           for item in element.items():
               sum = sum + len(item[0])
               sum += item[1]
       else:
           sum += calculate_structure_sum(element)
    return sum



result = calculate_structure_sum(data_structure)
print(result)