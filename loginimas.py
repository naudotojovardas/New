import logging
#logging.basicConfig(level=logging.DEBUG,filename='loginimas', filemode='w')
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(asctime)s]  - %(message)s')

try:
    num = float(input('number: '))
    logging.info(num)
    name = str(input('name: '))
    logging.info(name)
    let =input('letters: ')
    logging.info(let)
except ValueError as e:
    logging.info({e})

def move_elements_to_end(lst, element):
    count = lst.count(element)
    lst = [x for x in lst if x != element]
    lst.extend([element] * count)
    return lst





