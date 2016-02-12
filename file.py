
def readfile(path, flags='rb'):
    with open(path, flags) as rh:
        for line in rh:
            yield line

if __name__ == '__main__':
    txt = ''.join(line for line in readfile(__file__))
    print(txt)
