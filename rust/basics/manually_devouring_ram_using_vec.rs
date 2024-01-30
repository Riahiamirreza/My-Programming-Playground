
fn main() {
    let mut v = Vec::new();
    
    loop {
        let mut input: String = String::new();
        let _ = std::io::stdin().read_line(&mut input);
        let n = input.trim().parse().unwrap_or(0);

        v.extend((0..n).map(|i| (i, format!("{}", i))));
        println!("len {}, capacity {}", v.len(), v.capacity());
    }
}
