TOTAL_RUNS = 5
DISCOUNT_LAYER_1 = 8
DISCOUNT_LAYER_2 = 10
DISCOUNT_LAYER_3 = 12
DISCOUNT_LAYER_4 = 14

def main():
    counter = 0
    while counter < TOTAL_RUNS:
        counter += 1
        try:
            total_amount = float(input("how much were your groceries: "))
            if total_amount < 0:
                print("invalid input, please input a positive number")
                continue
    
            print("%.2f" % total_amount)
            if total_amount < 10:
                print("you get no coupon")
            elif total_amount >= 10 and total_amount < 60:
                discount_coupon = total_amount * DISCOUNT_LAYER_1 / 100
                print("you win a discount coupon of %.2f" % discount_coupon, "(", DISCOUNT_LAYER_1, "% of your purchase)")
            elif total_amount >= 60 and total_amount < 150:
                discount_coupon = total_amount * DISCOUNT_LAYER_2 / 100
                print("you win a discount coupon of %.2f" % discount_coupon, "(", DISCOUNT_LAYER_2, "% of your purchase)")
            elif total_amount >= 150 and total_amount < 210:
                discount_coupon = total_amount * DISCOUNT_LAYER_3 / 100
                print("you win a discount coupon of %.2f" % discount_coupon, "(", DISCOUNT_LAYER_3, "% of your purchase)")
            else:
                discount_coupon = total_amount * DISCOUNT_LAYER_4 / 100
                print("you win a discount coupon of %.2f" % discount_coupon, "(", DISCOUNT_LAYER_4, "% of your purchase)")
        except ValueError as e:
            print("invalid input, please input a number")

if __name__ == "__main__":
    main()

    
# Money Spent    	Coupon Percentage
# Less than $10	No coupon
# From $10 to less than $60      	8%
# From $60 to less than $150      	10%
# From $150 to less than $210     	12%
# From $210 or more          	14%