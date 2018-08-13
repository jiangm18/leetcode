import java.util.HashMap;

public class RomanToInt {

	public static void main(String[] args) {
		int res = romanToInt("DCXXI");
		System.out.println(res);
		
			
		}

	public static int romanToInt(String s) {
		// TODO Auto-generated method stub
		int res = 0;
        HashMap<Character,Integer> hm = new HashMap<Character,Integer>();
        hm.put('M',1000);
        hm.put('D',500);
        hm.put('C',100);
        hm.put('L',50);
        hm.put('X',10);
        hm.put('V',5);
        hm.put('I',1);
        int i = s.length()-1;
        while(i>0){
            if(hm.get(s.charAt(i))<=hm.get(s.charAt(i-1))){
                res = res + hm.get(s.charAt(i));
                i--;
            }else{
                res = res + hm.get(s.charAt(i)) - hm.get(s.charAt(i-1));
                i = i - 2;
            }
        }
        if(i==0){
            res = res + hm.get(s.charAt(i));
        }
        return res;
	}

}

