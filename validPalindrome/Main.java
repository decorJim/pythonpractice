public class Main {

    public static boolean isValidPalindrome(String s) {

        String alphaNumString = "";
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                alphaNumString += s.charAt(i);
            }
        }

        alphaNumString = alphaNumString.toLowerCase();
        System.out.println(alphaNumString);

        int i = 0;
        int j = alphaNumString.length() - 1;

        while (i < j) {

            if (alphaNumString.charAt(i) != alphaNumString.charAt(j)) {
                return false;
            }

            i ++;
            j --;
        }

        return true;
    }

    public static void main(String[] args) {

        System.out.println(isValidPalindrome("A $#man- Has+ 2 Car"));
        System.out.println(isValidPalindrome(""));
        System.out.println(isValidPalindrome("a"));
        System.out.println(isValidPalindrome("A man A"));
    }
}