function getSum(a, b) {
  if ( a == b ){
    return a
  } 

  let min = Math.min(a, b);
  let max = Math.max(a, b);

  let acc = (max - min + 1) * (min + max) / 2;
  return acc

}

module.exports = {
  getSum
}
