
fn execute(f: fn(i32) -> i32, i: i32) -> i32 {
    f(i)
}

fn main() {
    let f: fn(i32) -> i32 = |i| i * 2;

    println!("{}", execute(f, 12));
}
