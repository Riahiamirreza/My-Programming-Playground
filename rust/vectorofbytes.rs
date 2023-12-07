
fn main() {
    let v: Vec<i8> = vec![1i8, 2i8, 3i8];
    let w: Vec<u8> = vec![1u8, 2u8, 3u8];
    for i in v {
        println!("{i}");
    }
    for j in w {
        println!("{}", j);
    }
}
