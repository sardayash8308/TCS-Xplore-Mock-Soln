import java.util.Scanner;

public class YashSoln {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Number : ");
        int a = sc.nextInt();
        int l = reverse(a);
        System.out.println("Reverse Number is : "+l);

    }
    public static int reverse(int a){
        int l = 0;
        if (a==0){return 0;}
        else if(a<0){
            a = a* -1;
            l = reverse(a) * -1;
            return l;
        }else{
            while(a!=0){
                l = l*10 + a%10;
                a /= 10;
            }
        }return l;
    }
}
