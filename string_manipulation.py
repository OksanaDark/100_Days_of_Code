some_string = 'Check out all of our playable games, videos, and toys.'

text = some_string.split(" ")

newString = ''

for val in text:
    val = val.strip(',')
    val = val.strip('.')
    newString += val.capitalize() + ' '
print(newString)
