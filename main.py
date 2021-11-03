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
    :param birthday: lista ce contine data nasterii, de forma DD/MM/YYYY
    :return: varsta in zile a unei persoane (aid)
    '''
    # ziua, luna si anul nasterii
    bd = int(birthday[0:2])
    bm = int(birthday[3:5]) - 1
    by = int(birthday[6:10])
    today = "03/11/2021"

    # ziua, luna si anul din prezent
    td = int(today[0:2])
    tm = int(today[3:5])
    ty = int(today[6:10])
    aid = 0
    month = [31, 29, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]

    # adaugam zilele trecute din anul curent
    aid = aid + td
    for i in range(0, tm):
        aid = aid + month[i]

    # adaugam zilele trecute din anii trecuti
    aid = aid + (month[bm] - bd)
    for i in range(bm+1, 12):
        aid = aid + month[i]

    # adaugam zilele din anii ramasi
    for i in range(by+1, ty):
        if i % 4 == 0:
            aid = aid + 366
        else:
            aid = aid + 365
    return aid

def test_get_age_in_days():
    assert get_age_in_days("25/04/2002") == 7162


def is_palindrome(n):
    '''
    Determină dacă un număr dat este palindrom
    :param n: nr. intreg
    :return: True daca numarul este palindrom si False daca numarul nu este palindrom
    '''
    oglindit =0
    copie_n =n
    while copie_n != 0:
        oglindit= oglindit * 10 + copie_n % 10
        copie_n = copie_n // 10
    if n==oglindit:
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(237) is False

def main():
    while True:
        print("1.Găsește ultimul număr prim mai mic decât un număr dat.")
        print("2.Determina vârsta persoanei în zile")
        print("5.Determină dacă un număr dat este palindrom.")
        print("x. iesire din program ")
        optiune=input("alege optiunea :")
        if optiune=="1":
            n=int(input("Dati numarul :"))
            print(get_largest_prime_below(n))
        elif optiune == "2":
            birthday = input("Introduceti data nasterii, in formatul DD/MM/YYYY : ")
            print(get_age_in_days(birthday))
        elif optiune=="5":
            n=int(input("Dati numarul :"))
            print(is_palindrome(n))
        elif optiune=="x":
            break
        else:
            print("Optiune invalida")

test_get_largest_prime_below()
test_get_age_in_days()
test_is_palindrome()
main()



