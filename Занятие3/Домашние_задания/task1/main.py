import json

if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    filename_1 = "input_1.json"
    filename_2 = "input_2.json"
    filename_3 = "output.json"

    with open(filename_1, 'w') as f_1:
        json_data_1 = json.dumps(list_1)
        f_1.write(json_data_1)
        print(json.dumps(list_1))
        
    with open(filename_2, 'w') as f_2:
        json_data_2 = json.dumps(list_2)
        f_2.write(json_data_2)

    with open(filename_1, 'r') as file_1:
        with open(filename_2, 'r') as file_2:
            with open(filename_3, 'w') as file_3:
                json_data_3 = json.dumps(json.load(file_1) + json.load(file_2))
                file_3.write(json_data_3)
