import csv
import os.path



def compute_statistics(cars):

    total_value_cars = 0
    total_value_each_brand = []
    total_number_cars = 0

    for car in cars:
        total_value_cars += (car[2] * car[3])
        total_value_each_brand.append( (car[1], car[2]*car[3]) )
        total_number_cars += car[2]

    max_val = 0
    for brand in total_value_each_brand:
        if brand[1] > max_val:
            max_val = brand[1]
            brand_name = brand[0]
            
    total_max_value_brand = (brand_name, max_val)

    answer = (
            total_value_cars,           # valoarea totala a masinilor de pe stoc
            total_value_each_brand,     # valoarea totala a masinilor pentru fiecare brand
            total_number_cars,          # nr. total de masini din stoc
            total_max_value_brand       # brandul de pe stoc cu valoarea totala a masinilor cea mai mare
        )
    
    return answer
                
def generate_csv(cars):
    header = ['id', 'brand', 'items', 'price']

    with open('cars.csv', 'w') as csv_file:
        file_writer = csv.writer(csv_file)
        file_writer.writerow( header )

        for row in cars:
            file_writer.writerow(row)
         
    print("csv written successfuly")

def modify_csv_delimiter(input_csv_file):
    new_delimiter = ":"
    if os.path.exists(input_csv_file):
        
        with open(input_csv_file, mode="r") as infile:
            reader = csv.reader(infile)    
            with open("new_delimiter.csv", mode="w") as outfile:
                writer = csv.writer(outfile, delimiter=new_delimiter)
                writer.writerows(reader)
        print("New delimiter run with success")
    else:
        print("Path Error - file '" + input_csv_file + "' not found")


if __name__ == "__main__":
    
    cars = (
        (1, 'Audi', 8, 52642),
        (2, 'Mercedes', 6, 57127),
        (3, 'Skoda', 10, 19000),
        (4, 'Volvo', 4, 29000),
        (5, 'Bentley', 1, 350000),
        (6, 'Hummer', 2, 41400),
        (7, 'Volkswagen', 7, 21600),
        (8, 'Reanult', 10, 14000),
        (9, 'Dacia', 15, 8000),
        (10, 'Ford', 5, 15000)
        )


    ex1 = compute_statistics(cars)
    # print(ex1[0]) # valoarea totala a masinilor de pe stoc
    # print(ex1[1]) # valoarea totala a masinilor pentru fiecare brand
    # print(ex1[2]) # nr. total de masini din stoc
    # print(ex1[3]) # brandul de pe stoc cu valoarea totala a masinilor cea mai mare

        
    generate_csv(cars)

    dirpath = os.getcwd()
    modify_csv_delimiter(dirpath + "/cars.csv")

