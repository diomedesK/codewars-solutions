function findOdd(A) {

  let countingMap = A.reduce( (acc, val) => {
    acc[val] = A.reduce( (acc, curr) => curr === val? acc + 1 : acc, 0 )
    return acc
  }, {})

  for ( let key in countingMap ) {
    let value = countingMap[key]
    if(value % 2 != 0){
      return parseInt(key, 10)
    }
  }

}

module.exports = {
  findOdd
}
