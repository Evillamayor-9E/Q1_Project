from pyscript import display, document# pyright: ignore[reportMissingImports]

def collecting_data(e):
    document.getElementById("out1").innerHTML = ""
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("number").value

    display(f"Full name: {name}", target="out1")
    display(f"Address: {address}", target="out1")
    display(f"Number: {number}", target="out1")

def ordering_form(e):
    document.getElementById("output2").innerHTML = ""
    Food1 = document.getElementById('menu1')
    Food2 = document.getElementById('menu2')
    Food3 = document.getElementById('menu3')
    Food4 = document.getElementById('menu4')
    Food5 = document.getElementById('menu5')

    total = (float(Food1.value) * Food1.checked + 
             float(Food2.value) * Food2.checked + 
             float(Food3.value) * Food3.checked + 
             float(Food4.value) * Food4.checked + 
             float(Food5.value) * Food5.checked )
    
    display(f'The total amount is {total} Pesos', target='output2')