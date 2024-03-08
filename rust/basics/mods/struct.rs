
mod school {
    pub struct Student {
        pub name: String,
        pub age: u8,
        grade: f32
    }
    impl Student {
        pub fn new() -> Self {
            Self {
                name: "ali".to_string(),
                age: 12u8,
                grade: 12.3f32
            }
        }
    }
}

fn main() {
    use school::Student;
    let s = Student::new();
    println!("{0}, {1}", s.name, s.age);
    // can not access s.grade, as it's in a different module and private.
}
