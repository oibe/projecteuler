import java.math.BigInteger;


public class p55 {
	public static boolean palindrome(String input){
		
		for(int i = 0; i < input.length()/2;i++){
			if(input.charAt(i)!= input.charAt(input.length()-(1+i))){
				return false;
			}
		}
		return true;
	}
	public static String reverse(String input){
		String result = "";
		for(int i = input.length()-1;i >= 0;i--){
			result+=input.charAt(i);
		}
		return result;
	}
	public static boolean problem(String input, int count){
		if(palindrome(input)== true && count != 0){
			//System.out.println(count);
			return true;
		}
		if(count == 50){
			return false;
		}
		BigInteger first = new BigInteger(input);
		BigInteger second = new BigInteger(reverse(input));
		
		BigInteger third = first.add(second);
		//System.out.println(first+":"+second+":"+third);
		return problem(third.toString(),count+1);
	}
	public static void main(String[] args){
		int counter= 0;
		for(int i = 0; i < 10000;i++){
			///System.out.println(i);
			if( problem(i+"",0)== false){
				counter++;
				
			}
		}
		System.out.println(counter);
		
	}
}
