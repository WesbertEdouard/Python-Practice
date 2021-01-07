class Solution {
    public int lengthOfLongestSubstring(String S) {
        int a_pointer = 0; 
        int b_pointer = 0;
        int max = 0; 

        HashSet<Character> hash_set = new HashSet(); 

        while (b_pointer < S.length()){
            if(!hash_set.contains(S.charAt(b_pointer))){
                hash_set.add(S.charAt(b_pointer));
                b_pointer++;
                max = Math.max(hash_set.size(), max);
            } else {
                hash_set.remove(S.charAt(a_pointer));
                a_pointer++;
            }
        }

        return max;
    }
}