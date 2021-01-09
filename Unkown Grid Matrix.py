#┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬
#||||||||||||||||||||||| Decriptions ||||||||||||||||||||||||||
#┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴


#═════════════════════════ General ══════════════════════════════════

"""
    ***Note:Some of the examples are wrong to show how the program works. 
    The software display an error, so do not forget to comment them.***


    The software can find the answer of n×n boxes with n×n cells. 
    The target of the software is assigning numbers with minimum 
    possible options. All information related to the functions and 
    variable can be found below:
"""

#════════════════════════ Variables ═════════════════════════════════

"""
*** Note: Every variable that starts with 'i' is used for iteration.

1. Sudoku_cells ──────> It is a 2-dimensional list to store the 
    number of cells in each box. The elements will be received 
    by user. 
    The first room is for the number of cells in a row
    and the second one is for the number of cells in a column


2. Sudoku_box ──────> It is a 2-dimensional list to store the
    number of boxes in our sudoku. The elements will be received
    by user. The First room is for the number of boxes in a row
    and the second one is for the number of boxes in a column


3. Possible_Numbers ──────> This list stores all allowed numbers.
    for example if each box has 4 cells, the possible numbers are
    1, 2, 3, and 4. If there is 5 cells, they are 1, 2, 3, 4, and 5.


4. Sudoku ──────> "Sudoku" receive the data of each cell as a list.
    it can be a number or if it is a empty cell user should write
    0. Then it is converted to an array and then a 3D array
    that represents the Sudoku. This 3D array contains 3
    major parts. In order:
        a. Height of Sudoku: number of boxes in a column.
        b. Length of Sudoku: number of boxes in a row.
        c. Total Cells of a Box of the Sudoku: total number of cells in a box.


5. Total_rows  ──────> It stors the number of cell in a column of the sudoku


6. i ──────> This variable is used for iteration and it is public


7. i_box_length ──────> It is used for iteration to reach to the number of boxes
    in a row.


8. i_box_height ──────> It is used for iteration to reach to the number of boxes
    in a column.


9. i_cell_length ──────> It is used for iteration to reach to the number of cells
    in a row of each box.


10. i_cell_height ──────> It is used for iteration to reach to the number of cells
    in a column of each box.

11. cell_pos ──────> Its full name is cell_position. This is used to store the position
    of the empty cell. Its type is 'List' and has three elements.
    In order they are:
    a. Sequence number of box in y-axis
    b. Sequence number of box in x-axis
    c. Sequence number of the cell

12. In_box_row ──────> This variable is used to store number order of first cell in the
    row which our empty cell is. First it divides the number order of empt cell by number
    of cell are in a row of each box. After dividing, it removes the numbers after radix point.
    Once it is done we can undrestand the row that our empty cell is. Consider number of row 
    in box not whole sudoku. To find the first cell in each box in that row, we multiply it by
    the number of cells in a row  of each box.

13. number ──────> It stores the number that software wants to place


14. Possible_Cells ──────> It stores all possible cells that we can place our number. If it is
    not possible it would be 0, otherwise the number its selfe.


15. Addition_TotalCells ──────> It stores the total sum of sequence number of cells that we can place
    our number.


16. Sudoku_copy  ──────> This array stores sudoku to begin with, and changes are applied to this 
    array.


17. Qty ──────> This variable count number of possible cells in the box. We use it to find if the
    number of possible cells is equal to the possiblity we are reviewing.


18. box_cells_avaibility ──────> This variable is increased if the quantity of possible cells is not 
    equal to possibility.


19. sudoku_boxes_avaibility ──────> This variable is increased if 'box_cells_avaibility' is equal to number
    of possible numbers in the box. It means non of numbers can be placed in box with the possibility we
    are reviewing.


20. Backtrack ──────> It stores the position of numbers in boxes if their possible cells are more than 1.


21. i_order ──────> It is used to store the number is sudoku base on the numbers of iteration.


22. filled_boxes ──────> If this variable is equal to number of total boxes, it means, sudoku is solved.


23. Allowed_Numbers ──────> This list stores numbers that can be placed in the desired box.


24. i_cell ──────> This is to count cells.


25. existed_Numbers ──────> This list stores the possible numbers. It is used to find is any repeated number
    in the column or row.


26. possibility ──────> This variable stores number of possible cells for a number
"""

#════════════════════════ Functions ═══════════════════════════════════════

"""
1. Receiver: This function receive the three important input.
    It has 3 parts. In order they are:

    a. Receiving Sudoku Grid ──────> In the beginning, it receives the number 
        of cells in each row and each column separately. Then it asks for the 
        number of boxes in each row and each column. It also checks the input 
        not to be wrong.

    b. Finding All possible Numbers ──────> In Sudoku, we have limits in 
        using numbers. The range of numbers starts from 1, but the number of 
        box cells defines the last number. For example, if each box has four 
        cells, the range would be 1, 2, 3, and 4. if we have five cells, it 
        would be 1, 2, 3, 4, and 5. So if we know the number of our cells, we 
        easily can find all possible numbers.

    c. Receive All cells values ──────> This part of the function is to get the 
        value of defined cells. The software stores them in a list in order. Then
        we convert the list to an array and then a 3D array. This 3D array follows 
        the shape of the Sudoku that is defined by the user. The first part of the 
        3D-array is for the number of rows. The second is for columns, and the last 
        one is for the number of cells in each box.

    Variables are Used in This Function:
        Sudoku_cells, Sudoku_box, Possible_Numbers, Sudoku, i




2. Displaying: This Function purpose is to display the sudoku
    in a proper and beautiful shape. It contains 3 sections.

    a. Print Numbers of the column grid ──────> This part displays
        numbers of the x-axis of our sudoku. 
    
    b. Print top border of the Sudoku ──────> I the second section
        program prints the top part of the sudoku border
    
    c. Print Numbers of each row of the grid and value of each cell 
    of the Sudoku ──────> To make our code easier and not using unnecessary libraries, 
        we print all data related to one row. This row can be the border or the values of 
        each cell. Our code writes the number of the row that is going to be written. 
        Then, it prints the edge. After printing the border, it starts to write the value 
        of each cell. Between each cell, sign "│" as the horizontal divider and "─" as the 
        vertical divider. Between each box, we use symbols that are utilized for the sudoku 
        border.

    Variables are Used in This Function:
        Sudoku_cells, Sudoku_box, Sudoku, i, i_box_length, i_box_height
        i_cell_length, i_cell_height



3. Is_allowed: This function checks all cells in the row and column of the empty cell that 
    the software wants to fill. If the number that the software wants to put in the empty 
    cell is repeated, it returns false otherwise, it would be True. It has two parts. 
    In order they are::

    a.  Checking The Column ──────> This section analyses all cells that are in the same 
        row with the empty cell. All cells in a box are not separated. Their sequence number 
        starts from 0 to the number of cells in a box. The software uses the module to find 
        cells under each other. The sequence number of cells is divided by the number of cells 
        in each box row, and have the same remainder are in the same column.

    b. Checking The Row ──────> In the beginning, the software finds the sequence number of the 
        first cell in each box row. We know the sequence number of all cells in a row follows the 
        same algorithm. The software divides the sequence number of empty cell by the number of cells 
        in a row of each box. Then, it will remove the radix point. The result shows the order of 
        the row. It just needs to multiply the result by the number of cells in a row in each box. 
        Then, it finds the sequence number of the first cell of the row in each box. For example, consider 
        the sequence number of the empty cell is 4, and the number of cells in a box is 9 ([9, 2, 3, 5, 0, 6, 7, 8, 1]). 
        
                    0 1 2
                   ╔═════╗
                 0 ║9│2│3║
                   ║─────║
                 1 ║5│ │6║
                   ║─────║
                 2 ║7│8│1║ 
                   ╚═════╝

        From the figure, it is clear that the number of its row is 1. Our array also shows that its order 
        is 4(starting from 0), so the sequence number of the first cell is 3, which is 5. We will have the 
        same result using our formula. 4 divided by three is 1.333.  After removing numbers after radix 
        point, it would be 1, which the number of our row. If we multiply one by three, which is equal 
        to three we will have the sequence number of the first cell in each box and the intended row.

        It is only required to monitor each cell. When all cells of the box in the intended row are 
        analyzed, the software jumps to the next box. It continues until all cells of all boxes in the 
        row are analyzed. If there is no same number it is fine otherwise, it returns False.

    
    If there is no problem, the function returns True. It means that the number is allowed to be there.

    Variables are Used in This Function:
        sudoku, Sudoku_cells, Sudoku_box, cell_pos, number
        i, i_box_length, i_box_height, In_box_row



4. Backtrack_Check: The software stores the position of filled cells. The program resets the Sudoku when 
    the solution is wrong. The action of caching filled cells help software to avoid repeating the same 
    mistakes in solving the Sudoku. This function helps software not to save the same cells with a 
    similar position and the number inside.

    Variables are Used in This Function: 
        number, Backtrack, Box_Position, i



5. Solve_Sudoku: This function carries the main job of the software. It appropriates other 'functions' to 
    analyze and solve the Sudoku. The entire operation is within an interminable loop, and the software 
    breaks this loop when our Sudoku is solved. The function contains two major parts. All of the below 
    actions happen for each box of the Sudoku:
    
    a. Checking The Box ──────> The function seeks for possible numbers that are missing from the box. It caches 
        missed numbers in 'Allowed_Numbers.' Variable 'filled_boxes' will be raised by one if 'Allowed_Numbers' 
        is blank. It means all cells of the box are full. The Sudoku is solved when 'fiiled_boxes' is equal to 
        the total number of boxes.

    b. Checking Cells and Fill Them

        ● The First Step ══> The function checks each number of 'Allowed_Numbers' in all cells of the box. It cashes 
            each cell if the number is allowed to be. For example, the software can assign the number 3 to the first and 
            fifth cell. The function cashes possibilities in a variable called 'Possible_Cells.' If we implement the example 
            in a 3*3 box, 'Possible_Cells' will be equivalent to [3,0,0,0,3,0,0,0,0].  

        ● The Second Step ══> The software proposes to apply logic as much as possible. It explores for numbers in the box 
            that only have one opportunity. The software analysis counts the number of elements of 'Possible_cells' that are 
            greater than zero. The software keeps limits if in find any number that obeys the rules. If there is no number, 
            it changes the rules. It continues as long as the permissible opportunities are less than or equal to the total 
            number of box cells. For example, the software begins with one-optional numbers. The software search for 
            two-optional numbers if all numbers have two or more possibilities. The software converts rules to the one-optional 
            when it assigns a number to the Sudoku.
		    The software stores each action. It helps to avoid replicating solutions or slips (mentioned in 'Backtrack_check'). 
            The software removes the latest cashed data when it already checked all possible options of the number.
        
        ● The Third Step ══> The answer or the Sudoku would be incorrect. The software can figure out the solution is wrong when 
            a number is dropping in the box, but laws won't allow the software to put the desired number. If 'Backtrack' is blank, 
            it indicates the Sudoku is wrong.

    All proceeds are employed to solve the Sudoku. The software returns the Sudoku when it is solved.

    Variables are Used in This Function:
        Sudoku, Sudoku_cells, Sudoku_box, Possible_Numbers, possibility
        Sudoku_copy, Possible_Cells, Qty, box_cells_avaibility
        sudoku_boxes_avaibility, Backtrack, i_order, sudoku_boxes_avaibility
        filled_boxes, Allowed_Numbers, i_box_length, i_box_height, i_cell, i



6. wrong_correct: Desired function act as a filter to analyze the Sudoku if it is correct. It contains three major parts.
    
    a. Checking Cells of Boxes ──────> This section of the code investigates each box if there is any repeated or forbidden 
        number. The software selects the first cell and compares it with the next cells. It goes to the next one and contrasts 
        the remaining cells after the desired one. The Sudoku is wrong if the intended cell is equal to the left cells after.
    
    b. Checking Rows of Sudoku ──────> The piece of code uses a different technic to find if there are repeated numbers in a row. 
        The software uses allowed numbers of the Sudoku. It analyzes each cell of the row and removes the number when it faces a filled 
        cell. The Sudoku is wrong if the number of the cell does not exist.
    
    c. Checking Column of Sudoku ──────> The piece of code uses a different technic to find if there are repeated numbers in a column. 
        The software uses allowed numbers of the Sudoku. It analyzes each cell of the column and removes the number when it faces a filled 
        cell. The Sudoku is wrong if the number of the cell does not exist.
    
    Variables are Used in This Function:
        Sudoku, Sudoku_cells, Sudoku_box, Possible_Numbers
        i_box_height, i_box_length, i_cell i_cell_height 
        i_cell_length, existed_Numbers

"""





#┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬
#||||||||||||||||||||||||| Librareis |||||||||||||||||||||||||||||||||||
#┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴

import numpy as np
import time
from datetime import datetime


#┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬
#|||||||||||||||||||||||| Functions |||||||||||||||||||||||||||||||||||||
#┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴


#═════════════════ ══════════════════════════ ══════════════════════════

#═════════════════ Receiver of Grids and Digits ════════════════════════

#═════════════════ ══════════════════════════ ══════════════════════════
def Receiver():

    #\_______Sudoku Grid Size___________/
    # Get The size of Sudoku from User

    #-----> Cells <------

    Sudoku_cells = [] # The number of cells in each box

    # The number of cells in the length of each box
    Sudoku_cells.append(int(input("Please Enter the length of each box: ")))

    while Sudoku_cells[0] <= 0:
        # If input is less than equal to 0 raise an Error
        print("Input can not be less equal to 0")
        Sudoku_cells[0] = int(input("Please Enter the length of each box: "))

    # The number of cells in the height of each box
    Sudoku_cells.append(int(input("Please Enter the height of each box: ")))

    while Sudoku_cells[1] <= 0:
        # If input is less than equal to 0 raise an Error
        print("Input can not be less equal to 0")
        Sudoku_cells[1] = int(input("Please Enter the height of each box: "))



    #------> Boxes <-------

    Sudoku_box = [] # The number of boxes in Sudoku

    # The number of Boxes in the length of Sudoku
    Sudoku_box.append(int(input("Please Enter the length of Sudoku: ")))

    while Sudoku_box[0] <= 0:
        # If input is less than equal to 0 raise an Error
        print("Input can not be less equal to 0")
        Sudoku_cells[0] = int(input("Please Enter the length of Sudoku: "))

    # The number of Boxes in the hight of Sudokux
    Sudoku_box.append(int(input("Please Enter the height of Sudokux: ")))

    while Sudoku_box[1] <= 0:
        # If input is less than equal to 0 raise an Error
        print("Input can not be less equal to 0")
        Sudoku_cells[1] = int(input("Please Enter the height of Sudoku: "))

    #\_______ Finding All possible Numbers___________/
    # All Possible Number That are in Sudoku

    Possible_Numbers = [] # Store All Possible Numbers

    for i in range(Sudoku_cells[0]*Sudoku_cells[1]):
        # Find and Add All Possible Numbers
        Possible_Numbers.append(i+1)
    
    #\_______Receive All cells values___________/

    Sudoku = [] # Store Data of Sudoku
    #Total number of cells is equal to multiplication of number of boxes by number of cells of each box
    for i in range(Sudoku_box[0]*Sudoku_box[1]*Sudoku_cells[0]*Sudoku_cells[1]):

        Sudoku.append(int(input("Please Enter value of Cell(" + str(i) + "): ")))

        # Check if input is correct
        while True:
            try:
                Sudoku[i] = int(Sudoku[i])

            except:

                print("Input is not valid")
                Sudoku[i] = int(input("Please Try again: "))

            else:
                break
        

        # Check if input does not cross the limits
        while True:
            if Sudoku[i]>Possible_Numbers[-1]:
                print("Input is greater than the limit")
                Sudoku[i] = int(input("Please Try again: "))

            elif Sudoku[i]<0:
                print("Input is less than the limit")
                Sudoku[i] = int(input("Please Try again: "))

            else:
                break

    Sudoku = np.array(Sudoku) # Convert the "Sudoku" to an ARRAY
    Sudoku = Sudoku.reshape((Sudoku_box[1], Sudoku_box[0], Sudoku_cells[0]*Sudoku_cells[1])) # Convert 1D "Sudoku" to 3D "Sudoku"

    return Sudoku_cells, Sudoku_box, Possible_Numbers, Sudoku # the output of the function








#═════════════════ ══════════════════════════ ══════════════════════════

#═════════════════ Display the Sudoku ══════════════════════════════════

#═════════════════ ══════════════════════════ ══════════════════════════

def Displaying(Sudoku_cells, Sudoku_box, Possible_Numbers, Sudoku):

    Total_rows = 0 # Number of cells of each row

    #\_______Print Numbers of the column grid___________/

    print("   ", end="") # Space to beautify

    # Writing the number of each column
    for i in range(Sudoku_cells[0]*Sudoku_box[0]):
        print(i, end="")
        print(" ", end="")
    
    print("")# Go to the next line

    print("  ", end="") # Space 



    #\_______Print top border of the Sudoku___________/

    print("╔", end="")

    for i_box_length in range(Sudoku_box[0]):
        # Continues until "i_box_length" is equal to number of each box of  Sudoku

        for i_cell_length in range(Sudoku_cells[0]):
            # Continues until "i_cell_length" is equal to number of cell of each box of Sudoku

            print("═", end="")# print border line

            if i_cell_length == Sudoku_cells[0]-1 and i_box_length == Sudoku_box[0]-1:
                print("╗")# print border line if it is the end of border
                            
            elif i_cell_length == Sudoku_cells[0]-1:
                # if it is the end of box
                print("╦", end="")# print border line 
                            
            else:
                #Note: between each number of grid, there is a space so one line is not enough
                print("═", end="")# print border line



    #\_______Print Numbers of each row of the grid and value of each cell of the Sudoku___________/

    for i_box_height in range(Sudoku_box[1]):
        # Continues until "i_box_height" is equal to the number of boxes in a row

        for i_cell_height in range(Sudoku_cells[1]):
            # Continues until "i_box_height" is equal to the number of boxes in a row

            print(str(Total_rows) + " " + "║", end="") # display number of row and border

            # Index of the cell that displaying is supposed to start
            cell_index = 0 + (i_cell_height * Sudoku_cells[0]) 

            for i_box_length in range(Sudoku_box[0]):
                # Continues until "i_box_length" is equal to the number of boxes in a row

                for i_cell_length in range(Sudoku_cells[0]):
                    # Continues until "i_cell_length" is equal to the number of cell in a row of each box
                    
                    print(Sudoku[i_box_height, i_box_length, cell_index + i_cell_length], end="") # print the number inside of that cell

                    if(i_cell_length == Sudoku_cells[0]-1):
                        # If it is the end box print sign below
                        print("║", end="")
                    
                    else:
                        # otherwise print sign below
                        print("│", end="")

            print("")# go to the next line
            print("  ", end="") #space

            if i_cell_height == Sudoku_cells[1]-1 and i_box_height == Sudoku_box[1]-1:
                # If all cells and boxes are done and only the bottom borde is remaining.

                print("╚", end="") # for left edge

                for i_box_length in range(Sudoku_box[0]):
                    # Continues until "i_box_length" is equal to the number of boxes in a row

                    for i_cell_length in range(Sudoku_cells[0]):
                        # Continues until "i_cell_length" is equal to the number of cells in a row of each box
                        print("═", end="")

                        if i_cell_length == Sudoku_cells[0]-1 and i_box_length == Sudoku_box[0]-1:
                            # If we reached to the right border
                            print("╝") # for right edge
                            
                        elif i_cell_length == Sudoku_cells[0]-1:
                            # If the box is finished
                            print("╩", end="")
                            
                        else:
                            #Note: between each number of grid, there is a space so one line is not enough
                            print("═", end="")        
            
            elif i_cell_height == Sudoku_cells[1]-1:
                # If a box is finished and we want go to the next row
                print("╠", end="") # left border

                for i_box_length in range(Sudoku_box[0]):
                    # Continues until "i_box_length" is equal to the number of boxes in a row

                    for i_cell_length in range(Sudoku_cells[0]):
                        # Continues until "i_cell_length" is equal to the number of cells in a row of each box
                        print("═", end="")

                        if i_cell_length == Sudoku_cells[0]-1 and i_box_length == Sudoku_box[0]-1:
                            # If we reached to the right border
                            print("╣") # for right edge
                            
                        elif i_cell_length == Sudoku_cells[0]-1:
                             # If the box is finished
                            print("╬", end="")
                            
                        else:
                            #Note: between each number of grid, there is a space so one line is not enough
                            print("═", end="")
                
            
            else:
                # If the cell row is finished and we want to go to the next row but box is same
                print("║", end="")# right border
    
                for i_box_length in range(Sudoku_box[0]):
                    # Continues until "i_box_length" is equal to the number of boxes in a row

                    for i_cell_length in range(Sudoku_cells[0]):
                        # Continues until "i_cell_length" is equal to the number of cells in a row of each box
                        print("─", end="")

                        if i_cell_length == Sudoku_cells[0]-1 and i_box_length == Sudoku_box[0]-1:
                            # If we reached to the right border
                            print("║")# left border

                        elif i_cell_length == Sudoku_cells[0]-1:
                            # If the box is finished
                            print("║", end="")
                            
                        else:
                            #Note: between each number of grid, there is a space so one line is not enough
                            print("─", end="")
            
            Total_rows += 1 # add 1 to "Total_row"

            




#═════════════════ ══════════════════════════ ══════════════════════════

#══════════════════ Sovling The Sudoku (Check Row and Column) ══════════

#═════════════════ ══════════════════════════ ══════════════════════════




def Is_allowed(Sudoku, Sudoku_cells, Sudoku_box, cell_pos, number):
    
    #\_______Checking The Column___________/

    for i_box_height in range(Sudoku_box[1]):
        # Continue until all Rows of Sudoku Boxes are checked 

        for i in range(Sudoku_cells[1] * Sudoku_cells[0]):
            # Continue until all of Box Cells are checked 

            if i % Sudoku_cells[0] == cell_pos[2] % Sudoku_cells[0]:
                # This helps to only check cells under each other

                if Sudoku[i_box_height, cell_pos[1], i] == number:
                    #This condition returns False if our number exist in this column

                    return False        
    
    
    
    #\_______Checking The Row___________/

    In_box_row = Sudoku_cells[0] * int(cell_pos[2]/Sudoku_cells[0]) # Stores the order number of first cell in that row

    for i_box_length in range(Sudoku_box[0]):
        # Continue until all column of Sudoku Boxes are checked 

        for i_cell_length in range(Sudoku_cells[0]):
            # Continue until all cells of Box in a Rows are checked
            
            if Sudoku[cell_pos[0], i_box_length, In_box_row + i_cell_length] == number:
                #This condition returns False if our number exist in this row
                return False
    

    return True # Return True if it is allowed to place our number in its row and column







#═════════════════ ══════════════════════════ ══════════════════════════

#═════════════ Sovling The Sudoku (Check if number data exsit) ═════════════

#═════════════════ ══════════════════════════ ══════════════════════════




def Backtrack_Check(number, Backtrack, Box_Position):
    i=0
    for i in range(len(Backtrack)):
        if Backtrack[i][0] == Box_Position[0] and Backtrack[i][1] == Box_Position[1] and Backtrack[i][2] == number:
            return False, i
    
    return True, i
            





#═════════════════ ══════════════════════════ ══════════════════════════

#═════════════ Sovling The Sudoku (Find numbers and place them) ═════════════

#═════════════════ ══════════════════════════ ══════════════════════════




def Solve_Sudoku(Sudoku, Sudoku_cells, Sudoku_box, Possible_Numbers):

    possibility = 1 # This variable stores number of possible cells for a number

    Sudoku_copy = Sudoku.copy() # 'Sudoko_copy' stores new filled cells and 'sudoku'

    Possible_Cells = [] # This one sotres cell that are possible to be filled in each box or aren't

    Qty = 0 # This variable stores number off possible cells in each box

    box_cells_avaibility = 0 # This varaible increase if the numbers in the box does not have conditions 

    sudoku_boxes_avaibility = 0 # This variable increase if non of numbers in the box have conditions

    Backtrack = [] # This variable stores numbers with more than one possible cell

    i_order = 0 # It is used to store the number is sudoku base on the numbers of iteration

    # This loop ends when Sudoku is solved
    while True:

        sudoku_boxes_avaibility = 0 # Every repeat make it equal to zero
        filled_boxes = 0 # Every repeat make it equal to zero


        for i_box_length in range(Sudoku_box[0]):
            # Continues until all Bytes in a row are checked

            for i_box_height in range(Sudoku_box[1]):
                # Continues until all Bytes in a row are checked

                box_cells_avaibility = 0 # Every repeat make it equal to zero


                #\_______Checking The Box___________/

                Allowed_Numbers = Possible_Numbers.copy() # Make a new varaible and save possible numbers in it

                # The loop below endes when it checked all cells in the box
                for i_cell in range(Sudoku_cells[0]*Sudoku_cells[1]):
                    
                    # The condition remove the number in the cell if it find it in the box
                    if Sudoku_copy[i_box_height, i_box_length, i_cell] > 0:
                        
                        Allowed_Numbers.remove(Sudoku_copy[i_box_height, i_box_length, i_cell]) # Remove the number in filled cell


                if Allowed_Numbers == []:
                    # This conditon check if box is filled
                    filled_boxes += 1
                


                #\_______Checking cells and Fill them___________/

                for number in Allowed_Numbers:

                    Possible_Cells.clear() # Empties the list

                    Qty = 0 # Make varialbe equal to zero




                    # Finding allowed cells
                    for i in range(Sudoku_cells[0]*Sudoku_cells[1]):

                        # If the cell is empty, analyse it.
                        if Sudoku_copy[i_box_height, i_box_length, i] == 0:

                            # If output of 'Is_allowed' is true (It means number is allowed to be there)
                            if Is_allowed(Sudoku_copy, Sudoku_cells, Sudoku_box, [i_box_height, i_box_length, i], number):

                                Possible_Cells.append(number) # If it is possible to place the number add it to the list
                                
                            else:

                                Possible_Cells.append(0) # If not, add 0
                        
                        else:

                            Possible_Cells.append(0) # If cell is filled add 0

                    

                    # The loop bellow count how many possible cells there are for this number in the box
                    for i in Possible_Cells:

                        if i > 0:

                            Qty += 1
                    
                    
                    
                    # If the number of possible cells is equal to the possiblity we are studing, enter
                    if Qty == possibility:
                        
                        # Check if it is stored for backtrack, If it is not output of 'Backtrack_Check' is true
                        if Backtrack_Check(number, Backtrack, [i_box_height, i_box_length])[0]:
                            
                            Backtrack.append([i_box_height, i_box_length, number, possibility, 1]) # Add information of number
                            
                            possibility = 1 

                            
                        i_order = 0

                        # This loop place the numbers in the allowed place
                        for i in range(len(Possible_Cells)):
                            
                            
                            # Once program face with a number it enters the condition
                            if Possible_Cells[i] > 0:

                                i_order += 1 # Add i_order by 1

                                # This program may face with the numbers in a box that may have more than one-
                                # possible cell. if they are 
                                if Possible_Cells[i] > 0 and i_order == Backtrack[Backtrack_Check(number, Backtrack, [i_box_height, i_box_length])[1]][4]:
                                    

                                    Sudoku_copy[i_box_height, i_box_length, i] = Possible_Cells[i]
                                    possibility = 1
                                    break    

                    else:
    
                        box_cells_avaibility += 1
                    
                    # if sudoku is wrong    
                    if Qty == 0:
                        # If the sudoku is wron
                        if Backtrack == []:
                            raise Exception ("The Sudoku is wrong")
                        
                        # If the solution is wrong
                        else:
                            Backtrack[-1][4] += 1
                            Sudoku_copy = Sudoku.copy()
                            box_cells_avaibility = 0
                            sudoku_boxes_avaibility = 0

                    # Remove Backtrack
                    if Backtrack != []:
                        for i in range(len(Backtrack)):
                            
                            # If all possible conditions are of the specific backtrack are checked
                            if Backtrack[-1][4] > Backtrack[-1][3]:
                                Backtrack.pop(-1)
                                
                                if Backtrack != []:
                                    # If anything left in 'Backtrack'
                                    Backtrack[-1][4] += 1
                                
                                possibility = 1
                            
                            elif Backtrack[-1][3] == 1:
                                # If all possible conditions are of the specific backtrack are not checked
                                Backtrack.pop(-1)
                                possibility = 1

                        if Backtrack == []:
                            # If there is nothing in 'Bacrack'
                            Sudoku = Sudoku_copy.copy()

    
                if box_cells_avaibility == len(Allowed_Numbers):

                    sudoku_boxes_avaibility += 1
                    

        if sudoku_boxes_avaibility == Sudoku_box[0]*Sudoku_box[1]:
            # This means all there is no number in sudoku that has possiblity equal to 'possibility' so software increase it
            possibility += 1
        
        if filled_boxes == Sudoku_box[0]*Sudoku_box[1]:
            # If Sudoku is solved
            Sudoku = Sudoku_copy.copy()
            break
    
    return Sudoku





#═════════════════ ══════════════════════════ ══════════════════════════

#═════════════ Sovling The Sudoku (Find out if sudoku is correct) ═════════════

#═════════════════ ══════════════════════════ ══════════════════════════




def wrong_correct(Sudoku, Sudoku_cells, Sudoku_box, Possible_Numbers):

    #\_______Checking Cells of Boxes___________/
    
    for i_box_height in range(Sudoku_box[1]):
        # Continues until all boxes of the column are checked

        for i_box_length in range(Sudoku_box[0]):
            # Continues until all boxes of the row are checked

            for i_cell in range(Sudoku_cells[0]*Sudoku_cells[1]):
                # Continues until all cells of the box are checked

                # This code here will be run if desired cell is bigger than 0 and less than the biggest possible number for this sudoku
                if Sudoku[i_box_height, i_box_length, i_cell] > 0 and Sudoku[i_box_height, i_box_length, i_cell] < Sudoku_cells[0]*Sudoku_cells[1]:
                    
                    for i in range(((Sudoku_cells[0]*Sudoku_cells[1])-i_cell)-1):
                        # Continues until all cell after desired one are checked

                        # Program enter this condition when our desired cell is equal to one of cells after itself
                        if Sudoku[i_box_height, i_box_length, i_cell] == Sudoku[i_box_height, i_box_length, i_cell + 1 + i]:
                            
                            # Print Error
                            raise Exception ("The Sudoku is wrong : Same numbers in one box")        
                
                # Here, program check the number of cell. If it is bigger than maximum and less than 0, program prints error
                elif Sudoku[i_box_height, i_box_length, i_cell] > Sudoku_cells[0]*Sudoku_cells[1] or Sudoku[i_box_height, i_box_length, i_cell] < 0:

                    # Print Error
                    raise Exception ("The Sudoku is wrong : Number Passes Limits")  

    #\_______Checking Rows of Sudoku___________/      
             
    for i_box_height in range(Sudoku_box[1]):
        # Continues until all boxes of the column are checked

        for i_cell_height in range(Sudoku_cells[1]):
            # Continues until all cells of the column are checked

            existed_Numbers = Possible_Numbers.copy() # Storing Possible numbers in 'existed_Numbers'

            for i_box_length in range(Sudoku_box[0]):
                # Continues until all boxes of the row are checked

                for i_cell_length in range(Sudoku_cells[0]):
                    # Continues until all cells of the row are checked

                    # Code blew remove existed number in the desired cell if it is not 0 and it exists in -
                    # the 'existed_Numbers'. If it is not equal to 0 and it does not in the 'existed_number'
                    # it prints Error out.
                    if Sudoku[i_box_height, i_box_length, (i_cell_height*Sudoku_cells[0])+i_cell_length] > 0:

                        try:

                            existed_Numbers.remove(Sudoku[i_box_height, i_box_length, (i_cell_height*Sudoku_cells[0])+i_cell_length])
                        except:

                            raise Exception ("The Sudoku is wrong : Same numbers in a row")
    

    #\_______Checking Column of Sudoku___________/ 

    for i_box_length in range(Sudoku_box[0]):
        # Continues until all boxes of the row are checked

        for i_cell_length in range(Sudoku_cells[0]):
            # Continues until all cells of the row are checked

            existed_Numbers = Possible_Numbers.copy() # Storing Possible numbers in 'existed_Numbers'

            for i_box_height in range(Sudoku_box[1]):
                # Continues until all boxes of the column are checked

                for i_cell_height in range(Sudoku_cells[1]):
                    # Continues until all cells of the column are checked

                    # Code blew remove existed number in the desired cell if it is not 0 and it exists in -
                    # the 'existed_Numbers'. If it is not equal to 0 and it does not in the 'existed_number'
                    # it prints Error out.
                    if Sudoku[i_box_height, i_box_length, (i_cell_height*Sudoku_cells[0])+i_cell_length] > 0:

                        try:

                            existed_Numbers.remove(Sudoku[i_box_height, i_box_length, (i_cell_height*Sudoku_cells[0])+i_cell_length])
                        except:

                            raise Exception ("The Sudoku is wrong : Same numbers in a column")




#┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬
#|||||||||||||||||||||||||| Main ||||||||||||||||||||||||||||||
#┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴

# Please Be Patient, It may takes more than 10 seconds for some Sudokus.


# Cells Start from left to right, top to down_____________________________________________________________________________________________________________________
Inputs = Receiver()
Cells = Inputs[0]
Boxes = Inputs[1]
Possible_Numbers_Sudoku = Inputs[2]
Sudoku_0 = Inputs[3]

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Sudoku_0) # Displaying not solved sudoku

wrong_correct(Sudoku_0, Cells, Boxes, Possible_Numbers_Sudoku) # Check if it is wrong

startTime = datetime.now() # Counting Time

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Solve_Sudoku(Sudoku_0, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku

print(datetime.now() - startTime) # ShowTime

startTime = datetime.now() # Count Time

print(Solve_Sudoku(Sudoku_0, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku(not ordered)

print(datetime.now() - startTime) # ShowTime



# 3*3_____________________________________________________________________________________________________________________
Cells = [3,3]
Boxes = [3,3]
Possible_Numbers_Sudoku = [1,2,3,4,5,6,7,8,9]
Sudoku_1 = np.array([[[0, 0, 0, 0, 0, 0, 5, 0, 0],[8, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 4, 3, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 2, 0],[0, 7, 0, 0, 0, 0, 0, 3, 0],[8, 0, 0, 1, 0, 0, 0, 0, 0]],
            [[6, 0, 0, 0, 0, 3, 0, 0, 0],[0, 0, 0, 4, 0, 0, 2, 0, 0],[0, 7, 5, 0, 0, 0, 6, 0, 0]]])
            
Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Sudoku_1) # Displaying not solved sudoku

wrong_correct(Sudoku_1, Cells, Boxes, Possible_Numbers_Sudoku) # Check if it is wrong

startTime = datetime.now() # Counting Time

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Solve_Sudoku(Sudoku_1, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku

print(datetime.now() - startTime) # ShowTime

startTime = datetime.now() # Count Time

print(Solve_Sudoku(Sudoku_1, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku(not ordered)

print(datetime.now() - startTime) # ShowTime


# 3*3_____________________________________________________________________________________________________________________
Cells = [3,3]
Boxes = [3,3]
Possible_Numbers_Sudoku = [1,2,3,4,5,6,7,8,9]
Sudoku_2 = np.array([[[0, 8, 1, 0, 0, 0, 0, 4, 6],[0, 0, 0, 0, 7, 0, 3, 0, 1],[0, 0, 0, 0, 0, 6, 0, 0, 5]],
            [[0, 0, 0, 9, 0, 5, 0, 1, 0],[6, 0, 0, 0, 0, 0, 4, 0, 0],[7, 0, 0, 4, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 6, 8, 0, 0, 2],[0, 0, 7, 0, 0, 3, 8, 0, 0],[6, 0, 1, 2, 0, 0, 0, 0, 0]]])

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Sudoku_2) # Displaying not solved sudoku

wrong_correct(Sudoku_2, Cells, Boxes, Possible_Numbers_Sudoku) # Check if it is wrong

startTime = datetime.now() # Counting Time

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Solve_Sudoku(Sudoku_2, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku

print(datetime.now() - startTime) # ShowTime

startTime = datetime.now() # Count Time

print(Solve_Sudoku(Sudoku_2, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku(not ordered)

print(datetime.now() - startTime) # ShowTime


# 3*3_____________________________________________________________________________________________________________________
Cells = [3,3]
Boxes = [3,3]
Possible_Numbers_Sudoku = [1,2,3,4,5,6,7,8,9]
Sudoku_3 = np.array([[[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]])

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Sudoku_3) # Displaying not solved sudoku

wrong_correct(Sudoku_3, Cells, Boxes, Possible_Numbers_Sudoku) # Check if it is wrong

startTime = datetime.now() # Counting Time

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Solve_Sudoku(Sudoku_3, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku

print(datetime.now() - startTime) # ShowTime

startTime = datetime.now() # Count Time

print(Solve_Sudoku(Sudoku_3, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku(not ordered)

print(datetime.now() - startTime) # ShowTime


# 2*5_____________________________________________________________________________________________________________________
Cells = [5,2]
Boxes = [2,5]
Possible_Numbers_Sudoku = [1,2,3,4,5,6,7,8,9,10]
Sudoku_4 = np.array([[[5, 0, 1, 0, 10, 0, 0, 4, 0, 0],[0, 0, 4, 8, 9, 10, 0, 5, 6, 0]],
            [[6, 9, 7, 0, 0, 0, 8, 0, 2, 0],[0, 0, 0, 1, 0, 0, 0, 0, 5, 0]],
            [[2, 1, 0, 6, 0, 4, 0, 10, 0, 9],[0, 0, 9, 4, 0, 0, 6, 0, 0, 0]],
            [[0, 10, 0, 0, 1, 0, 3, 0, 0, 0],[3, 0, 0, 0, 2, 0, 0, 6, 0, 5]],
            [[0, 0, 8, 0, 6, 0, 0, 0, 0, 0],[0, 9, 0, 0, 0, 0, 0, 10, 0, 0]]])

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Sudoku_4) # Displaying not solved sudoku
print(Sudoku_4[0,1,8])
wrong_correct(Sudoku_4, Cells, Boxes, Possible_Numbers_Sudoku) # Check if it is wrong

startTime = datetime.now() # Counting Time

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Solve_Sudoku(Sudoku_4, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku

print(datetime.now() - startTime) # ShowTime

startTime = datetime.now() # Count Time

print(Solve_Sudoku(Sudoku_4, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku(not ordered)

print(datetime.now() - startTime) # ShowTime

# 3*3 wrong_____________________________________________________________________________________________________________________
Cells = [3,3]
Boxes = [3,3]
Possible_Numbers_Sudoku = [1,2,3,4,5,6,7,8,9]
Sudoku_5 = np.array([[[8, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 7, 0, 0, 0, 0],[8, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 8]],
            [[0, 0, 8, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]])

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Sudoku_5) # Displaying not solved sudoku

wrong_correct(Sudoku_5, Cells, Boxes, Possible_Numbers_Sudoku) # Check if it is wrong

startTime = datetime.now() # Counting Time

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Solve_Sudoku(Sudoku_5, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku

print(datetime.now() - startTime) # ShowTime

startTime = datetime.now() # Count Time

print(Solve_Sudoku(Sudoku_5, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku(not ordered)

print(datetime.now() - startTime) # ShowTime

# 3*3 wrong_____________________________________________________________________________________________________________________
Cells = [3,3]
Boxes = [3,3]
Possible_Numbers_Sudoku = [1,2,3,4,5,6,7,8,9]
Sudoku_6 = np.array([[[8, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[8, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]])

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Sudoku_6) # Displaying not solved sudoku

wrong_correct(Sudoku_6, Cells, Boxes, Possible_Numbers_Sudoku) # Check if it is wrong

startTime = datetime.now() # Counting Time

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Solve_Sudoku(Sudoku_6, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku

print(datetime.now() - startTime) # ShowTime

startTime = datetime.now() # Count Time

print(Solve_Sudoku(Sudoku_6, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku(not ordered)

print(datetime.now() - startTime) # ShowTime

# 3*3 wrong_____________________________________________________________________________________________________________________
Cells = [3,3]
Boxes = [3,3]
Possible_Numbers_Sudoku = [1,2,3,4,5,6,7,8,9]
Sudoku_6 = np.array([[[8, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[8, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]])

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Sudoku_6) # Displaying not solved sudoku

wrong_correct(Sudoku_6, Cells, Boxes, Possible_Numbers_Sudoku) # Check if it is wrong

startTime = datetime.now() # Counting Time

Displaying(Cells, Boxes, Possible_Numbers_Sudoku, Solve_Sudoku(Sudoku_6, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku

print(datetime.now() - startTime) # ShowTime

startTime = datetime.now() # Count Time

print(Solve_Sudoku(Sudoku_6, Cells, Boxes, Possible_Numbers_Sudoku)) # Displaying solved sudoku(not ordered)

print(datetime.now() - startTime) # ShowTime