use std::io::*;

fn main() {
    let mut so = BufWriter::new(stdout().lock());

    let mut s = String::new();
    stdin().read_to_string(&mut s).unwrap();
    let mut lines = s.lines();
    let bt = lines.next().unwrap().to_string();
    let mut t = bt.as_bytes();
    let bp = lines.next().unwrap().to_string();
    let mut p = bp.as_bytes();

    let n = t.len();
    let m = p.len();

    let mut pi = [0; 1000000];
    let mut i = 0;
    for j in 1..m {
        while i > 0 && p[i] != p[j] { i = pi[i - 1]; }
        if p[i] == p[j] {
            i += 1;
            pi[j] = i;
        }
    }

    let mut idx = 0;
    let mut cnt = 0;
    let mut str = String::new();
    for j in 0..n {
        while idx > 0 && p[idx] != t[j] { idx = pi[idx - 1]; }
        if p[idx] == t[j] {
            if idx == m - 1 {
                cnt += 1;
                str.push_str(&format!("{} ", j - m + 2));
                idx = pi[idx];
            } else { idx += 1; }
        }
    }

    writeln!(so, "{}", cnt).ok();
    writeln!(so, "{}", str.trim()).ok();
}