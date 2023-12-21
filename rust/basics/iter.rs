
struct CountDown {
    counter: i32
}

impl CountDown {
    fn new(start: i32) -> Self {
        Self {
            counter: start
        }
    }
}

impl Iterator for CountDown {
    type Item = i32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.counter > 0 {
            self.counter -= 1;
            Some(self.counter+1)
        } else {
            None
        }
    }
}

fn main() {
    let counter: i32 = std::env::args().collect::<Vec<String>>()[1].parse().unwrap();
    for i in CountDown::new(counter) {
        println!("{}", i);
    }
}
