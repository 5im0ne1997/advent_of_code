use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    let input_file = BufReader::new(File::open("./src/input.txt").expect("Fail to read file"));
    let mut safe_report1: u32 = 0;
    let mut safe_report2: u32 = 0;
    for line in input_file.lines() {
        let mut list_number: Vec<u32> = Vec::new();
        for number in line.unwrap().split_whitespace() {
            list_number.push(number.parse().unwrap());
        }

        if resolve(list_number.clone()) {
            safe_report1 += 1;
            safe_report2 += 1;
        } else {
            let vec_lenght = list_number.len();
            for i_for_lenght in 0..=vec_lenght - 1 {
                let mut temp_vec: Vec<u32> = list_number.clone();
                temp_vec.remove(i_for_lenght);
                if resolve(temp_vec.clone()) {
                    safe_report2 += 1;
                    break;
                }
            }
        }
    }

    println!("{safe_report1}");
    println!("{safe_report2}");
}

fn resolve(list: Vec<u32>) -> bool {
    let mut previous_number: u32 = 0;
    let mut up = false;
    let mut down = false;
    let mut flag = true;
    for (i, number) in list.into_iter().enumerate() {
        let current_number: u32 = number;
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
    return flag;
}
