from sys import stdin,stdout
S = lambda: stdin.readline().strip()

def rename_file(filename):
    year = ""
    month = ""
    day = ""
    prefix_d = "DRIFT"
    extension = ".jpg"
   
    if filename.startswith("DCIM"):
        # DCIM-2023-04-30-1.jpg
        parts = filename.split("-")
        year = parts[1]
        month = parts[2]
        day = parts[3].split(".")[0]
    elif filename.startswith("PXL"):
        # PXL_20230430_092422111.jpg
        parts = filename.split("_")
        year = parts[1][:4]
        month = parts[1][4:6]
        day = parts[1][6:8]
    else:
        # 202304300924-1.jpg
        year = filename[:4]
        month = filename[4:6]
        day = filename[6:8]

    if year and month and day:
        new_filename = f"{prefix_d}_{year}_{month}_{day}{extension}"
        return new_filename
    else:
        return None


def main():
    filename = S()
    new_filename = rename_file(filename)
    print(new_filename)

if __name__ == "__main__":
    main()