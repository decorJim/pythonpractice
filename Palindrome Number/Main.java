

public class Main {

    public static boolean palindromeNum(int num) {
        if (num<0) {
            return false;
        }

        String s=String.valueOf(num);

        int i=0;
        int j=s.length()-1;

        while(i<j) {
            if(s.charAt(i)!=s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public static void main(String[] args) {
        int num1=121;
        System.out.println(palindromeNum(num1));
        int num2=123;
        System.out.println(palindromeNum(num2));

        int num3=-121;
        System.out.println(palindromeNum(num3));
        int num4=1;
        System.out.println(palindromeNum(num4));

        /**
         *    i->   <-j
         *    1 1 2 1 1
         *
         */
    }
}