import java.util.*;


public class Main {
    public static int longuestPalindrome(String s) {
        HashSet<Character> uniques=new HashSet<>();
        for(int i=0;i<s.length();i++) {
            if (uniques.contains(s.charAt(i))) {
                uniques.remove(s.charAt(i));
            }
            else {
                uniques.add(s.charAt(i));
            }
        }
        System.out.println("uniques"+uniques);
        /**
         * WE DONT CONSIDER 1 CHARACTER IN ODD SUBSTRING
         * THE EVEN PART IS ALREADY CONSIDERED
         * aaaccdddddcc  length=12
         * aa|a   (2)
         * dddd|d (4)
         * set=[a,d]     length=2
         * 2+4+4(c)=10
         * we can only have one more number after the total even number
         * 10+1=11 -> can be found by s.length-set.length+1=12-2+1=11
         */

        return s.length()-uniques.size()+1;
    }

    public static void main(String[] args) {
       String s="abccccdd";
       System.out.println(longuestPalindrome(s));
       s="aaaccdddddcc";
       System.out.println(longuestPalindrome(s));
    }
}