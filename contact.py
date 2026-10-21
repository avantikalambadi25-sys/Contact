
import csv

file = open("contacts.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["Name", "Phone"])
writer.writerow(["Avantika", "9876543210"])
writer.writerow(["Gungun", "9876543211"])
writer.writerow(["Anjali", "9876543212"])
writer.writerow(["Aman", "9876543213"])
writer.writerow(["Rahul", "9876543214"])

file.close()

file = open("contacts.csv", "r")
reader = csv.DictReader(file)

for row in reader:
    if row["Name"].startswith("A"):
        print(row["Name"], row["Phone"])

file.close()
