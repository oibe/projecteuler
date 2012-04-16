import java.util.ArrayList;
import java.util.Collections;


public class p254
{
	public static int factorial(int num)
	{
		int sum = 1;
		for(int i = 1; i <= num;i++)
		{
			sum*=i;
		}
		return sum;
	}
	
	public static int f(int num)
	{
		int sum = 0;
		for(;num > 0; num/=10)
			sum+=factorial(num%10);
		return sum;
	}
	
	public static int sf(int num)
	{
		int val = f(num);
		int sum = 0;
		for(;val > 0; val/=10)
			sum+=(val%10);
		return sum;
	}
	
	public static int g(int i)
	{
		for(int j = 1;;j++)
		{
			if(sf(j) == i)
				return j;
		}
	}
	
	public static int sg(int num)
	{
		int val = g(num);
		int sum = 0;
		for(;val > 0; val/=10)
			sum+=(val%10);
		return sum;
	}
	
	public static String invFHelper(int sum,int[] arr,String result,int index)
	{
		if(sum < 0)
		{
			return "zzzz";
		}
		if(sum == 0)
		{
			return result;
		}
		ArrayList<String> list = new ArrayList<String>();
		
		for(int i = index; i < arr.length;i++)
		{
			list.add(invFHelper(sum-factorial(arr[i]),arr,result+arr[i],index+1));
		}
		Collections.sort(list);
		return list.get(0);
	}
	
	public static String invF(int sum,int[] arr)
	{
		return invFHelper(sum,arr,"",0);
	}
	
	public static ArrayList<String> invSFHelper(int sum,int val,String result,int index,ArrayList<String> list)
	{
		if(sum < 0)
		{
			return list;
		}
		if(sum == 0)
		{
			list.add(result);
			return list;
		}
		
		for(int i = 1; i < val;i++)
		{
			invSFHelper(sum-i,val,result+i,index+1,list);
		}
		return list;
	}
	
	public static ArrayList<String> invSF(int sum)
	{
		ArrayList<String> list = new ArrayList<String>();
		return invSFHelper(sum,sum,"",1,list);
	}
	
	public static void main(String[] args)
	{
		/*int sum = 0;
		for(int i = 1; i <= 150;i++)
		{
			sum+=sg(i);
		}
		System.out.println(sum);*/
		int[] a = {1,2,3,4,5,6,7,8,9,10,11,12};
		System.out.println(invSF(32));
	}

}
