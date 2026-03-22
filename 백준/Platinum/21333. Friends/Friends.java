import java.util.*;

public class Test {
    static int search(ArrayList<int[]> segs, int target, int st) {
        int low = 0, high = segs.size();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (segs.get(mid)[st] >= target) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
    static ArrayList<int[]> segs = new ArrayList<>();
    static HashSet<Integer> friends = new HashSet<>();
    static long score = 0;
    public static void init(int N, int L, int[] P) {
        Arrays.sort(P);
        for (int i = 0; i < N; i++) {
            friends.add(P[i]);
        }
        int curr = P[0];
        for (int i = 1; i <= N; i++) {
            if (i == N || P[i] != P[i - 1] + 1) {
                long length = P[i - 1] - curr + 1;
                segs.add(new int[]{curr, P[i - 1]});
                score += length * length;
                if (i < N) {
                    curr = P[i];
                }
            }
        }
    }
    public static void jump(int A, int B) {
        friends.remove(A);
        int idx = search(segs, A, 1);
        long st = segs.get(idx)[0];
        long en = segs.get(idx)[1];
        score -= (en - st + 1) * (en - st + 1);
        if (st == A && en == A) {
            segs.remove(idx);
        } else if (st == A) {
            segs.get(idx)[0] = A + 1;
            long newLen = en - A;
            score += newLen * newLen;
        } else if (en == A) {
            segs.get(idx)[1] = A - 1;
            long newLen = A - st;
            score += newLen * newLen;
        } else {
            segs.get(idx)[1] = A - 1;
            long newLen1 = A - st;
            score += newLen1 * newLen1;
            int newSt = A + 1;
            int newEn = (int) en;
            long newLen2 = newEn - newSt + 1;
            score += newLen2 * newLen2;
            segs.add(idx + 1, new int[]{newSt, newEn});
        }
        friends.add(B);
        idx = search(segs, B, 0);
        if (friends.contains(B - 1) && friends.contains(B + 1)) {
            long st1 = segs.get(idx - 1)[0], en1 = segs.get(idx - 1)[1];
            long st2 = segs.get(idx)[0], en2 = segs.get(idx)[1];
            score -= (en1 - st1 + 1) * (en1 - st1 + 1);
            score -= (en2 - st2 + 1) * (en2 - st2 + 1);
            segs.get(idx - 1)[1] = (int) en2;
            score += (en2 - st1 + 1) * (en2 - st1 + 1);
            segs.remove(idx);
        } else if (friends.contains(B - 1)) {
            long st1 = segs.get(idx - 1)[0], en1 = segs.get(idx - 1)[1];
            score -= (en1 - st1 + 1) * (en1 - st1 + 1);
            segs.get(idx - 1)[1] = B;
            score += (B - st1 + 1) * (B - st1 + 1);
        } else if (friends.contains(B + 1)) {
            long st2 = segs.get(idx)[0], en2 = segs.get(idx)[1];
            score -= (en2 - st2 + 1) * (en2 - st2 + 1);
            segs.get(idx)[0] = B;
            score += (en2 - B + 1) * (en2 - B + 1);
        } else {
            score += 1;
            segs.add(idx, new int[]{B, B});
        }
    }
    public static long score() {
        return score;
    }
}
