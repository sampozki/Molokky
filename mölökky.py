#Sampozki 2018
import time
import matplotlib.pyplot as plt


def isnumber(text):
    while True:
        x = input(text)
        if x.isdigit():
            return int(x)
        else:
            print("Please enter a number.")


def plot(pelaajat, kierroslista):
    for i in pelaajat:
        plt.plot(kierroslista, pelaajat[i], label=str(i))
    plt.title('Mölökky')
    plt.ylabel('Points')
    plt.xlabel('Rounds')
    plt.ylim(0, 50)
    plt.xlim(0, max(kierroslista))
    plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
    plt.show()


def main():
    start = time.time()
    n = isnumber("Player amount: ")
    kierros, kierroslista = 0, [0]
    pelaajat = {}
    game = True
    for e in range(0, n):
        pelaajat[input("Player " + str(len(pelaajat) + 1) + " name: ").capitalize()] = [0]
    while game:
        kierros += 1
        kierroslista.append(kierros)
        for a in pelaajat:
            amount = pelaajat[a][-1] + isnumber(a + ": ")
            if amount > 50:
                amount = 25
            if amount == 50:
                pelaajat[a].append(50)
                print(a + " is the winner!")
                print("The game took: {:02.1f} minutes.".format((time.time() - start)/60))
                for o in pelaajat:
                    if len(pelaajat[o]) < len(pelaajat[a]):
                        pelaajat[o].append(pelaajat[o][-1])
                plot(pelaajat, kierroslista)
                game = False
            pelaajat[a].append(amount)
        for o in pelaajat:
            print(o + ": " + str(pelaajat[o][-1]), end=", ")
        print("\n")


if __name__ == '__main__':
    main()
