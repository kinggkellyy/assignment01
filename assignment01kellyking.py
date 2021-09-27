# Name: Kelly King
# Course: CS151, Prof. Mehri
# Date: [September 27,2021]
# Programming Assignment: 1
# Program Inputs: [the dimensions (length,width, and height of a room in feet]
# Program Outputs: [total area of four walls and ceiling to determine the amount of primer and paint needed in gallons]
#1 set variables: length, width, height, gallons in primer, gallons in paint
#2 ask user for length, width, and height in feet
#3 output: area of four walls and ceiling determines amount of primer and paint needed

#Algorithim:
#1:
length = int(input("please insert length in ft:"))

#2:
width = int(input("please insert width in ft:"))

#3
height = int(input("please insert height in ft:"))

#4
area = 2*(length + width)*height
gallons_in_primer = (area/200)

#5
gallons_in_paint = (area/350)

#6
print ("the area of the four walls and ceiling",area, "amount of paint", gallons_in_paint, "amount of primer", gallons_in_primer)


