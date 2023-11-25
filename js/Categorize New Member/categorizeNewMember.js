function openOrSenior(data){
  return data.map( (entry) => ( entry[0] >= 55 ) && ( entry[1] > 7 )? "Senior" : "Open")
}

module.exports = openOrSenior
