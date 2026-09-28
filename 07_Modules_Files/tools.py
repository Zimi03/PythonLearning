def seconds_to_mmss(seconds):
    minutes = seconds//60
    left_seconds = seconds - (minutes*60)
    return f'{minutes}:{left_seconds:02d}'

def is_even(number):
    return number%2 == 0