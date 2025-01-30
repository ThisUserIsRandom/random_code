/**
 * You can edit, run, and share this code.
 * play.kotlinlang.org
 */

class rect(a:Int,b:String){
    val peri = a*a 
    val name = "reactyangly"
}

fun main() {
    
    var i : Long = 123456789012
    var j : Float = 2.33f
  	var str = "this will work too"  
    var Nullable:Int? // nullable value
    
    println("number is $i")
    println("sum of two numbers : ${4+78}")
    println("this is printable" /*this is a comment inside of a line*/+"lets test this")
    
    var test : Int = 10;
    if(test%2==0){
        println("even hai")
    } else {
        println("odd hai")
    }
    
    val reactangle : rect = rect(5,"damndoom")
    
    println("peri is ${reactangle.peri} , name = ${reactangle.name}")
    
    val arra = listOf("one","two")
    
    for (item in 0..10 step 2){ // in arra / arra.indices // steps
        println(item)
    }
    
}

var list = listOf(-1,-2,1,2,3)
val positives = list.filter { x -> x > 0 } // to filter values
if(1 in list) // tells the presence 
val map = mapOf("a" to 1, "b" to 2, "c" to 3)

object Resource {
    val name = "Name"
} // this is called a signleton
