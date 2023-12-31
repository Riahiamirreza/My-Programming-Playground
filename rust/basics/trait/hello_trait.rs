
trait Hello {
    fn say_hi(&self);
}

impl Hello for String {
    fn say_hi(&self) {
        println!("hi {}", self);
    }
}

fn greeter(i: impl Hello) {
    i.say_hi();
}

fn main() {
    let s: String = String::from("Jack");
    s.say_hi();
    greeter(s);
}
