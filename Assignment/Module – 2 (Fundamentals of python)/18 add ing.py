str1 = 'ending'

if str1.endswith('ing'):
    if len(str1) >=3:
        str1 = str1.replace('ing','ly')
        print('changed string', +str1)
    else:
        print('unchanged')
else:
    print('Doesnt contain ing in the end')
