use std::io::{stdin, Read};

fn calc(n: usize, digit: usize, ans: &mut [usize; 10]) {
    let mut n = n;
    while n > 0 {
        ans[n % 10] += digit;
        n /= 10;
    }
}

fn count(a: usize, b: usize, digit: usize, ans: &mut [usize; 10]) {
    let (mut a, mut b) = (a, b);
    while a % 10 != 0 && a <= b {
        calc(a, digit, ans);
        a += 1;
    }
    if a > b { return; }
    while b % 10 != 9 && a <= b {
        calc(b, digit, ans);
        b -= 1;
    }
    for i in 0..10 {
        ans[i] += (b / 10 - a / 10 + 1) * digit;
    }
    count(a / 10, b / 10, digit * 10, ans);
}

fn main() {
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    let mut ans: [usize; 10] = [0; 10];
    count(1, n, 1, &mut ans);
    for i in &ans {
        print!("{} ", i);
    }
}