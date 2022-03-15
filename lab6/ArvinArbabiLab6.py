def main():
    while True:
        file_name = input("Enter the name of an input file: ")
        try:
            with open(file_name,'r',encoding='utf_8') as f:
                lines = f.readlines()
                first_line = lines[0].strip()
                if not first_line.isnumeric():
                    print("Error: file contents invalid.")
                    f.close()
                    continue
                
                num_lines = int(first_line)

                if not num_lines == len(lines) - 1:
                    print("Error: End of file expected.")
                    f.close()
                    continue

                sum = 0
                for l in lines[1:]:
                    l_strip = l.strip()
                    if not l_strip.isnumeric():
                        print("Error: file contents invalid.")
                        f.close()
                        sum = 0
                        break
                    
                    sum += float(l_strip)
                
                if not sum == 0:
                    print(sum)

        except IOError as e:
            print(e)
        except IndexError as e:
            print("Error: File contents invalid.")
        finally:
            if not f == None:
                f.close()

            


if __name__ == "__main__":
    main()
