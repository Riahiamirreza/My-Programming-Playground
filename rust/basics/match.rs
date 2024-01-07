
fn main() {
    for i in -3..10 {
        match i {
            1 => println!("one"),
            2|3|4 => println!("two, three or four"),
            5 => println!("five"),
            -1 => println!("negative!"),
            _ => println!("something else"),
        };
    }
}
