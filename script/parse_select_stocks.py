with open("./tmp.txt", 'r') as f:
    data = f.read().splitlines()
    
    stock_ids = []
    for i, entry in enumerate(data):
        if (i-1) % 10 == 0:
            stock_id = int(entry.split()[0])
            stock_ids.append(stock_id)

print ("stock_ids:", stock_ids)
        