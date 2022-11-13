def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
    data.split("\n: :.")
    ls = []
    for i in data:
        for j in range(len(i)):
            if str(i[j]).isdigit():
                ls +=i[j]
    max = ls[0]
    k = 0
    for i in range(len(ls)):
        if ls[i]>max:
            max = ls[i]
    return max

# Read data from file
f = open("txt_file/data08.txt").read()
print(main(f))