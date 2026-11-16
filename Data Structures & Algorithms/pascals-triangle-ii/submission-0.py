class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """
        We are given a row number and we have to return the pascal's triangle row for that specific row. We could just apply a formula and return it that way, where the result is just the answer for that layer, however, there is another way that we can do it, by carrying instead of appending. If we have a temp variable, that creates the nex layer while final_row has the old values and over writes them, then we can create all of the rows. There is another way to do it where we don't use temp, and actually use the values already in final_row, and overwrite final_row as we go ,a dn we would have to do this left to right because we would be replacing old values, buch each value in the middle is used 2 times instead of 1, so we'd have to be careful about when we repace it,s o this is the safeset method. 
        """
        row = [1]

        for i in range(rowIndex):
            row.append(1)
            for j in range(len(row) - 2, 0, -1):
                row[j] += row[j - 1]
        return row
                