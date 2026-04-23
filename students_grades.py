from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.get_by_index(index)

        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, hledane_body):
        nalezene_indexy = []

        for i in range(len(self.scores)):
            if self.scores[i] == hledane_body:
                nalezene_indexy.append(i)

        return nalezene_indexy

    def get_sorted(self):
        kopie_skore = self.scores[:]
        n = len(kopie_skore)

        for i in range(n):
            for j in range(0, n - i - 1):
                if kopie_skore[j] > kopie_skore[j + 1]:
                    kopie_skore[j], kopie_skore[j + 1] = kopie_skore[j + 1], kopie_skore[j]

        return kopie_skore

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(f"počet studentů, kteří psali test: {results.count()}")

    for i in range(results.count()):
        body = results.get_by_index(i)
        znamka = results.get_grade(i)

        print(f"Student{i}:  {body} points - {znamka}")
        print("--------------------------------------------------")
        print(f"indexy studentu se 100 body: {results.find(100)}")
        print("--------------------------------------------------")
        print(f"seřazené výsledky: {results.get_sorted()}")
        print("--------------------------------------------------")
        print("test na nahodnych datech:")
        random_results = StudentsGrades(random_numbers(30, 0, 100))
        print(f"pocet studentu - nahodny: {random_results.count()}")
        print(f"seřazené náhodné výsledky: {random_results.get_sorted()}")



if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(f"{results.get_grade(2)}")
    print(f"{results.get_grade(7)}")

    print(results.find(100))
    print(results.find(67))

    print(results.get_sorted())
    print(results.scores)

    main()