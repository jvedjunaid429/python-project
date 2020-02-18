row1_column1 = "x"
row1_column2 = "o"
row1_column3 = " "
row2_column1 = "x"
row2_column2 = "x"
row2_column3 = " "
row3_column1 = "o"
row3_column2 = " "
row3_column3 = " "
​
print("       |       |       ")
print("   {}   |   {}   |   {}   ".format(row1_column1, row1_column2, row1_column3))
print("       |       |       ")
print("-------+-------+-------")
print("       |       |       ")
print("   {}   |   {}   |   {}   ".format(row2_column1, row2_column2, row2_column3))
print("       |       |       ")
print("-------+-------+-------")
print("       |       |       ")
print("   {}   |   {}   |   {}  ".format(row3_column1, row3_column2, row3_column3))
print("       |       |       ")
​
if topleft == ("X") and topcentre == ("X") and topright == ("X"):
    print("winner".)
