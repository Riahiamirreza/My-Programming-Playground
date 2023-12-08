use std::io;


fn main() {
    let x: Option<i32> = { 
        let mut buffer: String = String::new();
        match io::stdin().read_line(&mut buffer) {
            Ok(_) => match buffer.trim().parse() {
                Ok(n) => Some(n),
                Err(_) => None
            }
            Err(_) => None
        }
    };
    match x {
        Some(s) => println!("input is: {}", s),
        None => println!("input is invalid")
    };
}
