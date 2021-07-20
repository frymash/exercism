def convert(number):
    raindrops = ''

    ls = [(3,'Pling'),(5,'Plang'),(7,'Plong')]

    for divisor, sound in ls:
        if number % divisor == 0:
            raindrops += sound

    return raindrops if raindrops else str(number) # ternary if statement
