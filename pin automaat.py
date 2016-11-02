
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














