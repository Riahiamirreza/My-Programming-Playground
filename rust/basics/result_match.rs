use std::env;


fn even_or_err(i: i32) -> Result<String, String> {
    if i%2 == 1 {Err("bad".to_string())} else {Ok(String::from("good"))}
}

fn main() {
    let args: Vec<String> = env::args().collect();
    match even_or_err(args.len() as i32) {
        Ok(_) => (),
        Err(msg) => panic!("{}", msg)
    };
}
