# source code can be found at: https://github.com/ArvinArbabi/Assignments/tree/master/lab6
def main():
    # pigeonhole loop
    while True:
        file_name = input("Enter the name of an input file: ")
        # opens file and checks if it is valid
        try:
            with open(file_name,'r',encoding='utf_8') as f:
                lines = f.readlines()
                first_line = lines[0].strip()

                # checks the validity of the input file
                # first line has to be numeric
                if not first_line.isnumeric():
                    print("Error: file contents invalid.")
                    f.close()
                    continue
                
                num_lines = int(first_line)

                # checks the validity of the input file
                # number of lines must match the first line
                if not num_lines == len(lines) - 1:
                    print("Error: End of file expected.")
                    f.close()
                    continue

                sum = 0
                # calculates the sum of the values in the file
                for l in lines[1:]:
                    l_strip = l.strip()
                    
                    # checks the validity of the input file
                    # all of the lines should be numeric
                    if not l_strip.isnumeric():
                        print("Error: file contents invalid.")
                        f.close()
                        sum = 0
                        break
                    
                    sum += float(l_strip)
                
                if not sum == 0:
                    print(sum)

        # catches any type of IO operation
        except IOError as e:
            print(e)
        # catches any type of index errors
        # e.g. empty file
        except IndexError as e:
            print("Error: File contents invalid.")
        # cleans up the resources
        finally:
            if not f == None:
                f.close()

# calling the main function
if __name__ == "__main__":
    main()

#-----------------------------------------------------------------------
# PS C:\work\assignments\lab6> python .\ArvinArbabiLab6.py
# Enter the name of an input file: bad1.dat
# Error: End of file expected.
# Enter the name of an input file: bad2.dat
# Error: file contents invalid.
# Enter the name of an input file: bad3.dat
# Error: End of file expected.
# Enter the name of an input file: bad4.dat
# Error: End of file expected.
# Enter the name of an input file: good.dat
# 55.0
# Enter the name of an input file: arvin
# [Errno 2] No such file or directory: 'arvin'
# Enter the name of an input file:
