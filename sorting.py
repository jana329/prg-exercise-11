import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(seznam_cisel):
    seznam_kopie = seznam_cisel.copy()
    n = len(seznam_cisel)

    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if seznam_kopie[j] < seznam_kopie[min_i]:
                min_i = j

        seznam_kopie[i], seznam_kopie[min_i] = seznam_cisel[min_i], seznam_kopie[i]

    return seznam_kopie

def bubble_sort(seznam_cisel):

    seznam_kopie = seznam_cisel.copy()
    n = len(seznam_cisel)

    plt.ion()
    plt.show()

    for i in range(n):
        for j in range(0, n - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(seznam_kopie)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(seznam_kopie)), seznam_kopie, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if seznam_kopie[j] > seznam_kopie[j + 1]:

                seznam_kopie[j], seznam_kopie[j + 1] = seznam_kopie[j + 1], seznam_kopie[j]

    plt.ioff()
    plt.show()

    return seznam_kopie


if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

    test_kratky = [5, 1, 4, 2, 8]
    test_nahodny = random_numbers(20)

    print(f"kratky pred serazenim: {test_kratky}")
    print(f"test kratky po serazeni: {selection_sort(test_kratky)}")

    print(f"random pred serazenim: {test_nahodny}")
    print(f"random po serazeni: {selection_sort(test_nahodny)}")

    bubble = bubble_sort(random_numbers(10))
    print(bubble)


