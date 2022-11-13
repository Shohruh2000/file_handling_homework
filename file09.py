def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data.split("\n")
    list1 = []
    for i in data.split("n"):
        for j in range(len(i)):
            if str(i[j]).isdigit():
                list1 +=i[j]
    n = len(list1)
    k = 0 
    min = list1[0]
    for k in range(n):
        if list1[k] < min:
            min = list1[k]
    return min

# Read data from file
f = open("txt_file/data09.txt").read()
print(main(f))