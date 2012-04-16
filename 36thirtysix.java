public class thirtysix {
	public static Boolean palindrome(String str){
		if(str.length() <= 1){
			return true;
		}
		int low = 0;
		int high = str.length()-1;
		while(low < high){
			if(str.charAt(low)!= str.charAt(high)){
				return false;
			}
			low++;high--;
		}
		return true;
	}
	public static void main(String[] args){
		int sum = 0;
		for(int i = 0;i< 1000000;i++){
			if(palindrome(Integer.toString(i)) && palindrome(Integer.toBinaryString(i))){
				sum+=i;
			}
		}
		System.out.println("sum "+sum);
	}
}
