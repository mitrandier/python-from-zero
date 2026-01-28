a = input("Hi enter the row and column number between 1,2,3 like 13 or 22: " )
horizontal = int(a[0])
vertical = int(a[1])
#print(horizontal, type(horizontal))
#print(vertical, type(vertical))

if horizontal >=4 and vertical >=4:
    a = input("please enter the row and column number between 1,2,3 like 13 or 22: " )
    horizontal = int(a[0])
    vertical = int(a[1])
    #print(horizontal, type(horizontal))
    #print(vertical, type(vertical))

row1=["⬜ ","⬜ ","⬜ "]
row2=["⬜ ","⬜ ","⬜ "]
row3=["⬜ ","⬜ ","⬜ "]
map = [row1,row2, row3]

#selected_row = map[vertical-1]
#selected_row[horizontal-1] = " x "

map[vertical-1][horizontal-1] = " x "

print(f"{row1}\n{row2}\n{row3}")
