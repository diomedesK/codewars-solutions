
function findOutlier(integers){

  let b = 0
  for ( let i = 0; i < 3; i++ ){
    integers[i] % 2 == 0? b++ : b --;
  }
  let isNormEven = b > 0

  for( let value of integers ){
    let isValueEven = value % 2 == 0;

    if( isNormEven ^ isValueEven  ){
      return value
    } 

  }

}

module.exports = findOutlier

