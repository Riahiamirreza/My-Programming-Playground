

struct A {
    name: String
}

impl A {
    fn new(name: String) -> Self {
        Self {
            name: name
        }
    }
}

impl B {
    fn new(age: u32) -> Self {
        Self {
            age: age
        }
    }
}

struct B {
    age: u32
}


trait View {
    fn view(&self);
}

impl View for A {
    fn view(&self) {
        println!("A.name: {}", self.name);
    }
}

impl View for B {
    fn view(&self) {
        println!("B.age: {}", self.age);
    }
}

fn view_all(v: &Vec<&dyn View>) {
    for i in v {
        i.view();
    }
}

fn main() {
    let a = A::new(String::from("ali"));
    let b = B::new(45 as u32);
    let mut v: Vec<&dyn View> = Vec::new();
    v.push(&a);
    v.push(&b);
    view_all(&v);
}
