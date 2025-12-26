# [Gold I] Building A New Barn - 6222 

[문제 링크](https://www.acmicpc.net/problem/6222) 

### 성능 요약

메모리: 34456 KB, 시간: 44 ms

### 분류

수학

### 제출 일자

2025년 12월 26일 18:01:20

### 문제 설명

<p>After scrimping and saving for years, Farmer John has decided to build a new barn. He wants the barn to be highly accessible, and he knows the coordinates of the grazing spots of all N (2 <= N <= 10,000) cows. Each grazing spot is at a point with integer coordinates (X_i, Y_i) (-10,000 <= X_i <= 10,000; -10,000 <= Y_i <= 10,000). The hungry cows never graze in spots that are horizontally or vertically adjacent.</p>

<p>The barn must be placed at integer coordinates and cannot be on any cow's grazing spot. The inconvenience of the barn for any cow is given the Manhattan distance formula |X-X_i|+|Y-Y_i|, where (X, Y) and (X_i, Y_i) are the coordinates of the barn and the cow's grazing spot, respectively.  Where should the barn be constructed in order to minimize the sum of its inconvenience for all the cows?</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 contains two space-separated integers which are the grazing location (X_i, Y_i) of cow i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: Two space-separated integers: the minimum inconvenience for the barn and the number of spots on which Farmer John can build the barn to achieve this minimum.</li>
</ul>

