import pandas as pd
import statistics

df = pd.read_csv("color.csv")

total_green_shirt = int(sum(df["green"]))
total_yellow_shirt = int(sum(df.fillna(0)["yellow"]))
total_blue_shirt = int(sum(df["blue"]))
total_pink_shirt = int(sum(df.fillna(0)["pink"]))
total_orange_shirt = int(sum(df["orange"]))
total_cream_shirt = int(sum(df.fillna(0)["cream"]))
total_red_shirt = int(sum(df["red"]))
total_white_shirt = int(sum(df["white"]))
total_brown_shirt = int(sum(df["brown"]))
total_ash_shirt = int(sum(df.fillna(0)["ash"]))
total_black_shirt = int(sum(df.fillna(0)["black"]))

print(f"The total number of Yellow shirt wore is {total_yellow_shirt}")
print(f"The total number of Blue shirt wore is {total_blue_shirt}")
print(f"The total number of Pink shirt wore is {total_pink_shirt}")
print(f"The total number of Red shirt wore is {total_red_shirt}")
print(f"The total number of Green shirt wore is {total_green_shirt}")
print(f"The total number of White shirt wore is {total_white_shirt}")
print(f"The total number of Black shirt wore is {total_black_shirt}")
print(f"The total number of Cream shirt wore is {total_cream_shirt}")
print(f"The total number of Ash shirt wore is {total_ash_shirt}")
print(f"The total number of Brown shirt wore is {total_brown_shirt}")
print(f"The total number of Orange shirt wore is {total_orange_shirt}")

List_of_colors_wore = [total_green_shirt, total_yellow_shirt, total_blue_shirt, total_pink_shirt,
                        total_orange_shirt, total_cream_shirt, total_red_shirt, total_brown_shirt,
                         total_white_shirt, total_ash_shirt, total_black_shirt]

mean = statistics.mean(List_of_colors_wore)
median = statistics.median(List_of_colors_wore)
shirt_most_wore = max(List_of_colors_wore)


print(f"The mean value of shirt color is {mean}. Therefore, the mean color is Brown")
print(f"Blue color shirt was wore {shirt_most_wore} times. Therefore, the most wore shirt color is Blue")
print(f"The Median value of shirt color is {median}. Therefore, the median color is Brown")


