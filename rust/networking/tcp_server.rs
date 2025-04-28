use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};


fn main() {
    let listener = TcpListener::bind("localhost:5533").expect("Could not bind");

    for stream in listener.incoming() {
        match stream {
            Ok(s) => {
                handle_stream(s);
            },
            Err(e) => { eprintln!("error: {}", e); }
        }
    }
}


fn handle_stream(mut s: TcpStream) {
    let mut buf = [0u8; 512];
    loop {
        let bytes_read_count = s.read(&mut buf).expect("Could read from stream");
        if bytes_read_count == 0 {
            return;
        }
        s.write_all(&buf[0..bytes_read_count]).expect("Could not write to stream");
    }
}
