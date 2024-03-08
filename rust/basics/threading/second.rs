fn spawn_counter(n: u32) -> std::thread::JoinHandle<()> {
    std::thread::spawn(move || {
        for i in 0..n {
            println!("{:?}: {}", std::thread::current().id(), i);
        }
    })
}

fn main() {
    let handles: Vec<std::thread::JoinHandle<()>> = (0..10).map(|i| spawn_counter(i)).collect::<Vec<_>>();
    for _ in 0..100000000 {
        print!("");
    }
    for h in handles {
        let _ = h.join();
    }
}
