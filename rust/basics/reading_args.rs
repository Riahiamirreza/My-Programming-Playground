use std::env;


fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        panic!("Invalid argument is passed");
    }
    let command = &args[1];

    if command == "say_hi" {
        println!("Hi");
    }

}
