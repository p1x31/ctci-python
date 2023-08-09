from sys import stdin,stdout
S = lambda: stdin.readline().strip()

def rename_file(filename):
    prefix = "DRIFT"
    year = filename[4:8]
    month = filename[8:10]
    day = filename[10:12]
    extension = filename[-3:]
    
    new_filename = f"{prefix}_{year}_{month}_{day}.{extension}"
    return new_filename

def main():
    filename = S()
    new_filename = rename_file(filename)
    print(new_filename)

if __name__ == "__main__":
    main()