/**
 * Created by jaswanth on 01/06/17.
 */

package demo

import java.util.Random

fun main(args : Array<String>){
    println("Hello,world!")

    val name = "jaswanth"

    var age = "24"

    var bigint :Int = Int.MAX_VALUE

    var samllint :Int = Int.MIN_VALUE

    println("biggest int :$bigint")

    println("smallest int :$samllint")

    var double :Double = 1.1111111111111111


    var double2 :Double = 1.1111111111111111

    println("sum:${("hi how are u ".length)}")

    val tento1 = 1.rangeTo(20)

    for (x in tento1)
        println("$x")

    val ran = Random()
    val magicNumber = ran.nextInt(50)
    print("$magicNumber ")
}