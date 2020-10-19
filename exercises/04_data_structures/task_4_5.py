# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"


Решение:
  
  Для решения данной задачи использую метод split() для разбития строк на части с
  использованием разделителя ','. Каждый список записываю в свою переменную. С помощью split 
  commands[-1].split(',') получаю список vlan. 
  С помощью метода set() преобразовую списки в множества и применяю метод intersection()
  для получения списка пересекающихся vlan
  
  
 command1 = "switchport trunk allowed vlan 1,2,3,5,8"
 command2 = "switchport trunk allowed vlan 1,3,8,9"
 list_vlan1 = command1.split()
 vlans1 = list_vlan1[-1].split(',')
 list_vlan2 = command2.split()
 vlans2 = list_vlan2[-1].split(',')
 vlans1 = set(vlans1)
 vlans2 = set(vlans2)
 vlans1.intersection(vlans2)
