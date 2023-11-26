public class Main {
    public static int reverseInteger(int num) {
        boolean negative=false;
        if (num<0) {
            negative=true;
            num=num*-1;
        }

        String strNum=String.valueOf(num);
        String reversedNum="";
        for(int i=strNum.length()-1;i>=0;i--) {
            reversedNum+=strNum.charAt(i);
        }
        int ans=Integer.valueOf(reversedNum);

        if(negative) {
            ans=ans*-1;
        }

        System.out.println(ans);
        return ans;
    }

    public static void main(String[] args) {
        int a=534;
        reverseInteger(a);

        int b=-354;
        reverseInteger(b);
    }
}