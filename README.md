# Solving Soduko With n×n Boxes and n×n Cells



## General Description

&nbsp; &nbsp; The software can find the answer of n×n boxes with n×n cells. The target of the software is assigning numbers with minimum possible options. All information related to the functions and variable can be found below

## Variables
_**Note**: Every variable that starts with 'i' is used for iteration._

**1. Sudoku_cells:**

&nbsp; &nbsp; It is a 2-dimensional list to store the number of cells in each box. The elements will be received by user. The first room is for the number of cells in a row and the second one is for the number of cells in a column


**2. Sudoku_box:** 

&nbsp; &nbsp; It is a 2-dimensional list to store the number of boxes in our sudoku. The elements will be received by user. The First room is for the number of boxes in a row and the second one is for the number of boxes in a column

**3. Possible_Numbers:** 

&nbsp; &nbsp; This list stores all allowed numbers. for example if each box has 4 cells, the possible numbers are 1, 2, 3, and 4. If there is 5 cells, they are 1, 2, 3, 4, and 5.


**4. Sudoku:**

&nbsp; &nbsp; "Sudoku" receive the data of each cell as a list. it can be a number or if it is a empty cell user should write 0. Then it is converted to an array and then a 3D array that represents the Sudoku. This 3D array contains 3 major parts. In order:
- Height of Sudoku: number of boxes in a column.
- Length of Sudoku: number of boxes in a row.
- Total Cells of a Box of the Sudoku: total number of cells in a box.


**5. Total_rows:**

&nbsp; &nbsp; It stors the number of cell in a column of the sudoku 


**6. i:**

&nbsp; &nbsp; This variable is used for iteration and it is public


**7. i_box_length** 

&nbsp; &nbsp; It is used for iteration to reach to the number of boxes in a row.


**8. i_box_height:**

&nbsp; &nbsp; It is used for iteration to reach to the number of boxes in a column.


**9. i_cell_length:** 

&nbsp; &nbsp; It is used for iteration to reach to the number of cells in a row of each box.


**10. i_cell_height:** 

&nbsp; &nbsp; It is used for iteration to reach to the number of cells in a column of each box.

**11. cell_pos :**

&nbsp; &nbsp; Its full name is cell_position. This is used to store the position of the empty cell. Its type is 'List' and has three elements. In order they are:
- Sequence number of box in y-axis
- Sequence numberr of box in x-axis
- Sequence number of the cell

**12. In_box_row:**

&nbsp; &nbsp; This variable is used to store Sequence number of first cell in the row which our empty cell is. First it divides the Sequence number of empt cell by number of cell are in a row of each box. After dividing, it removes the numbers after radix point. Once it is done we can undrestand the row that our empty cell is. Consider number of row in box not whole sudoku. To find the first cell in each box in that row, we multiply it by the number of cells in a row  of each box.

**13. number:**

&nbsp; &nbsp; It stores the number that software wants to place


**14. Possible_Cells:**

&nbsp; &nbsp; It stores all possible cells that we can place our number. If it is not possible it would be 0, otherwise the number its selfe.


**15. Addition_TotalCells:**

&nbsp; &nbsp; It stores the total sum of Sequence numbers of cells that we can place our number.


**16. Sudoku_copy:**

&nbsp; &nbsp; This array stores sudoku to begin with, and changes are applied to this array.


**17. Qty:**

&nbsp; &nbsp; This variable count number of possible cells in the box. We use it to find if the number of possible cells is equal to the possiblity we are reviewing.


**18. box_cells_avaibility:**

&nbsp; &nbsp;This variable is increased if the quantity of possible cells is not equal to possibility.


**19. sudoku_boxes_avaibility:**

&nbsp; &nbsp; This variable is increased if 'box_cells_avaibility' is equal to number of possible numbers in the box. It means non of numbers can be placed in box with the possibility we are reviewing.


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
    
    Checking Cells of Boxes ──────> This section of the code investigates each box if there is any repeated or forbidden 
        number. The software selects the first cell and compares it with the next cells. It goes to the next one and contrasts 
        the remaining cells after the desired one. The Sudoku is wrong if the intended cell is equal to the left cells after.
    
    Checking Rows of Sudoku ──────> The piece of code uses a different technic to find if there are repeated numbers in a row. 
        The software uses allowed numbers of the Sudoku. It analyzes each cell of the row and removes the number when it faces a filled 
        cell. The Sudoku is wrong if the number of the cell does not exist.
    
    Checking Column of Sudoku ──────> The piece of code uses a different technic to find if there are repeated numbers in a column. 
        The software uses allowed numbers of the Sudoku. It analyzes each cell of the column and removes the number when it faces a filled 
        cell. The Sudoku is wrong if the number of the cell does not exist.
    
    Variables are Used in This Function:
        Sudoku, Sudoku_cells, Sudoku_box, Possible_Numbers
        i_box_height, i_box_length, i_cell i_cell_height 
        i_cell_length, existed_Numbers

"""
