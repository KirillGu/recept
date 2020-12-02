import json
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



     return print(json.dumps(cook_book, indent=1, ensure_ascii=False))
get_rec()
