
fn main() {
    let mut counter: i32 = 0;
    let result = loop {
        counter += 1;
        println!("{}", counter);
        if counter == 10 {
            break counter * counter;
        }
    };
    println!("{}", result);
}
