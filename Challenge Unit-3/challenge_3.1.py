def linear_search_product(products, target_product):
  indices=[]
  for i in range (len(products)):
    if products[i]==target_product:
        indices.append(i)
  return indices
if _name=="__main_":
  products =                      ["lotus","lily","jasmine","lotus","daisy","rose"]                     
  target_product="lotus"
  indices=linear_search_product    (products,target_product)
  print(indices)