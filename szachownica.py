print("This app check whether the queen can move from the first field to the second in one move.")

while True:
    field_1_col = int(input("Enter first column number(1-8): "))
    if (field_1_col>0 and field_1_col<=8):
        break

while True:
    field_1_row = int(input("Enter first row number(1-8): "))
    if (field_1_row>0 and field_1_row<=8):
        break

while True:
    field_2_col = int(input("Enter second column number(1-8): "))
    if (field_2_col>0 and field_2_col<=8):
        break    

while True:
    field_2_row = int(input("Enter second row number(1-8): "))
    if (field_2_row>0 and field_2_row<=8):
        break

if field_1_row == field_2_row or field_1_col == field_2_col or abs(field_1_row - field_2_row) == abs(field_1_col - field_2_col):
    print("Yes, the queen can move from the first field to the second in one move")
else:
    print("No, the queen can move from the first field to the second in one move")

