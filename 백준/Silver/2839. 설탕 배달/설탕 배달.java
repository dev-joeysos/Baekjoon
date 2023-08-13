import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		//설탕 Nkg 입력
		int N, sum = 0;
		N = scan.nextInt();
		
		for(int x = 0; x <= N/5; x++) {
			for(int y = 0; y <= N/3; y++) {
				//비교를 위해 처음 0일때만
				if(sum == 0) {
					if(5*x + 3*y == N) 
						sum = x + y;
				}
				else {
					if(5*x + 3*y == N) {
						if(x + y < sum)
							sum = x + y;
					}
				}
			}
		}
		//다 돌려봤는데도 sum이 0 그대로다 = 정확한 N으로 떨어지게 봉지를 못나눈다		
		if(sum == 0)
			System.out.println(-1);
		else System.out.println(sum);
	}
}