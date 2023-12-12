fn main() {
    let mut v: Vec<String> = Vec::new();
    let (s1, s2) = (String::from("hello"), String::from("world!"));
    v.push(s1);
    v.push(s2);
    println!("{} {}", v[0], v[1]);
}
