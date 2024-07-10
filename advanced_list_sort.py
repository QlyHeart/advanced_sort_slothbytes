# version 7/9/2024
# author "Queenly" for slothBytes

def advanced_sort(list):
    unique_elements = []
    sublists = []
    for element in list:
        if not unique_elements.__contains__(element):
            unique_elements.append(element)
    for element in unique_elements:
        sublist = []
        for i in range(len(list)):
            if list[i] == element:
                sublist.append(element)
        sublists.append(sublist)

    return sublists
        
def main():
    #test functionality
    int_list = [1, 2, "hallo", "slothbytes", "<3", 6, 7, "slothbytes", 10.1, 10, "2 ", '2', 3, "slothbytes", 5, 6, 7, 8, 9, 10]
    print(advanced_sort(int_list))

if __name__ == "__main__":
    main()
