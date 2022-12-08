import scala.io.Source
import scala.collection.mutable.Map
import scala.collection.immutable.ListMap


@main def countCals = 
    val lines = Source.fromFile("calories_test.txt").getLines.toList
    var elfCount = 0
    var elfMap = Map[Int, Int]()

    for line <- lines do
        if line.isBlank() then
            elfCount += 1
        else
            val int_line = line.toInt

            if elfMap.contains(elfCount) then
                elfMap(elfCount) += int_line
            else
                elfMap += elfCount -> int_line

    
    var elfMap_sorted = ListMap(elfMap.toMap.toSeq.sortWith(_._2 > _._2):_*)
    
    var calCount = 0
    for (key, value) <- elfMap_sorted.take(3) do
        calCount += value

    println(calCount)
    
                