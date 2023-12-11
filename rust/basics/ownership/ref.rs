
fn say_hi(name: &String) -> () {
    println!("Hi, {}", name);
}

fn main() {
    let s: String = String::from("Ali");
    say_hi(&s);
    let another = format!("name: {}", s);
    println!("{}", another);
}
