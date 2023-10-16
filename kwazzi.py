def print_star_digits():
    temp=[]
    star_digits={
        '2': ['*****',
              '*   *',
              '    *',
              ' *** ',
              '*    ',
              '*    ',
              '*****'],
        '3': ['**** ',
              '*   *',
              '    *',
              ' *** ',
              '    *',
              '*   *',
              '**** '],
        '5': ['*****',
              '*    ',
              '*    ',
              '*****',
              '    *',
              '    *',
              '*****']}
    number=input ("Введите число (2 или 3 или 5) ")
    if number in star_digits:
            for line in star_digits[number]:
                print(line)
    else:
            print('0 или 1')
print_star_digits()
