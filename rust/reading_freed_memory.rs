
use std::mem;
use std::ptr;

struct Secret {
    data: [u8; 8]
}

fn main() {
    let secret = Secret {data: [11u8; 8]};
    let secret_location = &secret.data as *const u8;

    mem::drop(secret);
    let mut recovered_secret = [0u8; 8];
    unsafe {
        ptr::copy_nonoverlapping(
            secret_location,
            recovered_secret.as_mut_ptr(),
            8
        );
    }
    println!("recovered secred: {:?}", recovered_secret);
}
