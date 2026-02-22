# [Gold I] Treasure Hunt - 22463 

[문제 링크](https://www.acmicpc.net/problem/22463) 

### 성능 요약

메모리: 377128 KB, 시간: 5704 ms

### 분류

이분 탐색, 값 / 좌표 압축, 누적 합

### 제출 일자

2026년 2월 18일 21:18:35

### 문제 설명

<p>
太郎君はある広場にお宝を探しにやってきました。この広場にはたくさんのお宝が埋められていますが、太郎君は最新の機械を持っているので、どこにお宝が埋まっているかをすべて知っています。広場はとても広いので太郎君は領域を決めてお宝を探すことにしましたが、お宝はたくさんあるためどのお宝がその領域の中にあるかすぐにわかりません。そこで太郎君はその領域の中にあるお宝の数を数えることにしました。

				</p>

### 입력 

 <pre><var>n</var> <var>m</var>
<var>x<sub>1</sub></var> <var>y<sub>1</sub></var>
<var>x<sub>2</sub></var> <var>y<sub>2</sub></var>
...
<var>x<sub>n</sub></var> <var>y<sub>n</sub></var>
<var>x<sub>11</sub></var> <var>y<sub>11</sub></var> <var>x<sub>12</sub></var> <var>y<sub>12</sub></var>
<var>x<sub>21</sub></var> <var>y<sub>21</sub></var> <var>x<sub>22</sub></var> <var>y<sub>22</sub></var>
...
<var>x<sub>m1</sub></var> <var>y<sub>m1</sub></var> <var>x<sub>m2</sub></var> <var>y<sub>m2</sub></var>
</pre>

<ul>
	<li><var>n</var>は広場に埋まっているお宝の数を表す</li>
	<li><var>m</var>は調べる領域の数を表す</li>
	<li>2行目から<var>n+1</var>行目はそれぞれのお宝が埋まっている座標を表す</li>
	<li><var>n+2</var>行目から<var>n+m+1</var>行目はそれぞれの調べる領域を表す</li>
	<li>x軸の正の方向が東、y軸の正の方向が北を表す</li>
	<li>それぞれの領域は長方形であり、<var>x<sub>i1</sub></var>と<var>y<sub>i1</sub></var>は長方形の南西の頂点の座標、<var>x<sub>i2</sub></var>と<var>y<sub>i2</sub></var>は長方形の北東の頂点の座標を表す</li>
</ul>

### 출력 

 <pre><var>C<sub>1</sub></var>
<var>C<sub>2</sub></var>
...
<var>C<sub>m</sub></var>
</pre>

<ul>
	<li>それぞれの領域に含まれるお宝の数を各行に出力せよ</li>
</ul>

