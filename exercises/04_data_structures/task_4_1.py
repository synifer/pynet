# -*- coding: utf-8 -*-
"""
Задание 4.1

Используя подготовленную строку nat, получить новую строку, в которой
в имени интерфейса вместо FastEthernet написано GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

Для выполнения данного задания я использую метод Replace()
Метод позволяет осуществить замену последовательности символов в строке на другую последовательность
После применения метода Replace() присваиваю новое значение переменной.

Ответ:
  
   string1 = 'nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"'
   string1.replace('Fast', 'Gigabit')
   string1 = string1.replace('Fast', 'Gigabit')
    

  
    
  
 
