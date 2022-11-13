def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer   The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ls = []
    ls = data.split("\n")
    ls2 = []

    for i in ls:
        ls2.append(len(i))

            

    return ls2

   
# Read data from file
f = open("txt_file/data06.txt").read()
print(main(f))