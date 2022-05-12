import csv

list_of_links = []

with open("filenames.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        text = row[0].replace("\\", "/")
        text = "https://drive.my-elibrary.com" + text + "\n"

        list_of_links.append(text)

with open("links.csv", "w") as linkfile:

    linkfile.writelines(list_of_links)

    print("Done")


