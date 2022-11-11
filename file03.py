def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data.split()
    list1 = []
    for i in data:
        for j in range(len(i)):
            if str(i[j]).isdigit():
                list1 +=i[j]
    
    return list1
    
# Read data from file
f = open("txt_file/data03.txt").read()
print(main(f))

