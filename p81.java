import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import static java.lang.System.*;

public class p81
{
	
	public static int[][] parser(int dimen,String fileName)
	{
		int[][] arr = new int[dimen][dimen];
		Scanner sc = null;
		try
		{
			sc = new Scanner(new File(fileName));
		} catch (FileNotFoundException e){ e.printStackTrace(); }
		int row = 0;
		while(sc.hasNext())
		{
			String[] line = sc.nextLine().split(",");
			for(int i = 0; i < line.length;i++)
			{
				arr[row][i] = Integer.parseInt(line[i]);
			}
			row++;
		}
		return arr;
	}
	
	public static void disp(int[][] arr,int dimen)
	{
		for(int i = 0; i < dimen;i++)
		{
			for(int j = 0; j < dimen;j++)
			{
				out.print(arr[i][j]+",");
			}
			out.println();
		}
	}
	
	public static int pathHelper(int[][] arr,int x, int y, int dimen,int sum)
	{
		if(x == dimen-1 && y == dimen-1)
			return sum;
		
		boolean check1 = false;
		boolean check2 = false;
		int val1 = 0;
		int val2 = 0;
		
		if(x != dimen - 1)
		{
			val1 = pathHelper(arr,x+1,y,dimen,sum+arr[x+1][y]);
			check1 = true;
		}
			
		if(y != dimen-1)
		{
			val2 = pathHelper(arr,x,y+1,dimen,sum+arr[x][y+1]);
			check2 = true;
		}
		
		if(check1 && check2)
		{
			return Math.min(val1, val2);
		}
		if(check1)
			return val1;
		return val2;
	}
	
	public static int path(int[][] arr,int dimen)
	{
		return pathHelper(arr,0,0,dimen,arr[0][0]);
	}
	
	public static void main(String[] args)
	{
		String fileName = "C:\\Users\\Programer\\Desktop\\test.txt";
		int dimen = 80;
		int[][] arr = parser(dimen,fileName);
		out.println("answer "+path(arr,dimen));
	}
}
