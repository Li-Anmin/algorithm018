public class isAnagram {
    public static void main(String[] args) {
        boolean result = false;
        result = isAnagram("rat","cat");
        System.out.println(result);

    }

    public static boolean isAnagram(String s,String t) {
        if (s.length() != t.length()) {
            return  false;
        }
        int[] alpha = new int[26];
        for (int i = 0; i < s.length(); i++) {
            alpha[s.charAt(i) - 'a']++;
            alpha[t.charAt(i) - 'a']--;
        }
        for (int i=0; i < s.length(); i++) {
            if (alpha[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
