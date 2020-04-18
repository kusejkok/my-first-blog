# Date: 18.04.2020
# Practice Project: Table Printer

tableData = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]


def printTable():
    lenTableData = len(tableData)
    for i in range(lenTableData):
        lenInnerList = len(tableData[i])
        max = len(tableData[i][0])
        for j in range(1,lenInnerList):
            # max
            if len(tableData[i][j]) > max:
                max = len(tableData[i][j])
        for j in range(0,lenInnerList):
            tableData[i][j] = tableData[i][j].rjust(max)
    myStr = ""
    for j in range(0,lenInnerList):
        for i in range(0, lenTableData):
            myStr = myStr + " " + tableData[i][j]
        myStr = myStr + "\n"
    print(myStr)



printTable()
