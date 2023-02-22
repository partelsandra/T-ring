import random 

def arvuta():
    number = int(input("Palun sisesta täringute arv:"))
    tulemus = ""
    for i in range(1, number + 1):
        number = random.randint(1, 6)
        tulemus += str(number) + '\n'
    print("\n" + tulemus)
    
arvuta()

