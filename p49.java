public class p49
{
	private static boolean isPrime(int num)
	{
		if(num == 0 || num == 1)
		{
			return false;
		}
		if(num == 2)
		{
			return true;
		}
		for(int i = 2;i < Math.sqrt(num)+1;i++)
		{
			if(num % i == 0)
			{
				return false;
			}
		}
		return true;
	}
	public static void main(String[] args)
	{
		
		for(int i = 0; i < 100;i++)
		{
			if(isPrime(i))
			{
				System.out.print(i +", ");
			}
		}
	}
}
