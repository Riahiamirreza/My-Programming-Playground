use std::env;

fn main() -> () {
    let args: Vec<String> = env::args().collect();
    if args.len() > 1 {
        for arg in &args[1..] {
            let i: Option<i32> = match arg.parse() {
                Ok(x) => Some(x),
                Err(_) => None
            };
            match i {
                Some(v) => println!("{}", v),
                None => panic!("can't parse {} into a number.", arg)
            };
        }
    }
}
