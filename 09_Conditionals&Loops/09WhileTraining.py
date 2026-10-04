#------------------------------------------------------
# While Loop Training
#---------------
# 
#------------------------------------------------------


names = ["AB", "CD", "EF", "GH", "IJ", "KL", "MN", "OP", "QR", "ST", "UV", "WX", "YZ"]

print(len(names))  # list length

index = 0

while index < len(names):
    print(f"{str(index + 1).zfill(2)}. {names[index]}")
    index += 1