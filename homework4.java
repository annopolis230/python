import java.util.*;
public class DeVoreZane_Powers {
    private static int multiplications;
    public static double power1(double b, int n){
        double total = b;
        for (int i=1; i < n;i++){
            total*=b;
            multiplications++;
        }
        return total;
    }
    public static double power2(double b, int n){
        if (n==0) return 1;
        else
            multiplications++;
            return b*power2(b,n-1);
    }
    public static double power3(double b, int n){
        double k;
        if (n==0){
            return 1;
        } else if (n%2==0){
            k = power3(b,n/2);
            multiplications++;
            return k*k;
        } else {
            k = power3(b,n/2);
            multiplications++;
            return (k*k)*b;
        }
    }
    private static double multiPow(double b, int n, double a){
        double b2 = b*b;
        if (n==0){
            return a;
        } else if (n%2==0){
            multiplications++;
            return multiPow(b2,n/2,a);
        } else {
            multiplications++;
            return (a*b)*multiPow(b2,n/2,a);
        }
    }
    public static double power4(double b, int n){
        return multiPow(b,n,1);
    }
    public static double power5(double b, int n){
        double a = 1;
        if (n==0) {
            return a;
        }
        while (n>0){
            if (n%2==1){
                a*=b;
            }
            multiplications++;
            b*=b;
            n/=2;
        }
        return a;
    }
    public static void main(String[] args){
        double b = 0;
        int n = 0;
        boolean continueInput = true;
        Scanner input = new Scanner(System.in);
        do {
            try {
                System.out.print("Enter value for b: ");
                b = input.nextDouble();
                continueInput = false;
            } catch (InputMismatchException e) {
                System.out.println("b must be a double, try again");
                input.nextLine();
            }
        } while(continueInput);
        continueInput = true;
        do {
            try {
                System.out.print("Enter a value for n: ");
                n = input.nextInt();
                continueInput = false;
            } catch (InputMismatchException e) {
                System.out.println("n must be an integer, try again");
                input.nextLine();
            }
        } while(continueInput);
        System.out.println("Math.pow says: "+Math.pow(b,n));
        multiplications = 0;
        System.out.println("power1("+n+","+b+") = "+power1(b,n));
        System.out.println("Multiplications = "+multiplications);
        multiplications = 0;
        System.out.println("power2("+n+","+b+") = "+power2(b,n));
        System.out.println("Multiplications = "+multiplications);
        multiplications = 0;
        System.out.println("power3("+n+","+b+") = "+power3(b,n));
        System.out.println("Multiplications = "+multiplications);
        multiplications = 0;
        System.out.println("power4("+n+","+b+") = "+power4(b,n));
        System.out.println("Multiplications = "+multiplications);
        multiplications = 0;
        System.out.println("power5("+n+","+b+") = "+power5(b,n));
        System.out.println("Multiplications = "+multiplications);
    }
}
