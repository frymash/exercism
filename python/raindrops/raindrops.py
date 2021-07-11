def convert(number):
    raindrops = ''

    dict = [(3,'Pling'),(5,'Plang'),(7,'Plong')]

    for divisor, sound in dict:
        if number % divisor == 0:
            raindrops += sound

    if raindrops == '':
        return str(number)
    else:
        return raindrops
