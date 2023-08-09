
def main():
    # Считывание данных из файла input.txt
    with open("input.txt", "r") as file:
        data = file.readline().split()

    # Извлечение количества построек и списка высот
    num_buildings = int(data[0])
    heights = list(map(int, data[1:]))

    # Нахождение индекса самой низкой постройки
    lowest_index = heights.index(min(heights))
    
    # Разделение списка высот на две части
    first_half = heights[:lowest_index]
    second_half = heights[lowest_index:]

    # Нахождение максимальной высоты в каждой части
    max_height_1 = max(first_half)
    max_height_2 = max(second_half)

    # Выбор минимальной из двух максимальных высот
    max_zip_line_height = min(max_height_1, max_height_2)

    # Запись минимальной высоты в файл output.txt
    with open("output.txt", "w") as file:
        file.write(str(max_zip_line_height))

if __name__ == "__main__":
    main()  