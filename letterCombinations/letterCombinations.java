import java.util.ArrayList;

public class letterCombinations{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String digits = "34";
		ArrayList<String> res = new ArrayList<String>();
		String[] dict = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
		letterCombinationsDFS(digits, dict, 0, "", res);
		System.out.println(res);
	}
	public static void letterCombinationsDFS(String digits, String[] dict, int level, String out, ArrayList<String> res){
		if (level == digits.length()){
			res.add(out);
		}else{
			String str = dict[digits.charAt(level)-'0'];
			for(int i = 0; i < str.length(); i++){
				out = out + str.charAt(i);
				letterCombinationsDFS(digits, dict, level+1, out, res);
				out = out.substring(0, out.length()-1);
			}
		}
	}

}
