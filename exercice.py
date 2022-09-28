#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	result=''
	result+=name
	#price sous-total
	sum=0
	for item in data:
		sum+=item[INDEX_QUANTITY]*item[INDEX_PRICE]
	#taxes
	taxes=0.15*sum
	#total
	total= sum+taxes
	bill_data=[
		("SOUS-TOTAL  ",sum),
		("TAXES		",taxes),
		("TOTAL		",total)
	]
	#format
	for i in bill_data:
		result+="\n" + f"{i[0]} {i[1] : >20.2f} $"
	return result


def format_number(number, num_decimal_digits):
	#absolute value
	nombre=abs(number)
	#partie decimale
	decimals=nombre%1
	#nombre
	nombre=nombre-decimals
	decimals_in_number= round(decimals*10**num_decimal_digits)
	decimals_str= '.'+f'{decimals_in_number}'

	whole=''
	while nombre>=1000:
		digits=nombre%1000
		whole = f' {digits:.0f}' +whole
		nombre=nombre// 1000
	whole = f'{nombre:.0f}' + whole

	if number<0:
		i='-'
	else:
		i=''
	return i+ whole + decimals_str

def get_triangle(num_rows):
	pyramid_row_top= '+'*(2*(num_rows)+1)
	pyramid_row_bottom=pyramid_row_top
	pyramid_int_rows=[]
	for i in range(num_rows+1):
		if i==0:
			continue
		row='+'+ ' '*(num_rows-i)+'A'*(2*i-1)+' '*(num_rows-i)+'+'
		pyramid_int_rows.append(list(row))
	pyramid_rows=[]
	for pyramid_int_row in pyramid_int_rows:
		pyramid_row=''
		for symbol in pyramid_int_row:
			pyramid_row+=symbol
		pyramid_rows.append(pyramid_row)

	pyramid= f'{pyramid_row_top}\n'
	for row_number in range(len(pyramid_rows)):
		pyramid+= pyramid_rows[row_number] + '\n'
	pyramid= pyramid+ pyramid_row_bottom
	return pyramid


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
