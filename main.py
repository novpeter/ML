import matplotlib.pyplot as plt
import csv


def draw_height_and_gender_bar(path):
    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        women_heights = []
        men_heights = []

        for row in reader:
            if row['gender'] == 'Female':
                women_heights.append(int(float(row['height'])))
            else:
                men_heights.append(int(float(row['height'])))

        women_average_height = 0
        men_average_height = 0

        if len(women_heights) != 0:
            women_average_height = sum(women_heights) / len(women_heights)

        if len(men_heights) !=0:
            men_average_height = sum(men_heights) / len(men_heights)

        column_names = ["W", "M"]
        average = [women_average_height, men_average_height]
        plt.bar(column_names, average)
        plt.show()


if __name__ == '__main__':
    draw_height_and_gender_bar('files/MOCK_DATA.csv')
