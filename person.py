def get_rec(rek_file='rec.txt'):
     cook_book = {}
     with open(rek_file) as rec_file:
         while True:
             dish = rec_file.readline().strip().lower()

             if not dish:
                 break
             cook_book[dish] = []
             num = int(rec_file.readline().strip())
             ing = [rec_file.readline().strip().rsplit('|') for _ in range(num)]
             rec_file.readline()
             for item in ing:
                 cook_book[dish].append({'ingridient_name': item[0].rstrip(),
                                         'quantity': int(item[1].replace(' ', '')),
                                         'measure': item[2].replace(' ', '')})



     return cook_book



def get_shop_list_by_dishes(cook_book, dishes, person_num):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_list_item = dict(ingridient)

            new_list_item['quantity'] *= person_num
            if new_list_item['ingridient_name'] not in shop_list:
                shop_list[new_list_item['ingridient_name']] = new_list_item
            else:
                shop_list[new_list_item['ingridient_name']]['quantity'] += new_list_item['quantity']
    return shop_list


def print_list(shop_list):
    for shop_list_item in shop_list.values():
        print(shop_list_item['ingridient_name'].split('[]'), shop_list_item['quantity'],
                                shop_list_item['measure'])


def list_user(cook_book):
    person_num = int(input('Для скольки персон готовим?: '))
    dishes = input('Введите какие блюда хотите: ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_num)
    print_list(shop_list)

cook_book = get_rec()
list_user(cook_book)
