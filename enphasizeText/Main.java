import java.util.regex.Pattern;

public class Main {
    public static String emphasizeText(String text) {
        /** replace already loops through the whole string, just put what you want to replace with */
        System.out.println("original"+text);
        text=text.replace("!","!!");
        text=text.replace(".","!");
        text=text.replace("?","!");
        System.out.println("processed"+text);
        return "";
    }
    public static void main(String[] args) {
        String a="!2lkfnm lk3?poskf.";
        emphasizeText(a);
    }
}