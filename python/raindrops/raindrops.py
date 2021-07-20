def convert(number):
    raindrops = ''

    ls = [(3,'Pling'),(5,'Plang'),(7,'Plong')]

    for divisor, sound in ls:
        if number % divisor == 0:
            raindrops += sound

    if raindrops == '':
        return str(number)
    else:
        return raindrops
