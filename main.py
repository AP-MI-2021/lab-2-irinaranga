from datetime import date



def isPrime(x):
    '''
    determina daca un nr. este prim
    :param x: nr. intreg
    :return: True, daca x este prim sau False, in caz contrar
    '''

    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    '''
    determina ultimul nr. mai mic decat n
    :param n: nr. intreg
    :return: ultimul nr. mai mic decat n
    '''
    for i in range(n,2,-1):
        if isPrime(i):
            return i
    return None

def test_get_largest_prime_below():
    assert get_largest_prime_below(14)==13

def get_age_in_days(birthday):
    '''
    Determina varsta persoanei in zile
    :param birthday: 3 nr. intregi
    :return: varsta in zile a unei persoane
    '''
    today = date.today()
    return today-birthday

#def test_get_age_in_days():
    #assert get_age_in_days(2002,4,25))==7104



def main():
    while True:
        print("1.Găsește ultimul număr prim mai mic decât un număr dat.")
        print("5.Determină dacă un număr dat este palindrom.")
        print("x. iesire din program ")
        optiune=input("alege optiunea :")
        if optiune=="1":
            n=int(input("Dati numarul :"))
            print(get_largest_prime_below(n))
        elif optiune == "2":
            birthday=date(2002,4,25)
            print(get_age_in_days(birthday))
        elif optiune=="x":
            break
        else:
            print("Optiune invalida")

test_get_largest_prime_below()
#test_get_age_in_days()
main()



