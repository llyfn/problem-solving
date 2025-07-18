# [Gold I] 본대 산책 3 - 14289 

[문제 링크](https://www.acmicpc.net/problem/14289) 

### 성능 요약

메모리: 26196 KB, 시간: 304 ms

### 분류

수학, 그래프 이론, 분할 정복을 이용한 거듭제곱

### 제출 일자

2025년 7월 8일 07:00:20

### 문제 설명

<p>숭실 대학교 정보 과학관은 유배를 당해서 캠퍼스의 길 건너편에 있다. 그래서 컴퓨터 학부 학생들은 캠퍼스를 ‘본대’ 라고 부르고 정보 과학관을 ‘정보대’ 라고 부른다. 준영이 또한 컴퓨터 학부 소속 학생이라서 정보 과학관에 박혀있으며 항상 꽃 이 활짝 핀 본 대를 선망한다. 어느 날 준영이는 본 대를 산책하기로 결심하였다.</p>

<p>숭실대학교 캠퍼스 지도는 n개의 건물이 있고, 인접한 두 건물을 뜻하는 도로 m개가 있다.</p>

<p>한 건물에서 바로 인접한 다른 건물로 이동 하는 데 1분이 걸린다. 준영이는 산책 도중에 한번도 길이나 건물에 멈춰서 머무르지 않는다. 준영이는 할 일이 많아서 딱 D분만 산책을 할 것이다. 산책을 시작 한 지 D분 일 때, 정보 과학관에 도착해야 한다. 이때 가능한 경로의 경우의 수를 구해주자.</p>

### 입력 

 <p>첫째 줄에는 건물의 수 n개,도로의 수 m개가 주어진다.(1 ≤ n ≤ 50, 0 ≤ m ≤ 1000)</p>

<p>다음 m줄에는 두 건물을 잇는 간선 a, b가 주어진다.(1 ≤ a, b ≤ n, a ≠ b) 특정 두 건물을 잇는 간선이 여러 번 나오지 않는다.</p>

<p>다음 줄에는 산책할 시간인 D분이 주어진다. 1번 정점이 정보대이며, 준영이는 0분에 정보대에 위치할 것이다.(1 ≤ D ≤ 1,000,000,000)</p>

### 출력 

 <p>가능한 경로의 수를 1,000,000,007로 나눈 나머지를 출력한다.</p>

