
fn foo() {}

fn main() {
    let x = foo;
    println!("size of foo: {}", std::mem::size_of_val(&foo));
    println!("size of x: {}", std::mem::size_of_val(&x));
}
