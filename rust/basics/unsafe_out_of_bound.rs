use std::env;

fn main() {
    let arr = [0u8; 5];
    if env::args().len() > 1 {
        let args: Vec<String> = env::args().collect();
        for arg in &args[1..] {
            let index: Option<usize> = match arg.trim().parse() {
                Ok(n) => Some(n),
                Err(_) => None
            };
            match index {
                Some(n) => unsafe {
                    let r = arr.get_unchecked(n);
                    println!("{: >3}: {}", n, r);
                }
                None => {
                    panic!("invalid argument");
                }
            };
        }
        return;
    }
    for i in 0..20 {
        if i >= arr.len() {
            unsafe {
                let r = arr.get_unchecked(i);
                println!("{: >2}: {}",i, r);
            }
        } else {
            println!("{: >2}: {}", i, arr[i]);
        }
    }
}
