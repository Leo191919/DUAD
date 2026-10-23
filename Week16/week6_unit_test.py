import pytest
from exercises2b import sum_value
from exercises3 import sum_list
from exercises4 import turn_over
from exercises5 import counting_letter
from exercises6 import alphabetical_sequence
from exercises7 import square_root, es_primo, roots_of_list, numbers_prime

#exercises2b - 
def test_sum_value():
    result = sum_value(6, 6)
    assert result == 12


def test_sum_negative_values():

    result = sum_value(-12, -6)
    assert result == -18

def test_sum_with_mixed_values():
    result = sum_value(7, -5)
    assert result == 2


#Exercises3-Sum_list

def test_sum_list():

    data = [1,2,3,4,5,6,7,8,9]
    result = sum_list(data)
    assert result == 45


def test_sum_list_with_negative_values():
    data =[-5, -9, 18, 22]
    result = sum_list(data)
    assert result == 26


def test_sum_list_all_negative():
    data =[-5, -9, -18, -22]
    result = sum_list(data)
    assert result == -54

#Exercises4 - turn_over

def test_turn_over():
    assert turn_over("Hello World") == "dlroW olleH"


def test_turn_over_empty ():
    assert turn_over("")==""


def test_turn_over_string_numbers_and_symbol():
    assert turn_over("123456!@#$%^")=="^%$#@!654321"


#Exercises5 - counting_letter

def test_counting_letter():
    upper, lower = counting_letter("HelloWorld")
    assert upper ==2 
    assert lower ==8


def test_counting_letter_all_uppercase():
    upper, lower = counting_letter("PYTHON")
    assert upper == 6
    assert lower == 0 

def test_counting_letter_with_spaces_and_numbers():
    upper, lower = counting_letter( "PyThOn 123!@#")
    assert upper == 3
    assert lower == 3 


#Exercises6 - alphabetical_sequence

def test_alphabetical_sequence():
    assert alphabetical_sequence("truck_trailer_car_train_bike_bus") == "bike_bus_car_trailer_train_truck"


def test_alphabetical_sequence_all_upper_letter():
    assert alphabetical_sequence("HUGO_MARTIN_LUCAS_MATEO_LEO_PABLO_ALVARO") == "ALVARO_HUGO_LEO_LUCAS_MARTIN_MATEO_PABLO"


def test_alphabetical_sequence_mixed_case_sensitive():
    assert alphabetical_sequence("betas_Alpha_gamma")

#Exercise7 -square_root, es_primo, roots_of_list, numbers_prime

def test_square_root_perfect_and_non_perfect_squares ():
    assert square_root(0) == 0 
    assert square_root (16) == 4 
    assert square_root (15) == 3
    assert square_root (99) == 9


def test_es_primo_known_and_non_known_primes ():
    assert es_primo(2) == True
    assert es_primo (17)== True
    assert es_primo (9) == False
    assert es_primo (87) == False


def test_roots_of_list_basic_case ():
    input_list = [4, 9, 25]
    expected_output=[2, 3, 5]
    assert roots_of_list(input_list) == expected_output


def test_numbers_prime_basic_case():
    input_list = [2, 3, 4, 5, 6, 7]
    expected_output = [2, 3, 5, 7]
    assert numbers_prime(input_list) == expected_output


    