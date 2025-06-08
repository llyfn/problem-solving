use std::io::*;
use std::collections::HashMap;
use std::collections::HashSet;

struct Scanner { it: std::collections::VecDeque<String>, }
impl Scanner {
    fn new() -> Self {
        Self { it: std::collections::VecDeque::new(), }
    }
    fn read<T: std::str::FromStr>(&mut self) -> T {
        while self.it.is_empty() {
            let mut line = String::new();
            stdin().read_line(&mut line).unwrap();
            self.it.extend(line.split_whitespace().map(String::from));
        }
        self.it.pop_front().unwrap().parse().ok().unwrap()
    }
}

struct DisjointSet {
    parent: Vec<usize>,
}

impl DisjointSet {
    fn new(n: usize) -> Self {
        let parent = (0..=n).collect();
        Self { parent }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x { self.parent[x] = self.find(self.parent[x]); }
        self.parent[x]
    }

    fn union(&mut self, mut x: usize, mut y: usize) {
        (x, y) = (self.find(x), self.find(y));
        if x < y { self.parent[y] = x; } else { self.parent[x] = y; }
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let (n, m): (usize, usize) = (sc.read(), sc.read());

    let mut ds = DisjointSet::new(n);

    for _ in 0..m {
        let (o, mut a, mut b): (usize, usize, usize) = (sc.read(), sc.read(), sc.read());

        if o == 0 {
            ds.union(a, b);
        } else if o == 1 {
            if ds.find(a) == ds.find(b) {
                writeln!(so, "YES").unwrap();
            } else {
                writeln!(so, "NO").unwrap();
            }
        }
    }
}
