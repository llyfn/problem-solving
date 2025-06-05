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

const MOD: usize = 1000003;
fn matmul(a: &Vec<Vec<usize>>, b: &Vec<Vec<usize>>) -> Vec<Vec<usize>> {
    let n = a.len();
    let mut r = vec![vec![0; n]; n];
    for i in 0..n {
        for j in 0..n {
            for k in 0..n {
                r[i][j] += a[i][k] * b[k][j];
                r[i][j] %= MOD;
            }
        }
    }
    r
}
fn matpow(a: &Vec<Vec<usize>>, p: usize) -> Vec<Vec<usize>> {
    if p == 1 {
        a.clone()
    } else if p % 2 == 1 {
        let r = matpow(a, p - 1);
        matmul(&r, a)
    } else {
        let r = matpow(a, p / 2);
        matmul(&r, &r)
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let (n, s, e, t)= (sc.read::<usize>(), sc.read::<usize>() - 1, sc.read::<usize>() - 1, sc.read::<usize>());

    let mut mat: Vec<Vec<usize>> = vec![vec![0; 5 * n]; 5 * n];
    for i in 0..n { for j in 1..5 { mat[5 * i + j][5 * i + j - 1] = 1; } }

    for i in 0..n {
        for (j, c) in sc.read::<String>().char_indices() {
            let d = c.to_digit(10).unwrap() as usize;
            if d == 1 { mat[5 * i][5 * j] = 1; }
            else if d > 1 { mat[5 * i][5 * j + d - 1] = 1; }
        }
    }

    mat = matpow(&mat, t);

    write!(so, "{} ", mat[5 * s][5 * e]).unwrap();
}