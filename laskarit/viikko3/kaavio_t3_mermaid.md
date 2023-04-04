---
title: Vehicle
---
classDiagram
    
    Machine <|-- Main : Use vehicle
    Engine <|-- Machine : drive() (if quantity >0)
    Machine <|-- Gas_tank :quantity
    Gas_tank <|-- Machine :tank.fill()
    Engine <|-- Gas_tank :quantity
    Gas_tank <|-- Engine :use_energy() if is_running()
    Gas_tank <|-- Engine :start() (if quantity >5)
    class Main{
    
    }
    class Engine{
        start()
        is_running()
        use_energy()
    }
    class Machine{
        drive()
        gas_tank
    }
    class Gas_tank{
        quantity
        fill()
        consume()

    }

