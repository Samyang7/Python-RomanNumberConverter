# COMP9021 20T3 - Rachid Hamadi
# Assignment 1 *** Due Monday 26 October (Week 7) @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
import math

def valid_number(arabic_number):
    length_before = len(arabic_number)
    arabic = int(arabic_number)
    length_after = len(str(arabic))
    # check whether there the number is starting with 0
    if length_before != length_after:
        return False
    # since the previous check already take care of negative number
    if arabic > 3999:
        return False
    return True

def valid_roman(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # V,L,D can't not be store more than 1 and they can be put ahead a bigger number
    # the small number must be within the range and can't not be V,L,D
    # smaller and bigger number, the next one must be bigger than the total
    VLD_dict = {'V': 0, 'L': 0, 'D': 0}
    
    previous_value = 0
    previous_roman = ''
    count = 0
    length = len(roman_string)
    index = -1
    signal = 0
    # scanning roman_string one by one from the right to left
    while index >= -length:
        current_roman = roman_string[index]
        # checking if the previous roman equal to current roman
        # not: turn off the 'indicate signal' and make 'count' equal to 0
        # yes: turn on the 'indicate signal' and increment count by 1
        if previous_roman != current_roman:
            signal = 0
            count = 0
        else:
            signal = 1
            count += 1
            if (count > 3):
                return False
        # checking V, L, D cannot be store more than 1
        if current_roman in VLD_dict.keys():
            VLD_dict[current_roman] += 1
            if VLD_dict[current_roman] > 1:
                return False
        
        if index != -length:
            # if the current value is greater than previous value
            # check if the next value is greater than the current value so that we know whether
            # we need to take care of next and current togther as a whole number or just the current number
            if roman_dict[current_roman] >= previous_value:
                # consider current number
                if roman_dict[roman_string[index-1]] >= roman_dict[current_roman]:
                    previous_value = roman_dict[current_roman]
                    previous_roman = current_roman
                    # if number is unique appear than the previous, count = 1
                    if signal == 0:
                        count += 1
                    index -= 1
                # consider next and current number
                else:
                    # subtracted number cannot be [V, L, D]
                    if roman_string[index-1] in VLD_dict.keys():
                        return False
                    # current cannot greater than next for more than 10 time
                    if roman_dict[current_roman] > 10 * roman_dict[roman_string[index-1]]:
                        return False
                    buffer_value = roman_dict[current_roman] - roman_dict[roman_string[index-1]]
                    # the combined value needs to greater than the previous value by at least 10 times
                    if len(str(buffer_value)) <= len(str(previous_value)) and previous_value != 0:
                        return False
                    previous_value = buffer_value
                    previous_roman = roman_string[index-1]
                    count += 1
                    index -= 2
            else:
                return False
        # if index is in the last position, check if it greater than the previous only
        else:
            if roman_dict[current_roman] < previous_value:
                return False
            else:
                index -= 1
    
    return True

def valid_argument(string):
    arabic_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    string_length = len(string)
    num_of_arabic = 0                                  
    num_of_roman = 0
    # check wether the argument contain both number and character
    # or don't even has a proper either arabic and roman
    for char in string:
        if char in arabic_list:
            num_of_arabic += 1
        if char in roman_list:
            num_of_roman += 1

    if num_of_arabic != 0:
        if string_length != num_of_arabic:
            return False
    if num_of_roman != 0:
        if string_length != num_of_roman:
            return False
    if num_of_roman == 0 and num_of_arabic == 0:
        return False

    if num_of_arabic == string_length:
        if valid_number(string) == False:
            return False
    # check if the roman is valid to be converted
    if num_of_roman == string_length:
        if valid_roman(string) == False:
            return False

    return True

def convert_arabic(arabic_string):
    roman = ''
    arabic_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    # scaning through each number of arabic
    # for example '16', starting from 1, base is 10, only need to append x once, next is 6, base is 0, only need to append V and I for once
    # another example 27, starting from 2, base is 10, need to append X twice, next is 7, base is 0, append V for once and I for twice
    length = len(arabic_string)
    for index in range(len(arabic_string)):
        number = int(arabic_string[index])
        if number != 0:
            exponent = length - 1 - index
            base = 10**exponent
            if number < 4:
                for i in range(number):
                    roman += arabic_dict[base]
            elif number == 4:
                roman += arabic_dict[base]
                roman += arabic_dict[base*5]
            elif number > 4 and number < 9:
                roman += arabic_dict[base*5]
                for i in range(number - 5):
                    roman += arabic_dict[base]
            elif number == 9:
                roman += arabic_dict[base]
                roman += arabic_dict[base*10]
    return roman

def convert_roman(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    index = -1
    length = -len(roman_string)
    while index >= length:
        if index > length:
            # if pattern is like xxi, just add it 
            if roman_dict[roman_string[index-1]] >= roman_dict[roman_string[index]]:
                total += roman_dict[roman_string[index]]
                index -= 1
            # if pattern is like IX, do X - I and add it
            else:
                temp_value = roman_dict[roman_string[index]] - roman_dict[roman_string[index-1]]
                total += temp_value
                index -= 2
        # avoid index error since last letter doesn't need to think about index-1
        elif index == length:
            total += roman_dict[roman_string[index]]
            index -= 1

    return total


def first_convert_method(string_be_converted):
    if valid_argument(string_be_converted) == False:
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()
    arabic_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if string_be_converted[0] in arabic_list:
        roman = convert_arabic(string_be_converted)
        print("Sure! It is " + roman)
    else:
        arabic = convert_roman(string_be_converted)
        print("Sure! It is " + str(arabic)) 

def convert_number(number_be_converted, generalized_roman_symbol):
    # create the generalized_roman_symbol like 'valid_generalized_roman' function but instead number as key
    symbol_dict = {}
    for index in range(-1, -len(generalized_roman_symbol)-1, -1):
        exponent  = (abs(index)-1) // 2
        remainder = (abs(index)-1) % 2
        if remainder == 1:
            symbol_dict[5*10**exponent] = generalized_roman_symbol[index]  
        else:
            symbol_dict[1*10**exponent] = generalized_roman_symbol[index]  
    # exact same as the 'convert_arabic' function
    generalized_roman = ''
    length = len(number_be_converted)
    for index in range(len(number_be_converted)):
        number = int(number_be_converted[index])
        if number != 0:
            exponent = length - 1 - index
            base = 10**exponent
            if number < 4:
                for i in range(number):
                    generalized_roman += symbol_dict[base]
            elif number == 4:
                generalized_roman += symbol_dict[base]
                generalized_roman += symbol_dict[base*5]
            elif number > 4 and number < 9:
                generalized_roman += symbol_dict[base*5]
                for i in range(number - 5):
                    generalized_roman += symbol_dict[base]
            elif number == 9:
                generalized_roman += symbol_dict[base]
                generalized_roman += symbol_dict[base*10]
    return generalized_roman

def convert_generalized_roman(generalized_roman, generalized_roman_symbol):
    # create the generalized_roman_symbol like 'valid_generalized_roman' function
    symbol_dict = {}
    for index in range(-1, -len(generalized_roman_symbol)-1, -1):
        exponent  = (abs(index)-1) // 2
        remainder = (abs(index)-1) % 2
        if remainder == 1:
            symbol_dict[generalized_roman_symbol[index]] = 5*10**exponent
        else:
            symbol_dict[generalized_roman_symbol[index]] = 1*10**exponent
    # exact same as the 'convert_roman' function
    total = 0
    index = -1
    length = -len(generalized_roman)
    while index >= length:
        if index > length:
            if symbol_dict[generalized_roman[index-1]] >= symbol_dict[generalized_roman[index]]:
                total += symbol_dict[generalized_roman[index]]
                index -= 1
            else:
                temp_value = symbol_dict[generalized_roman[index]] - symbol_dict[generalized_roman[index-1]]
                total += temp_value
                index -= 2
        elif index == length:
            total += symbol_dict[generalized_roman[index]]
            index -= 1

    return total    


def valid_generalized_roman(generalized_roman, generalized_roman_symbol):

    # create the generalized_roman_symbol and special sysmbol like 'valid_argument function'
    # later we can just copy the same code from 'valid_arguement' to check
    symbol_dict = {}
    special_dict = {}
    for index in range(-1, -len(generalized_roman_symbol)-1, -1):
        exponent  = (abs(index)-1) // 2
        remainder = (abs(index)-1) % 2
        if remainder == 1:
            symbol_dict[generalized_roman_symbol[index]] = 5*10**exponent
        else:
            symbol_dict[generalized_roman_symbol[index]] = 1*10**exponent
    for key in symbol_dict.keys():
        if str(symbol_dict[key])[0] == '5':
            special_dict[key] = 0
    
    previous_value = 0
    previous_roman = ''
    count = 0
    length = len(generalized_roman)
    index = -1
    signal = 0
    # scanning roman_string one by one from the right to left
    while index >= -length:
        current_roman = generalized_roman[index]
        # checking if the previous roman equal to current roman
        # not: turn off the 'indicate signal' and make 'count' equal to 0
        # yes: turn on the 'indicate signal' and increment count by 1
        if previous_roman != current_roman:
            signal = 0
            count = 0
        else:
            signal = 1
            count += 1
            if (count > 3):
                return False
        # checking V, L, D cannot be store more than 1
        if current_roman in special_dict.keys():
            special_dict[current_roman] += 1
            if special_dict[current_roman] > 1:
                return False
        
        if index != -length:
            # if the current value is greater than previous value
            # check if the next value is greater than the current value so that we know whether
            # we need to take care of next and current togther as a whole number or just the current number
            if symbol_dict[current_roman] >= previous_value:
                # consider current number
                if symbol_dict[generalized_roman[index-1]] >= symbol_dict[current_roman]:
                    previous_value = symbol_dict[current_roman]
                    previous_roman = current_roman
                    # if number is unique appear than the previous, count = 1
                    if signal == 0:
                        count += 1
                    index -= 1
                # consider next and current number
                else:
                    # subtracted number cannot be [V, L, D]
                    if generalized_roman[index-1] in special_dict.keys():
                        return False
                    # current cannot greater than next for more than 10 time
                    if symbol_dict[current_roman] > 10 * symbol_dict[generalized_roman[index-1]]:
                        return False
                    buffer_value = symbol_dict[current_roman] - symbol_dict[generalized_roman[index-1]]
                    # the combined value needs to greater than the previous value by at least 10 times
                    if len(str(buffer_value)) <= len(str(previous_value)) and previous_value != 0:
                        return False
                    previous_value = buffer_value
                    previous_roman = generalized_roman[index-1]
                    count += 1
                    index -= 2
            else:
                return False
        # if index is in the last position, check if it greater than the previous only
        else:
            if symbol_dict[current_roman] < previous_value:
                return False
            else:
                index -= 1
    
    return True


def valid_be_converted(string, letter):
    count_number = 0
    arabic_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    length = len(string)
    # check if the string contain the number, letter or other char
    # if char is not in letter then it is invalid
    # if it contain other char then it is invalid
    for char in string:
        if char.isalpha() == False and char not in arabic_list:
            return False
        elif char in arabic_list:
            count_number += 1
        elif char.isalpha():
            if char not in letter:
                return False
    # if string contains not fully number, invalid
    if count_number != 0 and count_number != length:
        return False
    # if number has 0 in the front, invalid
    if count_number == length:
        if len(str(int(string))) < length:
            return False
    return True
             
def valid_letter(decode_letter_string):
    decode_dict = {}
    for letter in decode_letter_string:
        # must be a letter
        if letter.isalpha() == False:
            return False
        if letter not in decode_dict:
            decode_dict[letter] = 1
        # needs to be distinct
        else:
            return False
    return True

def third_convert_method(string_to_be_converted, decode_letter):
    if valid_letter(decode_letter) == False:
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()
    if valid_be_converted(string_to_be_converted, decode_letter) == False:
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()
    # if the format meet the requirment, check whether generalized_roman meet convert requirment like classic_roman
    if string_to_be_converted[0].isalpha():
        if valid_generalized_roman(string_to_be_converted, decode_letter) == False:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        else:
            number = convert_generalized_roman(string_to_be_converted, decode_letter)
            print("Sure! It is " + str(number))
    else:
        generalized_roman = convert_number(string_to_be_converted, decode_letter)
        print("Sure! It is " + generalized_roman)

def valid_minimal_string(string):
    # test if the each element is valid letter not matter it is lower case or upper case
    for char in string:
        if char.isalpha() == False:
            return False
    return True

# signal is used to indicate that the value we need can not be 5 or 50 or 500...
# the find_single_value function is to find the valid value of A that A only existed once in the sequence
def find_single_value(reverse_string, used_value, previous_value, index, element_dict, signal):
    value = 0
    degree = degree2= 0

    while True:
        # the searching idea is bascially same as 'find_double_function'
        if signal == 0:
            num = [1, 5]
            T = num[0]*10**degree
            T2 = num[1]*10**degree2
            while T in used_value or T <= previous_value:
                degree += 1
                T = num[0]*10**degree
            while T2 in used_value or T2 <= previous_value:
                degree2 += 1
                T2 = num[1]*10**degree2


            if T >= T2:
                if T2 > previous_value:
                    value = T2
                    break
                elif T > previous_value:
                    value = T
                    break
            else:
                if T > previous_value:
                    value = T
                    break
                elif T2 > previous_value:
                    value = T2
                    break

        else:
            num = [1]
            T = num[0]*10**degree
            while T in used_value or T <= previous_value:
                degree += 1
                T = num[0]*10**degree
        
            if T > previous_value:
                value = T
                break

    used_value.append(value)
    element_dict[reverse_string[index]] = value
    return value

# the signal act as the same function just like find_single_value
# the fix signal do the job when the AB patten A is determined already and need to find B
# the find double value function is to find valid pair of AB that B - A is smallest integer comparing with previous value
# here T means B, Y means A, Y cannot be 5, 50, 500..., depend on the signal, T can be 1, 5, 10, 50... or only 1, 10, 100...
# if fix_signal is 1, means Y on longer at value from 1, 10, 100,... instead it is value A
# after finished finding the value, put them into used_value
def find_double_value(reverse_string, used_value, previous_value, index, element_dict, signal, fix_signal):
    # finding the next smallest valid combination
    n3 = n4 = n5 = 0
    value1 = value2= 0
    while True:
        if signal == 0:
            num = [1, 5]
            T = num[0]*10**n4
            T2 = num[1]*10**n5
            if fix_signal == 0:
                Y = 1*10**n3
            else:
                Y = element_dict[reverse_string[index+1]]

            # need to make sure T, T2 or Y is not in the used_list
            # if fix_signal is 1 not need to check Y
            while T in used_value:
                n4 += 1
                T = num[0]*10**n4
            while T2 in used_value:
                n5 += 1
                T2 = num[1]*10**n5
            if fix_signal == 0:
                while Y in used_value:
                    n3 += 1
                    Y = 1*10**n3
            # need to make sure T or T2 at least greater than Y
            while Y >= T:
                n4 += 1
                T = num[0]*10**n4
            while Y >= T2:
                n5 += 1
                T2 = num[1]*10**n5

            if previous_value == 0:
                if T2 <= T:
                    if (T2 > Y and (T2-Y) > previous_value and T2 <= Y*10):
                        value1 = T2
                        value2 = Y
                        break
                    if (T > Y and (T-Y) > previous_value and T <= Y*10):
                        value1 = T
                        value2 = Y
                        break
                else:
                    if (T > Y and (T-Y) > previous_value and T <= Y*10):
                        value1 = T
                        value2 = Y
                        break
                    if (T2 > Y and (T2-Y) > previous_value and T2 <= Y*10):
                        value1 = T2
                        value2 = Y
                        break
            else:
                # since it is AB pattern need to make sure the B-A value also need to bigger than previous value by 1 position
                # for example, if previous value is 4, the B-A must be at least 10
                if T2 <= T:
                    if (T2 > Y and (T2-Y) > previous_value and len(str(T2-Y))>len(str(previous_value)) and T2 <= Y*10):
                        value1 = T2
                        value2 = Y
                        break
                    if (T > Y and (T-Y) > previous_value and len(str(T-Y))>len(str(previous_value)) and T <= Y*10):
                        value1 = T
                        value2 = Y
                        break  
                else:
                    if (T > Y and (T-Y) > previous_value and len(str(T-Y))>len(str(previous_value)) and T <= Y*10):
                        value1 = T
                        value2 = Y
                        break  
                    if (T2 > Y and (T2-Y) > previous_value and len(str(T2-Y))>len(str(previous_value)) and T2 <= Y*10):
                        value1 = T2
                        value2 = Y
                        break

        else:
            num = [1]
            T = num[0]*10**n4
            if fix_signal == 0:
                Y = 1*10**n3
            else:
                Y = element_dict[reverse_string[index+1]]
            
            while T in used_value:
                n4 += 1
                T = num[0]*10**n4
            if fix_signal == 0:
                while Y in used_value:
                    n3 += 1
                    Y = 1*10**n3
            
            while Y >= T:
                n4 += 1
                T = num[0]*10**n4
                
            if previous_value == 0:
                if (T > Y and (T-Y) > previous_value and T <= Y*10):
                    value1 = T
                    value2 = Y
                    break
            else:
                if (T > Y and (T-Y) > previous_value and len(str(T-Y))>len(str(previous_value)) and T <= Y*10):
                    value1 = T
                    value2 = Y
                    break

    used_value.append(value1)
    used_value.append(value2)       
    element_dict[reverse_string[index]] = value1 
    element_dict[reverse_string[index+1]] = value2

    return value1, value2

def convert_string(string):
    # remove duplicate
    element_set = set()
    for char in string:
        element_set.add(char)
    # make a element key list so that later value can be add into it
    # key is the letter, value is the number that will be allocated later
    element_dict = {}
    for ele in list(element_set):
        if ele not in element_dict:
            element_dict[ele] = 0
    # examine the sequence from right to left so reverse the string to check 
    # check the string letter by letter, record the letter value that had been allocated in the 'used_value' list
    # everytime need to check with the previous value. If there is a pattern like 'AB' which A and B both unique 
    # in the sequence, then need to do B-A and this value must at least greater than previous value by 1 position
    reverse_string = string[::-1]
    previous_value = 0
    used_value = []
    index = 0
    while index < len(reverse_string):
        # if the letter value is already be decided, need to make sure it value must be greater than previous value
        # if it doesn't, system return, otherwise increment index no need to find the value for it since it already has one
        if element_dict[reverse_string[index]] != 0:
            if element_dict[reverse_string[index]] < previous_value:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            previous_value += element_dict[reverse_string[index]]
            index += 1
        else:
            index2 = reverse_string.find(reverse_string[index], index+1)
            # if the letter is unique
            if index2 == -1:
                # the next letter is also unique
                if index != len(reverse_string)-1 and reverse_string.find(reverse_string[index+1], index + 2) == -1 and element_dict[reverse_string[index+1]] == 0:
                    # if there is a pattern AB, need to compare whether A + B smaller or B - A smaller
                    # use find_single_function for A+B and use find_double_function to find B - A
                    dict1 = element_dict.copy()
                    dict2 = element_dict.copy()
                    list1 = used_value.copy()
                    list2 = used_value.copy()
                    value1, value2 = find_double_value(reverse_string, list1, previous_value, index, dict1, 0, 0)
                    value3 = find_single_value(reverse_string, list2, previous_value, index, dict2, 0)
                    value4 = find_single_value(reverse_string, list2, previous_value, index+1, dict2, 0)

                    buffer_value1 = value1 - value2
                    buffer_value2 = value3 + value4
                    if buffer_value1 < buffer_value2:
                        value1, value2 = find_double_value(reverse_string, used_value, previous_value, index, element_dict, 0, 0)
                        previous_value += buffer_value1
                    else:
                        value3 = find_single_value(reverse_string, used_value, previous_value, index, element_dict, 0)
                        value4 = find_single_value(reverse_string, used_value, previous_value, index+1, element_dict, 0)
                        previous_value += (value3 + value4)
                    index += 2
                # the next letter is not unique, then just need to find a value for the first unique letter using find_single_value
                else:
                    output = find_single_value(reverse_string, used_value, previous_value, index, element_dict, 0)
                    previous_value += output
                    index += 1
            else:
                # if there exist more than one letter and the distance between it is bigger than 3
                # it is then no possible to convert it
                if index2 - index > 3:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                # if there exist more than one letter and the it is right next to itself
                elif index2 - index == 1:
                    # if three in a role, get the value for the letter and increment index by 3, value cannot be 5, 50, 500..
                    if index2 + 1 < len(reverse_string) and reverse_string[index2+1] == reverse_string[index2]:
                        output = find_single_value(reverse_string, used_value, previous_value, index, element_dict, 1)
                        previous_value += output*3
                        index += 3
                    # if four in a role, it is wrong, system return
                    elif index2 + 2 < len(reverse_string) and reverse_string[index2+2] == reverse_string[index2+1] == reverse_string[index2]:
                        print("Hey, ask me something that's not impossible to do!")
                        sys.exit()
                    # if two in a role, get the value for the letter and increment index by 2, value cannot be 5, 50, 500..
                    else:
                        output = find_single_value(reverse_string, used_value, previous_value, index, element_dict, 1)
                        previous_value += output*2
                        index += 2
                # if the pattern is like ACA
                elif index2 - index == 2:
                    n = 0
                    # need to check whether it is AAACA AACA ACA or AAAACA
                    while (index2 + n) < len(reverse_string) and reverse_string[index2+n] == reverse_string[index2]:
                        n += 1
                    if n == 4:
                        print("Hey, ask me something that's not impossible to do!")
                        sys.exit()
                    # if it is AAACA AACA ACA we know that CA must be A-C, so use find_double_function to find the pair 
                    # and increment the index depending on if it is AAACA AACA or ACA, also A can not be 5, 50, 500 so 
                    # we pass signal 1 to indicate
                    value1, value2 = find_double_value(reverse_string, used_value, previous_value, index, element_dict, 1, 0)
                    buffer_value1 = value1 - value2
                    previous_value += (buffer_value1 + value1*n)
                    index += (2+n)
                # if the pattern is like ACBA, we know that B must be smaller than A, C must be greater than A
                # so first decided the BA value by 'find_double_function' and then use 'find_double_function' again
                # to find the C value but this time since A has already be decided, pass a fix signal 1 to the function 
                # and tell that it is going to find the smallest integer who is valid to do AC
                elif index2 - index == 3:
                    value1, value2 = find_double_value(reverse_string, used_value, previous_value, index, element_dict, 1, 0)
                    buffer_value1 = value1 - value2
                    previous_value += buffer_value1
                    value1, value2 = find_double_value(reverse_string, used_value, previous_value, index+2, element_dict, 0, 1)
                    buffer_value1 = value1 - value2
                    previous_value += buffer_value1
                    index += 4

    # find the max_value that had been allocated to the letter
    # in the meantime, store the dictionary reversely, so the key is value, value is letter
    max_value = 0
    number_dict = {}
    for key in element_dict:
        if element_dict[key] > max_value:
            max_value = element_dict[key]
        number_dict[element_dict[key]] = key
    # finding the degree of the max_value
    degree = 0
    while max_value // 10**degree != 0:
        degree += 1
    
    # the usual number sequence is 1, 5, 10, 50, 100, 500 ...
    # it can also be interpolate into 1*10**0, 5*10**0, 1*10**1, 5*10**1, 1*10**2, 5*10**2...
    # which 0, 1, 2 is the degree and that's why i used the while loop to find the maximum degree in last step
    # iterate though the degree and one reach the max_value or go beyond degree, break the loop
    # cancatenate single letter into output_string also
    output_string = ''
    n = 0
    while n < degree:
        if 1*10**n in number_dict:
            output_string += number_dict[1*10**n]
        else:
            output_string += '_'
        if 1*10**n == max_value:
            break

        if 5*10**n in number_dict:
            output_string += number_dict[5*10**n]
        else:
            output_string += '_'
        if 5*10**n == max_value:
            break
        n += 1
    #output_string += number_dict[max_value]
    reverse_output_string = output_string[::-1]
    print("Sure! It is {} using {}".format(str(previous_value), reverse_output_string))


def second_convert_method(minimally_convert_string):
    # check if the element in the string is letter or not
    if valid_minimal_string(minimally_convert_string) == False:
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()    
    convert_string(minimally_convert_string)
    
    return True

def valid_input(input_list):
    length = len(input_list)
    # check if total parts of string is 3 or 4 or 5 after split
    if length != 3 and length != 4 and length != 5:
        return False

    # check the spelling is correct
    if length == 3:
        if input_list[0] != 'Please' or input_list[1] != 'convert':
            return False
    if length == 4:
        if input_list[3] != 'minimally':
            return False
    if length == 5:
        if input_list[3] != 'using':
            return False
    return True 
      
# define the starting function
def please_convert():
    input_string = input('How can I help you? ')
    input_list = input_string.split()
    if valid_input(input_list) == False:
        print("I don't get what you want, sorry mate!")
        sys.exit()

    length = len(input_list)
    if length == 3:
        first_convert_method(input_list[2])
    elif length == 4:
        second_convert_method(input_list[2])
    else:
        third_convert_method(input_list[2], input_list[4])

please_convert()

