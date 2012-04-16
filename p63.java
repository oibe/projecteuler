import java.math.BigInteger;


public class p63
{
	public static int length(double num)
	{
		int count = 0;
		while(Math.floor(num)  > 0){
			count++;
			num/=10;
		}
		return count;
	}
	public static void main(String[] args)
	{
		int count = 1;
		for(int base = 2; base < 10;base++ )
		{
			int exp = 1;
			BigInteger orig = new BigInteger(""+base);
			BigInteger num = new BigInteger(""+base);
			num.pow(exp);
			while(num.toString().length() <= exp )
			{

				if(num.toString().length() == exp)
				{
					count++;
					System.out.println(base+"^"+exp+"="+num);
				}
				exp++;
				num = new BigInteger(orig.toString());
				num.pow(exp);
			}
		}
		System.out.println("answer "+count);
	}
}
