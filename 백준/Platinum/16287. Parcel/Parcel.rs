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

    let w: usize = sc.read();
    let n: usize = sc.read();

    let mut items = vec![0; n];
    for i in 0..n { items[i] = sc.read(); }

    let mut p1: Vec<usize> = vec![0; w];
    let mut p2: Vec<usize> = vec![0; w];
    let mut ans = "NO";

    for i in 0..n {
        for j in i + 1..n {
            let k = items[i] + items[j];
            if items[i] + items[j] < w { p1[k] = i; p2[k] = j; }
        }
    }

    'outer: for i in 0..n {
        for j in i + 1..n {
            let k = items[i] + items[j];
            if k < w && p1[w - k] > 0 {
                if p1[w - k] != i && p1[w - k] != j && p2[w - k] != i && p2[w - k] != j {
                    ans = "YES";
                    break 'outer;
                }
            }
        }
    }

    writeln!(so, "{}", ans).ok();
}