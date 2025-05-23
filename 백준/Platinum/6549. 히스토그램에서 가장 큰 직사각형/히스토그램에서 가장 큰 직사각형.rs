use std::collections::VecDeque;
use std::io::*;

struct Scanner { it: std::str::SplitAsciiWhitespace<'static>, }
impl Scanner {
    fn new() -> Self {
        let mut s = String::new();
        stdin().read_to_string(&mut s).ok();
        Self { it: s.leak().split_ascii_whitespace() }
    }
    fn read<T: std::str::FromStr>(&mut self) -> T {
        self.it.next().unwrap().parse::<T>().ok().unwrap()
    }
}



fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    loop {
        let n: usize = sc.read();
        if n == 0 { break; }
        let mut hist = vec![0; n];
        let mut stack: Vec<(usize, usize)> = Vec::new();
        for i in 0..n { hist[i] = sc.read(); }
        let mut area = 0;

        for i in 0..n {
            while let Some((j, h)) = stack.last() {
                if *h < hist[i] { break; }
                let j = stack.pop().unwrap().0;
                let w = if stack.is_empty() { i } else { i - stack.last().unwrap().0 - 1 };
                area = area.max(hist[j] * w);
            }
            stack.push((i, hist[i]));
        }
        while let Some((j, h)) = stack.pop() {
            let w = if stack.is_empty() { n } else { n - stack.last().unwrap().0 - 1 };
            area = area.max(hist[j] * w);
        }
        
        writeln!(so, "{}", area).ok();
    }
}