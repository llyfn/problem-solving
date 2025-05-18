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

const MAX_N: usize = 100001;
const MAX_H: usize = 18;

static mut PARENT: [[usize; MAX_H]; MAX_N] = [[0; MAX_H]; MAX_N];
static mut DEPTH: [usize; MAX_N] = [0; MAX_N];
static mut GRAPH: Vec<Vec<usize>> = Vec::new();
static mut HEIGHT: usize = 0;

fn find_parent(par: usize, curr: usize, dep: usize) {
    unsafe {
        if GRAPH[curr].is_empty() { return; }
        PARENT[curr][0] = par;
        DEPTH[curr] = dep;
        for &next in &GRAPH[curr] {
            if next != par { find_parent(curr, next, dep + 1); }
        }
    }
}

fn find_lca(mut a: usize, mut b: usize) -> usize {
    unsafe {
        if DEPTH[a] < DEPTH[b] { return find_lca(b, a); }
        let mut diff = DEPTH[a] - DEPTH[b];
        for i in 0..MAX_H {
            if (diff & 1 << i) > 0 { a = PARENT[a][i]; }
        }
        if a != b {
            for i in (0..=HEIGHT).rev() {
                if PARENT[a][i] != 0 && PARENT[a][i] != PARENT[b][i] {
                    a = PARENT[a][i];
                    b = PARENT[b][i];
                }
            }
            a = PARENT[a][0];
        }
        a
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let n = sc.read::<usize>();
    unsafe {
        GRAPH = vec![Vec::new(); n + 1];
        HEIGHT = (n as f64).log2().ceil() as usize;
    }
    for _ in 0..(n - 1) {
        let a = sc.read::<usize>();
        let b = sc.read::<usize>();
        unsafe {
            GRAPH[a].push(b);
            GRAPH[b].push(a);
        }
    }
    find_parent(0, 1, 0);
    unsafe {
        for i in 1..=HEIGHT {
            for j in 2..=n {
                if PARENT[j][i - 1] != 0 {
                    PARENT[j][i] = PARENT[PARENT[j][i - 1]][i - 1];
                }
            }
        }
    }

    let m = sc.read::<usize>();

    for _ in 0..m {
        let a = sc.read::<usize>();
        let b = sc.read::<usize>();
        writeln!(so, "{}", find_lca(a, b));
    }
}