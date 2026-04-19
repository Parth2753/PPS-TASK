def crop_trend():
    try:
        n = int(input("Enter number of days: "))

        if n <= 0:
            print("Invalid input")
            return

        prices = []

        for i in range(n):
            price = float(input("Enter price for day " + str(i+1) + ": "))
            
            if price < 0:
                print("Invalid price")
                return
            
            prices.append(price)

        increasing = True
        decreasing = True

        for i in range(len(prices) - 1):
            if prices[i] >= prices[i + 1]:
                increasing = False
            if prices[i] <= prices[i + 1]:
                decreasing = False

        print("\nMarket Analysis:")

        if increasing:
            print("Trend: Increasing")
            print("Decision: SELL")

        elif decreasing:
            print("Trend: Decreasing")
            print("Decision: WAIT")

        else:
            print("Trend: Fluctuating")
            print("Decision: HOLD")

    except:
        print("Error")

crop_trend()
