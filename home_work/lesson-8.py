import AllClass.my_class as ac

# Создаем 4 человека
first_h = ac.Human(1, 'Олег', 32, '23.10.1993')

first_c = ac.Company(1)
first_c.add_human(first_h)
first_c.print_company_human_info()

print('Изменения в ветке работяги')