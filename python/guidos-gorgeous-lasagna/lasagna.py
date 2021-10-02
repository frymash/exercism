'''
Firstly, define the necessary constants; the expected bake time is 40 minutes and the
time required to prepare each lasagna layer (PREPARATION_TIME) is 2 minutes.
'''
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
 
    Function that takes the number of layers in the lasagna and multiplies it by the
    number of minutes needed to prepare each layer (2 min).
    """
    total_preparation_time = number_of_layers * PREPARATION_TIME
    return total_preparation_time
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time for the lasagna.
    Function takes the total preparation time (for all the lasagna layers combined)
    and adds it to the elapsed bake time.
    """
    elapsed_cooking_time = (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
    return elapsed_cooking_time
