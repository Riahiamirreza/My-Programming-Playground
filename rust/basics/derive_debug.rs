
#[derive(Debug)]
struct Student {
    name: String,
    age: u8
}


fn main() {
    let s1 = Student {name: String::from("ali"), age: 12 as u8};
    let s2 = Student {name: String::from("akbar"), age: 15u8};

    println!("{:?}, {:?}", s1, s2);
}
