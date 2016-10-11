function fizzBuzz(i)
{
    //test for fizzbuzz
    if (i%15 === 0){
        return ("FizzBuzz")    
    }
    //test for fizz
    else if ( i%3 === 0){
        return ("Fizz")
    }
    //test for buzz
    else if (i%5 === 0) {
        return ("Buzz")
        }
    //default statement    
    else {
        return (i);
    }
}
