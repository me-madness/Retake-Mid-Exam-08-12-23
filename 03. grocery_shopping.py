list_of_product = input().split("|")
command = input().split("%")
new_list_of_products = []
count_product = 1

while command[0] != "Shop!":
    
    if command[0] == "Important":
        product = command[1]
        if product not in list_of_product:
            list_of_product.insert(0,product)
        else:
            list_of_product.remove(product)
            list_of_product.insert(0,product)   
    elif command[0] == "Add":
        if product not in list_of_product:
            list_of_product.append(product)
        else:
            print("The product is already in the list.")
    elif command[0] == "Swap":
        product_one = command[1]
        product_two = command[2]
        if product_one not in list_of_product:
            print(f"Product {product_one} missing!")
        else:
            if product_two not in list_of_product:
                print(f"Product {product_two} missing!")
            else:
                a, b = list_of_product.index(product_one), list_of_product.index(product_two)
                list_of_product[b], list_of_product[a] = list_of_product[a], list_of_product[b]      
    elif command[0] == "Remove":
        ex_product = command[1]
        if ex_product not in list_of_product:
            print(f"Product {ex_product} isn't in the list.")
        else:    
            list_of_product.remove(ex_product)
    elif command[0] == "Reversed":
        new_list_of_products.reverse(list_of_product)
        list_of_product = new_list_of_products
    command = input().split("%")
    
for product in list_of_product:
    print(f"{count_product}.{product}") 
    count_product += 1   
    
    
# eggs|milk|bread|fish    
# Important%bread
# Swap%eggs%tomato
# Shop!


# apple|cheese|salt|bananas
# Remove%cheese
# Swap%salt%bananas
# Shop!