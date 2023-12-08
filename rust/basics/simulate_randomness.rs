use std::io::prelude::*;
use std::fs;
use std::time;

const ENTROPY_SOURCE_PATH: &str = "/dev/urandom";

fn generate() -> Result<u64, ()> {
    let mut x: u64 = time::SystemTime::now().duration_since(time::UNIX_EPOCH).unwrap().as_secs() as u64;
    let mut f: fs::File = fs::File::open(ENTROPY_SOURCE_PATH).unwrap();
    let mut buffer = [0u8; 100];
    let _ = f.read_exact(&mut buffer);
    for i in buffer {
        x = x.overflowing_add(i as u64).0;
        x = x.overflowing_mul(i as u64).0;
    }
    Ok(x)
}

fn main() {
    let x = match generate() {
        Ok(v) => v,
        Err(e) => panic!("{:?}", e)
    };
    println!("{x}");
}
