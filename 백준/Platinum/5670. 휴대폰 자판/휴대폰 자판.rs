use std::io::*;
use std::collections::HashMap;

struct Node { key: char, data: Option<String>, children: HashMap<char, Node> }

impl Node {
    fn new(key: char) -> Self {
        Self { key, data: None, children: HashMap::new(), }
    }
}

struct Trie { head: Node }

impl Trie {
    fn new(head: Node) -> Self {
        Self { head }
    }

    fn insert(&mut self, word: String) {
        let mut curr = &mut self.head;
        for c in word.chars() { curr = curr.children.entry(c).or_insert(Node::new(c)); }
        curr.data = Some(word);
    }

    fn search_cost(&self, word: &str) -> usize {
        let mut curr = &self.head;
        let mut cost = 1;
        curr = curr.children.get(&word.chars().next().unwrap()).unwrap();
        for c in word.chars().skip(1) {
            if curr.children.len() > 1 || curr.data.is_some() { cost += 1; }
            curr = curr.children.get(&c).unwrap()
        }
        cost
    }
}

fn main() {
    let stdin = stdin();
    let mut lines = stdin.lock().lines();
    let mut so = BufWriter::new(stdout().lock());
    while let Some(Ok(line)) = lines.next() {
        let n: usize = line.trim().parse().unwrap();
        let words: Vec<String> = (0..n).map(|_| lines.next().unwrap().unwrap()).collect();
        let mut trie = Trie::new(Node::new('\0'));
        for word in &words { trie.insert(word.clone()); }
        let cost = words.iter().map(|word| trie.search_cost(word)).sum::<usize>();
        writeln!(so, "{:.2}", (cost as f64) / (n as f64)).ok();
    }
}