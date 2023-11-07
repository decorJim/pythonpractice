import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;


public class Main {

    public static String longuestSubstring(String s) {
        System.out.println(s);

        String longuest="";

        /** general pointer traverse all of s*/
        for(int i=0;i<s.length();i++) {

            /** s odd **/
            int j=i;
            int k=i;

            while(j>=0 && k<s.length()) {
                if(s.charAt(j)!=s.charAt(k)) {
                    break;
                }
                if(s.substring(j,k+1).length()>longuest.length()) {
                    /** k+1 index not included **/
                    longuest = s.substring(j, k + 1);
                }
                j--;
                k++;
            }

            /** s even **/
            j=i;
            k=i+1;
            while(j>=0 && k<s.length()) {
                if(s.charAt(j)!=s.charAt(k)) {
                    break;
                }
                if(s.substring(j,k+1).length()>longuest.length()){
                    /** k+1 index not included **/
                    longuest=s.substring(j, k + 1);
                }
                j--;
                k++;
            }

        }

        return longuest;
    }

    public static void main(String[] args) {
        String s="babad";
        System.out.println(longuestSubstring(s));
        s="cbbd";
        System.out.println(longuestSubstring(s));
        /**
         *<-jk->
         *  i
         *  ababa
         *  s odd -> j,k=i
         *  s even -> j,k=i,i+1
         *    jik
         *  ababa
         *  s[2:4]
         *
         */
    }
}