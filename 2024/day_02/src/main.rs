use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    let input_file = BufReader::new(File::open("./src/input.txt").expect("Fail to read file"));
    let mut safe_report: u32 = 0;
    for line in input_file.lines() {
        let mut previous_number: u32 = 0;
        let mut up = false;
        let mut down = false;
        let mut flag = true;
        for (i, number) in line.unwrap().split_whitespace().enumerate() {
            let current_number: u32 = number.parse().unwrap();
            if i == 0 {
                previous_number = current_number;
            } else {
                let sum = current_number as f32 - previous_number as f32;
                if sum > 0 as f32 && sum < 4 as f32 {
                    up = true;
                } else if sum < 0 as f32 && sum > -4 as f32 {
                    down = true;
                } else {
                    flag = false;
                    break;
                }
            }
            previous_number = current_number;
            if up && down {
                flag = false;
                break;
            }
        }
        if flag {
            safe_report += 1;
        }
    }
    println!("{safe_report}");
}
