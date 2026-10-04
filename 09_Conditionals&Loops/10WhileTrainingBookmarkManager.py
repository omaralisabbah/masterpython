#------------------------------------------------------
# While Training Bookmark Manager
#--------------------------------
# 
#------------------------------------------------------


Websites_Bookmarks = []

Bookmarks_number = 10

index = 0

while Bookmarks_number > 0:
    website = input("Website name with out https:// ")
    Websites_Bookmarks.append(f"https://{website.strip().lower()}") 
    Bookmarks_number -= 1
    print(f"Website Added <3, {Bookmarks_number} Left of the bookmarks available ")
    print(Websites_Bookmarks)

else:
    print("Bookmarks bar is full!!")


if len(Websites_Bookmarks) > 0:
    Websites_Bookmarks.sort()
    index = 0
    print