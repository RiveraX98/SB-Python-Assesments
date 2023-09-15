function snakeToCamel(word) {
    // snakeToCamel("awesome_sauce"); // "awesomeSauce"
  
    let fullList = word.split("_")
    let firstWord=fullList.slice(0,1)
    let restWords =fullList.slice(1)

    let cappedWords=restWords.map(function(word){
        first= word[0]
        rest= word.slice(1)
        firstCapped=first.toUpperCase()
        capped = firstCapped+rest
        return capped
    })

    concatWord = firstWord.concat(cappedWords)
    cammeled = concatWord.join("")
    return cammeled
    
    
}





