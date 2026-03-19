# [Platinum V] Euclidean Nim - 15617 

[문제 링크](https://www.acmicpc.net/problem/15617) 

### 성능 요약

메모리: 1040 KB, 시간: 24 ms

### 분류

수학, 정수론, 게임 이론, 유클리드 호제법

### 제출 일자

2026년 3월 19일 13:21:57

### 문제 설명

<p>Euclid and Pythagoras are pseudonyms of two Byteotians for their love of mathematical puzzles. Lately, they spend evenings playing the following game. There is a stack of n stones on the table. Friends perform alternating moves. Euclid's move consists of taking any positive multiple of p stones from the stack (providing the stack contains at least p stones) or adding exactly p stones to the stack-adding the stones is possible, however, only in case the stack contains less than p stones. Pythagoras' move is analogical, except that either he takes a multiple of q stones, or adds exactly q stones. The winner is the player who empties the stack. Euclid begins the game.</p>

<p>Friends wonder whether they have worked out this game perfectly. Help them and write a program that will state what should be the result of the game, providing both players are making optimal moves.</p>

### 입력 

 <p>The first line of input contains one integer t (1 ≤ t ≤ 1,000) denoting the number of test cases described in the following part of the input. Description of one test case consists of one line containing three integers p, q and n (1 ≤ p, q, n ≤ 10<sup>9</sup>).</p>

### 출력 

 <p>Output should include exactly t lines containing answers to the subsequent test cases from input. The answer should be one letter <code>E</code> (if Euclid could bring about his victory, regardless of the Pythagoras' movements), <code>P</code> (if Pythagoras could bring about his victory, regardless of Euclid's moves) or <code>R</code> (for <i>remis</i>, i.e. <i>draw</i> in Polish, if the game will be played infinitely).</p>

