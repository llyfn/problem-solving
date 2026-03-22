# [Platinum IV] Friends - 21333 

[문제 링크](https://www.acmicpc.net/problem/21333) 

### 성능 요약

메모리: 106292 KB, 시간: 800 ms

### 분류

자료 구조, 집합과 맵, 트리를 사용한 집합과 맵

### 제출 일자

2026년 3월 22일 09:31:22

### 문제 설명

<p>$N$ friends are playing a game. The game is played on a row of $L$ squares, numbered from $0$ to $L - 1$, where squares $i$ and $i+1$ are adjacent to each other. At most one friend stand on each square at any given time. In each step of the game, one friend jumps from its current square to a new (non-occupied) square.</p>

<p>In any moment of the game, the <em>score</em> of a friend is the length of the longest contiguous segment of friends it is part of. This means that if a friend stands on some position $x$, and there are friends on positions $a, a + 1, ..., x - 1, x, x + 1, ..., b - 1, b$, the score of the friend is $b - a + 1$.</p>

<p>The total score of the game is the sum of scores for all friends. At various times during the game, the friends wonder what their current total score is.</p>

### 입력 

 <p>The sample judge reads input in the following format:</p>

<ul>
	<li>line $1$: <code>N L Q</code></li>
	<li>line $2$: <code>P[0] P[1] .. P[N - 1]</code></li>
	<li>lines $3$ to $3 + Q - 1$: each line represents either a jump or a score question. If the line is <code>0 A B</code>, a jump from $A$ to $B$ is to be made, and if the line is <code>1</code> a scoring question is to be made.</li>
</ul>

### 출력 

 <p>For each scoring question, the judge writes a line with the return value of <code>score()</code>.</p>

