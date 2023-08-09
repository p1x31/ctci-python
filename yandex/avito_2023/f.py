from sys import stdin,stdout
from collections import Counter,deque,defaultdict

S = lambda: stdin.readline().strip()
M = lambda: map(str, stdin.readline().strip().split())
def rename_files(events, filenames):
    
    extension = ".jpg"
    new_filenames = []

    for filename in filenames:
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

        event = events[(year, month, day)]
        new_filename = f"{event}_{year}_{month}_{day}"
        new_filenames.append(new_filename)

    new_filenames.sort()
    
    counter = {}
    result = []
    for new_filename in new_filenames:
        if new_filename not in counter:
            counter[new_filename] = 1
        else:
            counter[new_filename] += 1
        
        new_imagename = f"{new_filename}_{str(counter[new_filename])}{extension}"
        result.append(new_imagename)
    
    return result

def main():
    events = {}
    for _ in range(3):
        event, year, month, day = M()
        events[(year, month, day)] = event
    
    filenames = []
    for _ in range(9):
        try:
            filename = S()
            filenames.append(filename)
        except EOFError:
            break
    
    new_filenames = rename_files(events, filenames)
    
    for new_filename in new_filenames:
        print(new_filename)
        
if __name__ == "__main__":
    main()