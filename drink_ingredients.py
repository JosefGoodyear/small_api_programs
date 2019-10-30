import requests, sys
# if running program without an argument, choose a random drink
if len(sys.argv) < 2:
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
# format drink name, if multiple words
else:
    drink = sys.argv[1]
    for i in range(2,len(sys.argv)):
        drink += '%20' + sys.argv[i]
    url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + drink
r =  requests.get(url).json()
# get drink name
try:
    print(r.get('drinks')[0].get('strDrink'))
except TypeError:
    print("I can't seem to find that drink!")
    exit()
# get drink ingredients
for i in range(1,9):
    if r.get('drinks')[0].get('strIngredient' + str(i)) is not None:
        print('\t' + r.get('drinks')[0].get('strIngredient' + str(i)))
    else:
        break

