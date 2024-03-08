
macro_rules! make_function {
    ($name:ident) => (
        fn $name() {
            println!("{}: hello", stringify!($name));
        }
    );
}


fn main() {
    make_function!(foo);
    make_function!(bar);

    foo();
    bar();
}
