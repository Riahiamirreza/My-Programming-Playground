
macro_rules! add {
    ($a:expr, $b:expr) => (
        $a + $b
    );
}

fn main() {
    let sum = add!(34, 1+5);
    assert_eq!(sum, 40);
}
