def func(a: str) -> str:
    '''
    принимает в качестве аргумента путь до очень большого файла (размер может быть 100Гб) и добавляющую в начало каждой строки этого файла порядковый номер этой строки.
    '''
    input_file = "/home/user/Doc/.../input_file"
    a = input_file
    with open(input_file, "rb") as fr:
        with open("output.txt", "wb") as fw:
            for i, line in enumerate(lines):
                fw.write(str(i + 1) + ' ' + line)
            fw.close()
    fr.close()
    return input_file
    