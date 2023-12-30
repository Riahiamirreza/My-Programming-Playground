
fn consume<I: Iterator>(iter: I) -> ()
    where I::Item: std::fmt::Debug
{
    for i in iter {
        println!("{:?}", i);
    }
}

fn main() {
    consume(String::from("hi").chars());
    consume(vec![1, 2, 3].iter());
    consume(1..10);
}
