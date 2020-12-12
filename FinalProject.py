# Donald Brown
# 1943301

import csv
from operator import itemgetter

# Main list to import all of the info
manufacturerinvlist = []
priceinvlist = []
sevicedateinvlist = []

# This will compile all of the information into the list lists just created
with open("ManufacturerList.csv") as manufactfurlist:
    ManufacturerList = csv.reader(manufactfurlist)
for line in ManufacturerList:
    manufacturerinvlist.append(line)
with open("PriceList.csv") as pricelist:
    ManufacturerList = csv.reader(pricelist)
for line in ManufacturerList:
    priceinvlist.append(line)
with open("ServiceDatesList.csv") as servucedatelist:
    ServiceDatesList = csv.reader(servucedatelist)
for line in ServiceDatesList:
    sevicedateinvlist.append(line)

# This will arrange the information ID to be sorted correctly
new_manufacturerinvlist = (sorted(manufacturerinvlist, key=itemgetter(0)))
new_priceinvlist = (sorted(priceinvlist, key=itemgetter(0)))
new_sevicedateinvlist = (sorted(sevicedateinvlist, key=itemgetter(0)))

# This will combime the prices no present and dates to the primary list
for i in range(0, len(new_manufacturerinvlist)):
    new_manufacturerinvlist[i].append(priceinvlist[i][1])
for i in range(0, len(new_manufacturerinvlist)):
    new_manufacturerinvlist[i].append(sevicedateinvlist[i][1])
final_inventory = new_manufacturerinvlist
complete_inventory = (sorted(final_inventory, key=itemgetter(1)))

# This will write the complete inventory
with open('FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)
for i in range(0, len(complete_inventory)):
    fiwrite.writerow(complete_inventory[i])

# This will make an inventory list for each item type or style that we have on the access documents
device_model_style = final_inventory
tower_inv = []
laptop_inv = []
phone_inv = []

# This willl look in each inventroy list for a specific type and then it will append them to their own lists/inv sheets
for i in range(0, len(device_model_style)):
    if device_model_style[i][2] == "computer_tower":
        tower_inv.append(device_model_style[i])
    elif device_model_style[i][2] == "mobile_phone":
        phone_inv.append(device_model_style[i])
    elif device_model_style[i][2] == "computer_laptop":
        laptop_inv.append(device_model_style[i])

# This will write files for every item type/style from the access documents
with open('LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)
for i in range(0, len(laptop_inv)):
    liwrite.writerow(laptop_inv[i])
with open('PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)
for i in range(0, len(phone_inv)):
    piwrite.writerow(phone_inv[i])
with open('TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)
for i in range(0, len(tower_inv)):
    tiwrite.writerow(tower_inv[i])

# This creats a damaged product inventroy list
damagedproductinv = []
for i in range(0, len(device_model_style)):
    if device_model_style[i][3] == "damaged":
        damagedproductinv.append(device_model_style[i])
damagedproductinv = (sorted(damagedproductinv, key=itemgetter(4), reverse=True))

# This will write the file for damaged inventory list
with open('DamagedInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)
for i in range(0, len(damagedproductinv)):
    diwrite.writerow(damagedproductinv[i])

# This will prompt the customer for style and type of product as well as manufacturer of said device
customer_manufacturer = str(input("Enter your manufacturer: "))
customer_device = str(input("Please enter your item type: "))
company_item = []

# Allow ‘q’ to quit the prompt
while (customer_manufacturer != "q"):
    for i in range(0, len(final_inventory)):
        if customer_manufacturer in final_inventory[i] and customer_device in final_inventory[i]:
            company_item.append(final_inventory[i])

# If nothing was added to the list print no such item
    if len(company_item) != 0:
        company_item = sorted(company_item, key=itemgetter(4), reverse=True)
        print("Your Item is: ", company_item[0])
    else:
        print("No such item in Inventory")
    customer_manufacturer = str(input("Enter your manufacturer, or q to exit query:"))
    customer_device = str(input("Please enter your item type: "))

# This will check all the items of same type/style and different manufacturer
    if(len(customer_manufacturer) != 0):
        customer_manufacturer = sorted(customer_manufacturer, key=itemgetter(4), reverse=True)
        print("You may also like ")