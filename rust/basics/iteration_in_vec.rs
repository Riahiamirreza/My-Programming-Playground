
fn main() {
    let v: Vec<i32> = vec![1, 2, 3, 4, 5].iter().map(|x| x * 2).collect();
    for i in v {
        println!("{}", i);
    }
}
