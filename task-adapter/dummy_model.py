import sys

import pandas

def main(a: str, b: str, data_csv_path: str) -> float:
    """
    Takes 2 parameters `a` and `b` as row/column indexes (a,b and b,a), 
    and returns the sum of the 2 values found in the csv file
    """
    data = pandas.read_csv(data_csv_path, header=None)
    return data.iloc[int(a), int(b)] + data.iloc[int(b), int(a)]


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
