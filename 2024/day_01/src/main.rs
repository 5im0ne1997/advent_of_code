use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    let input_file = BufReader::new(File::open("./src/input.txt")
        .expect("Fail to read file"));

    let mut a: Vec<u32> = Vec::new();
    let mut b: Vec<u32> = Vec::new();

    for line in input_file.lines() {
        for (i, word) in line.unwrap().split_whitespace().enumerate() {
            match i {
                0 => a.push(word.parse().unwrap()),
                1 => b.push(word.parse().unwrap()),
                _ => continue,
            }
        }
    }    
    a.sort();
    b.sort();
    
}
