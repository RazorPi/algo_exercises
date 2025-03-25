function hasDuplicateValue(array){
    for(let i = 0; i < array.length; i++){
        for(let j = 0; j < array.length; j++){
            if(i !== j && array[i]=== array[j]){
                return true;
            }
        }
    }
    console.log(steps) // print number of steps if no duplicates
    return false
}