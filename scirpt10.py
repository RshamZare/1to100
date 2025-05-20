# Currency Converter
# Convert from one currency to another using fixed exchange rates.
# USD TO CAD 

def currency_exchnage(amount):
    type_of_exchange = str(input("What currnecy you want to convert to? USD/CAD: "))
    amount = int(input("How much? "))
    if type_of_exchange == "USD":
        cad_exchange = amount * 1.40
        return cad_exchange
    if type_of_exchange == "CAD":
        usd_exchnage = amount * 0.72
        return usd_exchnage

print(currency_exchnage(100))