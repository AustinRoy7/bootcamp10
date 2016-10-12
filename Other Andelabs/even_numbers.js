function isEven (n){
  //test data type of n
  ntype = typeof n;
  //assign boolean to false if data is a float
  if ( ntype == "float"){
    eventest = false;
  }
  //test integers for evenness and return boolean result
  else{
  n = Math.abs(n);
  eventest = Boolean (n%2 === 0);
  }
  return (eventest);
}
