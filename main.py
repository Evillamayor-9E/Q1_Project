from pyscript import display

Title = 'Raining Taco' #grabe pagkakaroblox kid mo
owner_name = 'Erich Villamayor'
year = 2026
product = ['soft taco', 'taco supreme', 'cheesy taco', 'crunchy taco', 'spicy taco']
Schedule = 'Open 1:00 am - 3:50am' 
price = {
    'soft taco' : 150,
    'taco supreme' : 200,
    'cheesy taco': 180,
    'crunchy taco' : 165,
    'spicy taco' : 220
}

display( Title, target="title")
display(f' by {owner_name}', target="owner_name")
display(f' since {year}', target="year")

display(product[0], target="row1col1")
display(f'₱ {price["soft taco"]}', target="row1col2")
display(product[1], target="row2col1")
display(f'₱ {price["taco supreme"]}', target="row2col2")
display(product[2], target="row3col1")
display(f'₱ {price["cheesy taco"]}', target="row3col2")
display(product[3], target="row4col1")
display(f'₱ {price["crunchy taco"]}', target="row4col2")
display(product[4], target="row5col1")
display(f'₱ {price["spicy taco"]}', target="row5col2")
