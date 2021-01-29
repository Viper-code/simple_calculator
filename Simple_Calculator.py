#Please dont type in letters or cacl wont work!

float_int = input('Please determine if you are going to use/get a integer or a decimal, type any other key to exit! dec/int ')
if float_int.lower() == 'int':
    print('you are using integers!')
    FIRST = int(input('First: '))
    operartor = input('Add the number or Minus?Type +, -, *, [/ to divide], ** to exponent somthing[2**4 = 16] : ')
    SECOND = int(input('Second: '))

    if operartor == "+":
        print('Sum ' + str(FIRST + SECOND))
    elif operartor == "-": 
        print('Sum ' + str(FIRST - SECOND))
    elif operartor == "*":
        print('Sum ' + str(FIRST * SECOND))
    elif operartor == "/":
        print('Sum ' + str(FIRST / SECOND))
    elif operartor == "**":
        print('Sum ' + str(FIRST ** SECOND))
    input('Pleas press enter to EXIT ')

elif float_int.lower() == 'dec':
    print('you are using decimals!')
    FIRST = float(input('First: '))
    operartor = input('Add the number or Minus?Type +, -, *, [/ to divide], ** to exponent somthing[2**4 = 16] : ')
    SECOND = float(input('Second: '))

    if operartor == "+":
        print('Sum ' + str(FIRST + SECOND))
    elif operartor == "-": 
        print('Sum ' + str(FIRST - SECOND))
    elif operartor == "*":
        print('Sum ' + str(FIRST * SECOND))
    elif operartor == "/":
        print('Sum ' + str(FIRST / SECOND))
    elif operartor == "**":
        print('Sum ' + str(FIRST ** SECOND))
    input('Pleas press enter to EXIT ')

