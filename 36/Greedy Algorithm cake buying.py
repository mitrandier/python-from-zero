money = 98
prices = [18 , 23 , 53 , 38 , 40 , 25 , 13]
n = len(prices)

# sort the cakes based on their prices
for i in range(n):
    for j in range(i):
        if prices[i] < prices[j]:
            t = prices[i]
            prices[i]= prices[j]
            prices[j] = t
# print(prices)
i = 0
while prices[i] <= money:
    print(f"buy cake, price: {prices[i]}.")
    money = money - prices[i]
    i = i+ 1
print(f"Remaining money: {money}")
