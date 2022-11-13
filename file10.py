def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data.split("\n")
   
    ls = []
    ls1 = []
    ls = data.split("\n")
    for i in ls:
        ls1.append(len(i))
        max = ls1[0]
        n = len(ls1)
        j = 0
    for j in range(n):
        if ls1[j] > max:
            max = ls1[j]
    return max

# Read data from file
f = open("txt_file/data10.txt").read()
print(main(f))