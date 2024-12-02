import java.util.HashMap;

public class Main {

    public static int romanTointeger(String s) {
        HashMap<Character, Integer> dictionnary = new HashMap<>(){
                { put('I', 1); }
                { put('V', 5); }
                { put('X', 10); }
                { put('L', 50); }
                { put('C', 100); }
                { put('D', 500); }
                { put('M', 1000); }
        };

        int value = 0;

        int i = 0;
        while( i < s.length() ) {

            Character letter = s.charAt(i);

            int currentVal = dictionnary.get(letter);

            if (i + 1 < s.length() && dictionnary.get(s.charAt(i + 1)) > currentVal) {
                currentVal = dictionnary.get(s.charAt(i + 1)) - currentVal;
                i++;
            }
            value += currentVal;

            i++;

        }

        return value;

    }

    public static void main(String[] args) {

        System.out.println(romanTointeger("III"));

        System.out.println(romanTointeger("LVIII"));

        System.out.println(romanTointeger("MCMXCIV"));
        
    }
}