function acceleration() {
    readline = require("readline-sync")
    var initial_velocity = readline.question("What is the initial velocity?: ")
    var final_velocity = readline.question("What is the final velocity?: ")
    var startiing_time = readline.question("What is the starting line?: ")
    var ending_time = readline.question("What is the ending time?: ")
    var delta_t = ending_time - starting_time
    var delta_v = final_velocity - initial_velocity
}