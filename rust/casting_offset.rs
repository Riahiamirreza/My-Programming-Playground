
fn main() {
    let s: String = String::from("hello");
    let s_ref: &str = s.as_ref();
    let ptr: *const u8 = s_ref.as_ptr();
    for i in 0..s_ref.len() {
        unsafe {
            println!("{}", *ptr.offset(i as isize) as u8);
        }
    }
}
