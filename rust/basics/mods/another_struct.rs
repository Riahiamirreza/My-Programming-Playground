
mod a {
    pub struct B(pub i32);
}

fn main() {
    let b = a::B(11);
    println!("{}", b.0);
}
