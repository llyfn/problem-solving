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

struct Point { x: i64, y: i64, tx: i64, ty: i64 }

fn ccw(a: &Point, b: &Point, c: &Point) -> i64 {
    (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x)
}

fn det(a: &Point, b: &Point) -> i64 {
    a.tx * b.ty - a.ty * b.tx
}

fn angle_cmp(a: &Point, b: &Point) -> std::cmp::Ordering {
    let d = det(a, b);
    if d > 0 { std::cmp::Ordering::Less }
    else if d < 0 { std::cmp::Ordering::Greater }
    else { (a.tx * a.tx + a.ty * a.ty).cmp(&(b.tx * b.tx + b.ty * b.ty)) }
}

fn main() {
    let mut sc = Scanner::new();

    let n = sc.read::<usize>();
    let mut points: Vec<Point> = Vec::with_capacity(n);
    for _ in 0..n {
        points.push(Point { x: sc.read::<i64>(), y: sc.read::<i64>(), tx: 0, ty: 0 });
    }
    points.sort_by(|a, b| a.y.cmp(&b.y).then(a.x.cmp(&b.x)));
    for i in 0..n {
        points[i].tx = points[i].x - points[0].x;
        points[i].ty = points[i].y - points[0].y;
    }
    points[1..].sort_by(|a, b| angle_cmp(a, b));
    let mut stack = vec![0, 1];
    let mut ed = 2;
    while ed < n {
        while stack.len() >= 2 {
            let mid = stack.pop().unwrap();
            let st = *stack.last().unwrap();
            if ccw(&points[st], &points[mid], &points[ed]) > 0 {
                stack.push(mid);
                break;
            }
        }
        stack.push(ed);
        ed += 1;
    }

    println!("{}", stack.len());
}