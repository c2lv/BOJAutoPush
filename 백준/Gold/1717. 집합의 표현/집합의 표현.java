import java.util.Scanner;

public class Main {
    public static int[] a;
	
    public static int find(int x) {
        if(x == a[x])
            return x;
        else 
            return a[x] = find(a[x]);
    }
    public static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if(x != y) {
            a[y] = x;
        }
    }
    public static void b(int x, int y) {
        x = find(x);
        y = find(y);
        if(x == y) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        a = new int[n+1];
        for(int i = 0; i <= n; i++) {
            a[i] = i;
        }
        for(int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int x = sc.nextInt();
            int y = sc.nextInt();
            if(a == 0) {
                union(x,y);
            } else {
                b(x, y);
            }
        }
    }
}