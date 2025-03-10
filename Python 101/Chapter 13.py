import csv

def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter = ',')
    for line in reader:
        print(line['country'])
        print(line['iso2'])

def csv_writer(data,path):
    with open(path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file,delimiter = ',')
        for line in data:
            writer.writerow(line)

def csv_dict_writer(path, fieldnames, data):
    with open(path,'w',newline='') as out_file:
        writer = csv.DictWriter(out_file,delimiter=",",fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    data = ["first_name, last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport,".split(","),
            "Jules,Dicki,Lake Nickelasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list=[]
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

    path = "dict_output.csv"
    csv_dict_writer(path,fieldnames,my_list)