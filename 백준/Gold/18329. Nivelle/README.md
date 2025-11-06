# [Gold I] Nivelle - 18329 

[문제 링크](https://www.acmicpc.net/problem/18329) 

### 성능 요약

메모리: 110736 KB, 시간: 164 ms

### 분류

애드 혹, 문자열, 두 포인터

### 제출 일자

2025년 11월 6일 19:23:17

### 문제 설명

<p><em>Original task description has been altered due to excessive violence. The following program is suitable for minors.</em></p>

<p>Bojan sees N cute little fluffy edible toys <em>(yaay!)</em> on a store shelf, ordered from 1 to N. Each fluffy toy is colored in one of 26 different colors. Each color is denoted by a lowercase letter from the English alphabet. Bojan wants to eat some of these toys <em>(drool)</em>.</p>

<p>For any set of toys, we can define its <em>colorfulness</em> as the number of different colors of toys in a set, divided by the total number of toys in a set. Bojan hates colorfulness. Bojan is very hungry. Bojan wants to eat a contiguous subsequence of toys.</p>

<p>Help Bojan find a contiguous subsequence of toys whose colorfulness is as small as possible.</p>

### 입력 

 <p>The first line contains an integer N (1 ≤ N ≤ 100 000), the length of array of toys from task description.</p>

<p>The second line contains a string S of length N. The i-th character of the string represents the color of i-th toy from the shelf.</p>

### 출력 

 <p>Output two indices L and R (1 ≤ L ≤ R ≤ N), which denote that the sought contiguous subsequence of toys is located at positions L, L + 1, . . . , R.</p>

<p>If there exists more than one contiguous subsequence with the same minimal colorfulness, you can output L and R which define any of them.</p>

