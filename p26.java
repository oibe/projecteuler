import java.util.ArrayList;


public class p26 {
	public static boolean contains(ArrayList<Integer> list, int 
start){
		if(list.isEmpty()){
			return false;
		}
		for(int i = 0;i < list.size();i++){
			if(list.get(i) == start){
				return true;
			}
		}
		return false;
	}
		public static ArrayList<Integer> problem(float div){
		
		ArrayList<Integer> list = new ArrayList<Integer>();
		ArrayList<Integer> start_list = new ArrayList<Integer>();
		float start = 1;
		float value = 0;
		float temp = 0;
		while(start != 0){
			if(start/div > 1){
				value = div*(float)Math.floor(start/div);
			}else{
				start*=10;
				temp = (float)Math.floor(start/div);
				value = div*temp;
			}
			if(contains(start_list,(int)start)){
				return list;
			}
			start_list.add(new Integer((int)start));
			start-=value;
			list.add(new Integer((int)temp));
		}
		return list;
	}
	public static void main(String[] args) {
		int temp = 0;
		int current = 0;
		int number = 0;
		for(int i = 1; i < 1000;i++){
			temp = problem(i).size();
			if(temp > current){
				current = temp;
				number = i;
			}
		}
		System.out.println(number);
	}
}

