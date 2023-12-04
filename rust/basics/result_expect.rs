fn get_err() -> Result<(), ()> {
    Err(())
}

fn get_ok() -> Result<(), ()> {
    Ok(())
}

fn main() -> () {
    get_err().expect("the 'get_err' function is invoked");
    get_ok().expect("the get_ok function is invoked");
}
