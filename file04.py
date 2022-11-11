def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data.split()
    ls = []
    for i in data:
        for j in range(len(i)):
            if str(i[j]).isalpha():
                ls +=i[j]
    return ls
# Read data from file
f = open("txt_file/data04.txt").read()
print(main(f))