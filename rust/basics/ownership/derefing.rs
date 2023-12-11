
fn main() {
    let x: Box<i32> = Box::new(1i32);
    let y: &Box<i32> = &x;
    let z: Box<&Box<i32>> = Box::new(&x);
    println!("{}", ***z);
    println!("{}", **y);
}
