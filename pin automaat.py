
correctPin = 6666 ## de werkende pin code
tries_left = 3 ## aantal pogingen
balance = 1000 ## geld op rekening

pinEntry = int(input("Please enter your pin code: "))

while pinEntry != correctPin: ## checken of de code correct is, maximaal 3 keer.
    tries_left -= 1
    if tries_left == 0:
        print("Your card is blocked, please contact your bank")
        break
    pinEntry = (input("Pin incorrect, please try again: "))

else: ## als de code correct is, vragen hoeveel de persoon wil opnemen en de nieuwe balans printen. 
    withdrawal_amount = int(input("How much would you like to withdraw: "))
    if withdrawal_amount > 1000:
        withdrawal_amount = int(input("You are not that rich, please enter a lower amount: "))
        balance = balance - withdrawal_amount
        print("Your new balance is {}".format(balance))
    elif withdrawal_amount < 0:
        withdrawal_amount = int(input("Don't be silly, you cannot withdraw a negative amount, please enter a positive amount: "))
        balance = balance - withdrawal_amount
        print("Your new balance is {}".format(balance))
    else:
        balance = balance - withdrawal_amount
        print("Your new balance is {}".format(balance))

## wat nog mist zijn checks om te kijken of de ingevoerde pincode en het withdrawal amount geen invalide characters bevatten.
## ik weet hoe ik dat zou kunnen doen met een for loop (en dus per character kijken), maar volgens mij zijn er makkelijkere/snellere
## /efficitientere manieren zoals bijv. str.isdigit(). Ik ben dat in de cursus echter nog niet tegen gekomen. Verder vraag ik me af
## of ik de herhaling van code (DRY) zou kunnen vermijden met een andere programflow, maar daar hoor ik dus graag jouw ideeen
## over.

# Ha, cool! Werkt goed!
# 
# Goed idee om nog wat validatie toe te voegen. Bij de pincode maakt het niet uit wat voor characters deze bevat, zolang hij maar gelijk is 
# aan de juiste pincode, toch? In theorie kan een pincode ook 'ü@#G' zijn (in dit geval). Als je ervoor wil zorgen dat er alleen cijfers ingegeven
# mogen worden dan kun je bijvoorbeeld de input parsen naar een int. Als dat niet lukt, dan is het dus geen valide getal. Hetzelfde kun je doen 
# bij het withdrawal amount. Als je daadwerkelijk naar de user wil communiceren welke van de ingevoerde characters onjuist is, dan kun je idd iets
# als str.isdigit() gebruiken.
# Edit: Oh ik zie net dat je t withdrawalAmount al parsed als int! Dus dat heb je al voor elkaar :-)
# 
# Wat betreft DRY en programflow, met behulp van methods/functions kun je het bijvoorbeeld zo doen (pseudocode):
# 
# # check pin
# amount = readWithdrawalAmount()
# balance = balance - amount
# print("New balance is...")
# 
# def readWithdrawalAmount():
#   while true:
#     amount = int(input("How much would you..."))
#     if amount > balance:
#       print("try again")
#     elif amount <= 0:
#       print("not so negative")
#     else 
#       return amount
# 
# Hiermee splits je dus de 'verantwoordelijkheid' van het programma in 3 dingen: pincode checken, correct withdrawal amount verkrijgen en balance updaten.
# Het opsplitsen van je programma in meerdere losse delen heeft tot gevolg dat het makkelijker te lezen, onderhouden en testen is.
# Hoe groter een programma is hoe meer dit geldt natuurlijk. Dit is dus specifiek iets dat ik niet zozeer tijdens studie heb geleerd maar veel meer tijdens werk.
#
# Oh en er zit 1 bugje in, zie hier:
#
# [master] administrator@~/dev/ATMtrial:python pin\ automaat.py
# Please enter your pin code: 6666
# How much would you like to withdraw: -1
# Don't be silly, you cannot withdraw a negative amount, please enter a positive amount: 2000
# Your new balance is -1000
# 
# Erg cool dat je zomaar iets zelf hebt bedacht en dat hebt geïmplementeerd, dat is precies hoe je programmeren het beste leert! 












