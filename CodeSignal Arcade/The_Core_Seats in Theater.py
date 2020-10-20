def seatsInTheater(nCols, nRows, col, row):
    return (nRows - row) * (nCols - (col - 1))