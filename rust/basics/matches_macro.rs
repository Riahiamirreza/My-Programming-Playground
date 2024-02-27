

fn main() {
    let x = 1;
    let i_am_false = matches!(x, 2);
    let i_am_true = matches!(x, 1);

    assert!(!i_am_false);
    assert!(i_am_true);
}
