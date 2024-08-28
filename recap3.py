def top_n_items(items, n):
    sorted_items = sorted(items, reverse=True)
    return sorted_items[:n]

items = [10, 20, 5, 7, 35, 12, 15]
top_n = 3
result = top_n_items(items, top_n)
print(f"Top {top_n} items:", result)
