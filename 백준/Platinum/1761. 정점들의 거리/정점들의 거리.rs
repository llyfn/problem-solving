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

const MAX_N: usize = 40001;
const MAX_H: usize = 20;

static mut PARENT: [[usize; MAX_H]; MAX_N] = [[0; MAX_H]; MAX_N];
static mut DIST: [[usize; MAX_H]; MAX_N] = [[0; MAX_H]; MAX_N];
static mut DEPTH: [usize; MAX_N] = [0; MAX_N];
static mut GRAPH: Vec<Vec<(usize, usize)>> = Vec::new();

fn find_parent(par: usize, curr: usize, dep: usize, cost: usize) {
    unsafe {
        if GRAPH[curr].is_empty() { return; }
        PARENT[curr][0] = par;
        DIST[curr][0] = cost;
        DEPTH[curr] = dep;
        for &next in &GRAPH[curr] {
            if next.0 != par { find_parent(curr, next.0, dep + 1, next.1); }
        }
    }
}

fn find_dist(mut a: usize, mut b: usize) -> usize {
    unsafe {
        let mut dist = 0;
        if DEPTH[a] < DEPTH[b] { return find_dist(b, a); }
        let mut diff = DEPTH[a] - DEPTH[b];
        for i in 0..MAX_H {
            if (diff & 1 << i) > 0 {
                dist += DIST[a][i];
                a = PARENT[a][i];
            }
        }
        if a != b {
            for i in (0..MAX_H).rev() {
                if PARENT[a][i] != 0 && PARENT[a][i] != PARENT[b][i] {
                    dist += DIST[a][i] + DIST[b][i];
                    a = PARENT[a][i];
                    b = PARENT[b][i];
                }
            }
            dist += DIST[a][0] + DIST[b][0];
        }
        dist
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let n = sc.read::<usize>();
    unsafe { GRAPH = vec![Vec::new(); n + 1]; }
    for _ in 0..(n - 1) {
        let a = sc.read::<usize>();
        let b = sc.read::<usize>();
        let cost = sc.read::<usize>();
        unsafe {
            GRAPH[a].push((b, cost));
            GRAPH[b].push((a, cost));
        }
    }
    find_parent(0, 1, 0, 0);
    unsafe {
        for i in 1..MAX_H {
            for j in 2..=n {
                if PARENT[j][i - 1] != 0 {
                    PARENT[j][i] = PARENT[PARENT[j][i - 1]][i - 1];
                    DIST[j][i] = DIST[j][i - 1] + DIST[PARENT[j][i - 1]][i - 1];
                }
            }
        }
    }

    let m = sc.read::<usize>();

    for _ in 0..m {
        let a = sc.read::<usize>();
        let b = sc.read::<usize>();
        writeln!(so, "{}", find_dist(a, b));
    }
}