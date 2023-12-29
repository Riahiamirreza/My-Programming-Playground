use std::thread;
use std::time::Duration;


fn main() {
    let handle: thread::JoinHandle<_> = thread::spawn(|| {
            for i in 1..100 {
                println!("{i}");
                thread::sleep(Duration::from_millis(10));
            }
        }
    );
    for i in 1..20 {
        println!("{i}");
        thread::sleep(Duration::from_millis(20));
    };
    handle.join();
}
