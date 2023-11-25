String.prototype.toJadenCase = function(){
  let res = this.toString()

  res = res.charAt(0).toUpperCase() + res.substring(1)

  for (let i = 0, len = res.length; i < len; i++) {
    if(res.charAt(i) == " " ){
      res = res.substring(0, i + 1) + res.charAt(i + 1).toUpperCase() + res.substring(i + 2)
    }

  }

  return res

}

module.exports = {
  String
}
