// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

function factorial(num) {
    if (num < 0) 
          return -1;
    else if (num == 0) 
        return 1;
      else {
          return (num * factorialize(num - 1));
      }

function fib(num){
  var a = 1, b = 0, tem;

  while (num >= 0){
    tem = a;
    a = a + b;
    b = tem;
    num--;
  }

  return b;
}

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
