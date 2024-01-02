
trait Greeter {
    fn greet(&self);
}


impl Greeter for i32 {
    fn greet(&self) -> () {
        println!("Hi, I'm {}", self);
    }
}

fn generic_greet<T: Greeter>(i: &T) {
    i.greet();
}

fn dynamic_greet(i: Box<dyn Greeter>) {
    i.greet();
}

fn main() {
    let i = 8;
    let j = Box::new(7);

    generic_greet(&i);
    dynamic_greet(j);
}
