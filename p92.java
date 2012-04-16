
public class p92
{
	public static int transform(int num)
	{
		int sum = 0;
		for(; num > 0; num/=10)
		{
			sum+=(int)Math.pow((num % 10),2);
		}
		return sum;
	}
	
	public static boolean algo(int num,BitSet b89, BitSet b1)
	{
		if(b89.checkBit(num-1) || num == 89)
		{
			b89.setBit(num-1);
			return true;
		}
		if(b1.checkBit(num-1)|| num == 1)
		{
			b1.setBit(num-1);
			return false;
		}
		while(num != 1 && num != 89)
		{
			num = transform(num);
			if(b89.checkBit(num-1) || num == 89)
			{
				b89.setBit(num-1);
				return true;
			}
			if(b1.checkBit(num-1)|| num == 1)
			{
				b1.setBit(num-1);
				return false;
			}
		}
		return false;
	}
	
	public static void main(String[] args)
	{
		int num = 10000000;
		BitSet b89 = new BitSet(num);
		BitSet b1 = new BitSet(num);
		int count = 0;
		for(int i = 1; i < num;i++)
		{
			if(algo(i,b89,b1))
				count++;
			if((i % (num/100)) == 0)
			{
				System.out.println((i/100)+"%");
			}
		}
		System.out.println("answer "+count);
	}
}

class BitSet
{
	private byte[] arr;
	public BitSet(int num)
	{
		arr = new byte[(int)Math.ceil(((double)num)/8.0)];
	}
	
	public void setBit(int num)
	{
		//0 indexed
		arr[num/8] = (byte)(arr[num/8]|0x1 << (7 - (num%8)));
	}
	
	public boolean checkBit(int num)
	{
		return ((arr[num/8] >> (7 - (num%8))) & 0x1) == 1;
	}
	
	public String toString()
	{
		String result = "";
		for(int i = arr.length-1; i >= 0; i--)
		{
			int b = arr[i];
			for(int j = 8; j > 0; j--)
			{
				if((b % 2) == 0)
				{
					result = "0"+result;
				}
				else
				{
					result = "1"+result;
				}
				b = b >> 1;
			}
			result = "|"+result;
		}
		return result.substring(1);
	}
	
}
