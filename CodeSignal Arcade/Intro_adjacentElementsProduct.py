def adjacentElementsProduct(inputArray):
    val = []
    for i in range(1,len(inputArray)):
        product = inputArray[i-1] * inputArray[i]
        val.append(product)
    return(max(val))