use std::fs;
use std::env;


fn main() {
    let args: Vec<String> = env::args().collect();
    let file_name: String;
    let content: String;
    match args.len() {
        1 | 0 => panic!("Not enough argument provided"),
        _ => {
            file_name = args[1].clone();
        }
    };
    match fs::read_to_string(file_name) {
        Ok(filecontent) => {content = filecontent},
        Err(err) => panic!("Invalid file name is given. Error: {}", err)
    };
    println!("{}", content);
}
