import static java.lang.Math.*;

public class p77
{
	public static int[] getList(int num)
	{
		int[] arr = new int[num];
		for(int i = 1; i <= num; i++)
			arr[i-1] = (3*i*i-i)/2;
		return arr;
	}
	
	public static boolean isPent(int num)
	{
		double a = 3;
		double b = -1;
		double c = -2*num;
		//ax^2+by+c
		double root1 = (-b+sqrt(b*b-4*a*c))/2*a;
		System.out.println("root1 "+root1);

		double root2 = (-b-sqrt(b*b-4*a*c))/2*a;
		System.out.println("root2 "+root2);

		double root = max(root1,root2);
		if((root % 1) == 0)
		{
			System.out.println("root "+root);
			return true;
		}
		return false;
	}
	
	public static void main(String[] args)
	{
		isPent(22);
		/*int dim = 30;
		int a;
		int b;
		int[] arr = getList(dim);
		for(int i = 0; i < dim;i++)
		{
			for(int j = i; j < dim;j++)
			{
				//arr[j]-arr[i]
			}
		}*/
	}
}