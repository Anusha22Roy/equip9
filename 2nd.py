def find_best_prices(requests, sellers):
    # Organize sellers by equipment type with their prices in a dictionary
    seller_dict = {}
    
    for equip, price in sellers:
        if equip not in seller_dict:
            seller_dict[equip] = []
        seller_dict[equip].append(price)
    
    # Sort seller prices for each equipment type
    for equip in seller_dict:
        seller_dict[equip].sort()
    
    # Process each request and find the lowest valid price
    result = []
    for equip, max_price in requests:
        if equip in seller_dict:
            # Find the lowest available price that meets the max_price constraint
            best_price = None
            for price in seller_dict[equip]:
                if price <= max_price:
                    best_price = price
                    break
            result.append(best_price)
        else:
            result.append(None)
    
    return result

# Example Input
requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

# Running the function
output = find_best_prices(requests, sellers)
print(output)