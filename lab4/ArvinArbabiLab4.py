import os

def main():
    while True:
        file_in_name = input("Input File: ")
        file_out_name = os.path.splitext(file_in_name)[0] + "_out" + os.path.splitext(file_in_name)[1]
        try:
            file_in = open(file_in_name, "r")
            file_out = open(file_out_name, "w+")
            fl = file_in.readlines()
            
            sum = 0.0

            for i in range(1,len(fl)):
                item_price = extract_item_price_tuple(fl[i])
                line_item = "${:.2f}".format(item_price[1])
                file_out.write("{:15s} {:<20}\n".format(item_price[0], line_item))
                sum += item_price[1]
            
            file_out.write("{:15s} ${:<20}\n".format("TOTAL PRICE:", sum))
            file_in.close()
            file_out.close()
            print(sum)
        
        except FileNotFoundError as e:
            print(e)
        except IndexError as e:
            print(e)
        except ValueError as e:
            print(e)


def extract_item_price_tuple(item_price):
    x = item_price.split(":")
    item = x[0].strip()
    price = float(x[1].strip())
    return (item, price)

if __name__ == ("__main__"):
    main() 