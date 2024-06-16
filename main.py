from tkinter import *
from tkinter import ttk
from time import sleep
import logging
# import pyodbc
from colorama import Fore
from tkinter.filedialog import asksaveasfile, askopenfile
import csv as c
import random
import os
import sys
import threading
import time
from tkinter import messagebox
from tkinter import font

ItemsList = []
tempInitiateList = []
tempInitiateList.append("Tornos")
tempInitiateList.append("Mechanical Tool")
tempInitiateList.append(2)
tempInitiateList.append("Brand New")
tempInitiateList.append("https://zissiskainicktornos.gr")
ItemsList.append(tempInitiateList)
currentItemsInTable = 1

logging.basicConfig(filename='workShopData.csv', level=logging.INFO, format='%(asctime)s,%(message)s',
                    datefmt='%I:%M:%S')
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (9 * width / 10, height))
font_width = int(width / 90)
main_frame = Frame(root)
main_frame.grid(row=0, column=0, sticky=NSEW)
title = Label(main_frame, text='Workshop Counter', font=("Arial", int(width / 35)), fg="blueviolet")
items = ttk.Treeview(main_frame, height=36, padding=10)
items['show'] = 'headings'
items.tag_configure('oddrow', background='gray90')
items.tag_configure('evenrow', background='white')

AddItemPage = Frame(root)
AddItemPage.grid(row=0, column=0, sticky=NSEW)

AddPageDescription = Frame(AddItemPage)
AddPageDescription.grid(row=0, column=1, sticky=NSEW)
AddPageDescriptionLabel = Label(AddPageDescription, text="Enter Description of item:", font=("Helvetica"))
AddPageDescriptionEntry = Entry(AddPageDescription, width=20, font=("Helvetica"))
AddPageDescriptionEntry.grid(row=1, column=2)
AddPageDescriptionLabel.grid(row=1, column=1)

AddPageFieldLabel = Label(AddPageDescription, text="Enter Field:", font=("Helvetica"))
AddPageFieldEntry = Entry(AddPageDescription, width=20, font=("Helvetica"))
AddPageFieldLabel.grid(row=2, column=1)
AddPageFieldEntry.grid(row=2, column=2)

AddPageQuantityLabel = Label(AddPageDescription, text="Enter Quantity:", font=("Helvetica"))
AddPageQuantityEntry = Entry(AddPageDescription, width=20, font=("Helvetica"))
AddPageQuantityLabel.grid(row=3, column=1)
AddPageQuantityEntry.grid(row=3, column=2)

AddPageConditionLabel = Label(AddPageDescription, text="Enter Condition:", font=("Helvetica"))
AddPageConditionEntry = Entry(AddPageDescription, width=20, font=("Helvetica"))
AddPageConditionLabel.grid(row=4, column=1)
AddPageConditionEntry.grid(row=4, column=2)

AddPageDataSheetLabel = Label(AddPageDescription, text="Enter Datasheet/Manual Link:", font=("Helvetica"))
AddPageDataSheetEntry = Entry(AddPageDescription, width=20, font=("Helvetica"))
AddPageDataSheetLabel.grid(row=5, column=1)
AddPageDataSheetEntry.grid(row=5, column=2)


def addItemInItems():
    global itemsList, currentItemsInTable
    currentItemsInTable += 1
    tempList = []
    tempList.append(AddPageDescriptionEntry.get())
    tempList.append(AddPageFieldEntry.get())
    tempList.append(AddPageQuantityEntry.get())
    tempList.append(AddPageConditionEntry.get())
    tempList.append(AddPageDataSheetEntry.get())
    ItemsList.append(tempList)
    # ItemsList[int(currentItemsInTable)][0] = str(currentItemsInTable)
    # ItemsList[int(currentItemsInTable)][1] = AddPageDescriptionEntry.get()
    # ItemsList[int(currentItemsInTable)][2] = AddPageFieldEntry.get()
    # ItemsList[int(currentItemsInTable)][3] = AddPageQuantityEntry.get()
    # ItemsList[int(currentItemsInTable)][4] = AddPageConditionEntry.get()
    updateValues()


AddPageButtonDone = Button(AddPageDescription, text="Add", command=addItemInItems)
AddPageButtonDone.grid(row=6, column=2)

AddPageCancelButton = Button(AddPageDescription, text="Cancel", command=main_frame.tkraise)
AddPageCancelButton.grid(row=6, column=1)

EditItemPage = Frame(root)
EditItemPage.grid(row=0, column=0, sticky=NSEW)

EditPageDescription = Frame(EditItemPage)
EditPageDescription.grid(row=0, column=1, sticky=NSEW)
EditPageSelectItemMenuLabel = Label(EditPageDescription, text="Select the item to edit")
EditPageSelectItemMenuLabel.grid(row=1, column=1)
EditPageSelectItemVariable = StringVar(EditItemPage)
EditPageSelectList = ["1"]

# EditPageSelectItemMenu = OptionMenu(EditPageDescription, EditPageSelectItemVariable,*EditPageSelectList)
# EditPageSelectItemMenu.config(width=100, font=("Helvetica", 10))
# EditPageSelectItemMenu.grid(row=1, column=2)

EditPageSelectItemLabel = Label(EditPageDescription, text="Which item want to edit(1-36):", font=("Helvetica"))
EditPageSelectItemEntry = Entry(EditPageDescription, width=20, font=("Helvetica"))
EditPageSelectItemEntry.grid(row=1, column=2)
EditPageSelectItemLabel.grid(row=1, column=1)

EditPageDescriptionLabel = Label(EditPageDescription, text="Enter Description of item:", font=("Helvetica"))
EditPageDescriptionEntry = Entry(EditPageDescription, width=20, font=("Helvetica"))
EditPageDescriptionEntry.grid(row=2, column=2)
EditPageDescriptionLabel.grid(row=2, column=1)

EditPageFieldLabel = Label(EditPageDescription, text="Enter Field:", font=("Helvetica"))
EditPageFieldEntry = Entry(EditPageDescription, width=20, font=("Helvetica"))
EditPageFieldLabel.grid(row=3, column=1)
EditPageFieldEntry.grid(row=3, column=2)

EditPageQuantityLabel = Label(EditPageDescription, text="Enter Quantity:", font=("Helvetica"))
EditPageQuantityEntry = Entry(EditPageDescription, width=20, font=("Helvetica"))
EditPageQuantityLabel.grid(row=4, column=1)
EditPageQuantityEntry.grid(row=4, column=2)

EditPageConditionLabel = Label(EditPageDescription, text="Enter Condition:", font=("Helvetica"))
EditPageConditionEntry = Entry(EditPageDescription, width=20, font=("Helvetica"))
EditPageConditionLabel.grid(row=5, column=1)
EditPageConditionEntry.grid(row=5, column=2)

EditPageDataSheetLabel = Label(EditPageDescription, text="Enter Datasheet/Manual Link:", font=("Helvetica"))
EditPageDataSheetEntry = Entry(EditPageDescription, width=20, font=("Helvetica"))
EditPageDataSheetLabel.grid(row=6, column=1)
EditPageDataSheetEntry.grid(row=6, column=2)
def EditItemInItems():
    print("a")

    updateValues()

EditPageButtonDone = Button(EditPageDescription, text="Edit", command=EditItemInItems)
EditPageButtonDone.grid(row=7, column=2)

EditPageCancelButton = Button(EditPageDescription, text="Cancel", command=main_frame.tkraise)
EditPageCancelButton.grid(row=7, column=1)

def addItemClicked():
    print("addItem")
    AddItemPage.tkraise()


def editItemClicked():
    print("editItem")
    EditItemPage.tkraise()

def deleteItemClicked():
    global currentItemsInTable
    print("Delete Last Item")
    currentItemsInTable -= 1
    ItemsList.pop()
    updateValues()
def exportCSVClicked():
    print("exportCSV")
    files = [('CSV Files', '*.csv'), ('Text Files', '*.txt')]
    exportfile = asksaveasfile(filetypes = files, defaultextension = files,)
    exportwriter = c.writer(exportfile)
    firstRow = ["Item Description", "Field", "Quantity", "Condition", "Datasheet / Manual Link"]
    exportwriter.writerow(firstRow)
    exportwriter.writerows(ItemsList)
def importCSVClicked():
    global ItemsList, currentItemsInTable
    print("importCSV")
    importFile = askopenfile(mode='r', filetypes =[('Text Files', '*txt'), ('CSV Files', '*.csv')])
    ItemsList.clear()
    currentItemsInTable = 0
    if importFile is not None:
        next(importFile)
        for importItems in importFile.readlines():
            importItems = importItems.replace("\n","")
            ItemsList.append(importItems.split(","))
        currentItemsInTable = len(ItemsList)
        updateValues()

menubar = Menu()
csv = Menu(menubar, tearoff=False)

csv.add_command(
    label="Add Item",
    accelerator="Ctrl+A",
    command=addItemClicked

)
csv.add_command(
    label="Edit Item",
    accelerator="Ctrl+E",
    command=editItemClicked

)
csv.add_command(label="Delete Last Item", accelerator="Ctrl+D", command=deleteItemClicked)
csv.add_separator()
csv.add_command(
    label="Export CSV",
    accelerator="Ctrl+S",
    command=exportCSVClicked
)
csv.add_command(
    label="Import CSV",
    accelerator="Ctrl+O",
    command=importCSVClicked

)
csv.add_separator()
csv.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(menu=csv, label="Settings")

title.pack(anchor=CENTER, fill=BOTH)
items.pack(anchor=CENTER, fill=BOTH)

# Global List




def updateValues():
    global currentItemsInTable
    # AddPageDescriptionEntry.insert(0," ")
    # AddPageFieldEntry.insert(0," ")
    # AddPageQuantityEntry.insert(0," ")
    # AddPageConditionEntry.insert(0," ")
    # AddPageDataSheetEntry.insert(0," ")
    # EditPageSelectItemVariable.set('')
    # EditPageSelectItemMenu["Menu"].delete(0, 'end')
    # newItemsNamesInMenu = []
    # for i in range(len(ItemsList)):
    #     newItemsNamesInMenu.append(ItemsList[i][0])
    # for item in newItemsNamesInMenu:
    #     EditPageSelectItemMenu["Menu"].add_command(label=item, command=tkinter._setit(EditPageSelectItemVariable, item))
    # conn = pyodbc.connect('DRIVER= {ODBC Driver 18 for SQL Server}; \
    #                         SERVER=MSSQLLocalDB; \
    #                         DATABASE=Christopher_Kirkwood_DB; \
    #                         Trust_Connection=yes')

    main_frame.tkraise()
    for item in items.get_children():
        items.delete(item)
    print(currentItemsInTable)
    # currentItemsInTable = len(ItemsList)
    # print(currentItemsInTable)

    print(ItemsList)
    for i in range(0, currentItemsInTable):
        # print(VoltageList[i])
        # print(TempsList[i])
        if i % 2:
            tag = 'oddrow'
        else:
            tag = 'evenrow'
        items.insert(parent='', index='end', tags=tag, text='',
                     values=(str(i + 1),
                             ItemsList[i][0],
                             ItemsList[i][1],
                             ItemsList[i][2],
                             ItemsList[i][3],
                             ItemsList[i][4]
                             )
                     )


def guiInit():
    root.iconname('Workshop Counter')
    root.title("Workshop Counter")
    percent_width = int(width / 7)
    items['columns'] = ("Item Number", 'Item Description', 'Field', 'Quantity', 'Condition', 'Datasheet / Manual Link')
    items.column("Item Number", anchor=CENTER, width=percent_width)
    items.column("Item Description", anchor=CENTER, width=percent_width)
    items.column("Field", anchor=CENTER, width=percent_width)
    items.column("Quantity", anchor=CENTER, width=percent_width)
    items.column("Condition", anchor=CENTER, width=percent_width)
    items.column("Datasheet / Manual Link", anchor=CENTER, width=percent_width)

    items.heading("Item Number", text="Item Number", anchor=CENTER)
    items.heading("Item Description", anchor=CENTER, text="Item Description")
    items.heading("Field", anchor=CENTER, text="Field")
    items.heading("Quantity", anchor=CENTER, text="Quantity")
    items.heading("Condition", anchor=CENTER, text="Condition")
    items.heading("Datasheet / Manual Link", anchor=CENTER, text="Datasheet / Manual Link")

    updateValues()
    root.config(menu=menubar)
    main_frame.tkraise()
    root.mainloop()


if __name__ == '__main__':
    print("a")
    guiInit()
