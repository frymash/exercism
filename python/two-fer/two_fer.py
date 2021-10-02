def two_fer(name='you'):
    return f'One for {name}, one for me.'

# Although f-strings are preferred, there's the option of using
# str.format() to solve the issue as well.
#
# def two_fer(name='you'):
#    return 'One for {}, one for me.'.format(name)
