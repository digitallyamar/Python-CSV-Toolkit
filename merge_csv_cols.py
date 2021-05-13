###############################################################################
###############################################################################
# Use merge_cols() function to merge cols in a csv file
#
# This fn. takes in 3 parameters:
#
#           <csv_file_name> - Input csv file
#           <from_col> - Starting col no. (index starts from 0)
#           <num_of_cols> - No. of cols to be merged
#
# **Note**: This code only recognizes comma separated values in a csv file
#
# You can also call this program directly as explained below:
#
# Usage: python3 merge_csv_cols.py <csv_file_name> <from_col> <num_of_cols>
#
#           If <num_of_cols> = 1, only col[1] is selected
#           If <num_of_cols> = 2, only col[1] & col[2] is selected and merged
#           If <num_of_cols> = 0, all cols starting from col[1] will be merged
#
# You can also merge only selected cols in between in a row.
#
# Eg: If the row data looks like row = [1, 2, 3, 4, 5]
#     You can merge only selected cols to get output like 
#     new_row = [1, 2, "3,4", 5]
#
#     The command to achieve this would be:
#     python3 merge_csv_cols.py numbers.csv 2 2
#
###############################################################################
###############################################################################


import sys, csv

def merge_cols(csv_file_name, from_col, num_of_cols):
    from_col = int(from_col)
    num_of_cols = int(num_of_cols)
    fcsv = open(csv_file_name, 'r')
    fcsv_out = open('merged_' + csv_file_name, 'w')
    csv_reader = csv.reader(fcsv, delimiter=',', quotechar='"')
    csv_writer = csv.writer(fcsv_out, delimiter=',', quotechar='"')

    for row in csv_reader:
        # Process only if required no. of cols are present
        if (len(row) > from_col):
            new_row = []
            copy_col_upto = from_col
            tmp_row = row
            index = 0
            for c in tmp_row:
                index += 1
                if (index > from_col):
                    # Break loading row LHS side on reaching boundary
                    break
                else:
                    new_row.append(c)

            # Check if we need to merge all cols
            m_col  = ""
            if (num_of_cols == 0):
                for col in row[from_col:]:
                    # Add this col value to merged col string
                    # Also add a ',' at the end
                    m_col += col + ','
                    
            else:
                # Pretty much same as prev logic
                # Except we wil check if we have reached max col value
                # and break when done.
                count = 0
                for col in row[from_col:]:
                    m_col += col + ','
                    count += 1
                    if count == num_of_cols:
                        break

            # Remove last ',' char
            if (m_col[-1] == ','):
                m_col = '"' + m_col[:-1] + '"'
            
            new_row.append(m_col)

            # Append any remaining cols outside our merge window

            #Get total no. of cols filled so far
            # Work around when we are selecting all cols
            if (num_of_cols == 0):
                num_of_cols = len(row) - from_col


            # Check if there are more cols still remaining
            cols_filled_len = from_col + num_of_cols

            if (len(row) > cols_filled_len):
                next_col_index = cols_filled_len
                
                #Add remaining cols to new row list
                new_row.extend(row[next_col_index:])
            
            # Finally, copy modified row to original row
            row = new_row
        
        csv_writer.writerow(row)
    
    # Close file handles
    fcsv.close()
    fcsv_out.close()



if __name__ == "__main__":
    if (len(sys.argv) < 4):
        print ('Usage:\npython3 merge_csv_cols.py <csv_file_name> <from_col> <num_of_cols>\n')
        print ('[**Note:** If all cols are to be merged, set <num_of_cols> = 0]\n')
        print ('[**Note:** If <num_of_cols> = 1, only col[1] will be selected.]\n')
        print ('Eg: python3 merge_csv_cols.py test.csv 2 0\n')
        sys.exit(0)
    
    csv_file_name = sys.argv[1]
    from_col = sys.argv[2]
    num_of_cols = sys.argv[3]

    # Call the actual function to do our merge.
    merge_cols(csv_file_name, from_col, num_of_cols)