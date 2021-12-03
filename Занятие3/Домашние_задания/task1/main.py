import json

if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    filename_1 = "input_1.json"
    filename_2 = "input_2.json"

    with open(filename_1, 'x') as f_1:
        json_data = json.dumps(list_1, indent=4)
        
    # with open(filename_2, 'x') as f_2:
    #     f_2.write(list_2)