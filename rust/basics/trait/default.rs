
trait Test {
    fn foo(&self) -> u32 {
        981
    }
}

struct A {}

struct B {}

impl Test for A {
    fn foo(&self) -> u32 {
        12
    }
}

// we don't implement Test::foo for B!
impl Test for B {}


fn main() {
    let a = A{};
    let b = B{};
    println!("a.foo: {}", a.foo());
    println!("b.foo: {}", b.foo());
}
