# -*- coding: cp1251 -*-

"""This class made dict where, size of pallet(size) = key, value of products(how_much) = key value
   and muchs of pallets we need(pallets) = pallets"""
global pallets
def calculator(how_much, size):
    if 0 <  how_much and size:
        pallets = how_much / size
        if how_much % size != 0:
            print ("in last pallet will be shortfall for ", how_much - (pallets * size), " products")
            pallets += 1
        print "for this product you need ", pallets, " pallets"
        return pallets
    else:
        print "Вы ввели отрицательное число"





