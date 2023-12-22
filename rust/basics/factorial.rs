
fn fact(i: i32) -> i32 {
    (1..=i).product()
}

fn main() -> Result<(), ()> {
    let args = std::env::args().collect::<Vec<String>>();
    if args.len() == 2 {
        match args[1].parse() {
            Ok(i) => {
                println!("{}", fact(i));
                Ok(())
            }
            Err(_) => Err(())
        }
    } else {
        Err(())
    }
}
