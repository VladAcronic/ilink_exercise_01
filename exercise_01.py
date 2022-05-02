#
# скрипт вычисляет возможные комбинации четырех входных параметров A B C D,
#  при которых значение F истинно (1) в соответстви со схемой

from operator import *
import itertools

class unsupportedOperationExeption (BaseException):
	pass

def inv_ (firstOperand):
	'''
		инвертирует 0 / 1 в 1 / 0, 
		если на вход подается отличное от 0/1 значение бросает исключение unsupportedOperationExeption
	'''
	if firstOperand == 0:
		return 1
	elif firstOperand == 1:
		return 0
	else:
		raise unsupportedOperationExeption

def calculateFValue (aValue, bValue, cValue, dValue):
	'''
		вычисляет значение F в соответствиии со схемой на основе введенных параметров A B C D
	'''
	result_01 = xor (aValue,bValue)
	result_02 = inv_ (result_01)
	result_03 = inv_ (bValue)
	result_04 = or_ (result_02, result_03)

	result_05 = and_ (cValue, result_04)
	result_06 = or_ (cValue,dValue)
	result_07 = inv_ (result_06)

	fValue = xor (result_05, result_07)

	return fValue

# генерируем комбинацию возможных вариантов значений А, В, С, Д
length = 4
combinations = []
combination = None
for combination in itertools.product([0,1], repeat=length):
	combinations.append(combination)

# обходим список кортежей, вычисляем значение F, 
# записываем удовлетворяющие усливию (F=1) в словарь 
aIndex = 0
bIndex = 1
cIndex = 2
dIndex = 3

resultFilteredMatrix = {}
for combination in combinations:

	resultFValue = calculateFValue (combination[aIndex], 
																	combination[bIndex], 
																	combination[cIndex],
																	combination[dIndex])

	if 1 == resultFValue:
		resultFilteredMatrix.update (dict ({combination:resultFValue}) )

# выводим результат		
print ("A  B  C  D | F")
print ()
for combination, resultF in resultFilteredMatrix.items():
	
	print (*combination, sep="  ", end=" | ")
	print (resultF)
