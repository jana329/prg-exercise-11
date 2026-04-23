import random

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

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

    print(selection_sort(random_numbers(20)))



