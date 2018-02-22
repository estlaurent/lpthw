# create a function that returns several values
# and sends those to a string

# the function returns how many quater notes, eight notes and sixteen
# notes per bar

bars = int(input("\nExactly how many bars of 4/4 do we have? "))

def results(bars):
    quater = bars * 4
    eight = bars * 8
    sixteen = bars * 16
    return bars, quater, eight, sixteen

out = results(bars)

print("""
    In {} bars we have:
    {} quater notes,
    {} eight notes and
    {} sixteeth notes""".format(*out))
