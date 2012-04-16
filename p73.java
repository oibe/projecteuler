import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;


class Fraction implements Comparable
{
	double numerator;
	double denominator;
	
	public Fraction(int num ,int den)
	{
		numerator = num;
		denominator = den;
	}
	
	public double GCD(double a , double b)
	{
		if(b == 0)
			return a;
		return GCD(b,a%b);
	}
	
	public Fraction reduce()
	{
		double gcd = GCD(this.numerator, this.denominator);
		this.numerator/=gcd;
		this.denominator/=gcd;
		return this;
	}
	
	public boolean equals(Object obj)
	{
		Fraction f = (Fraction)obj;
		return this.numerator == f.numerator && this.denominator == f.denominator;
	}

	public int compareTo(Object o) 
	{
		Fraction f = (Fraction)o;
		Double oVal = new Double(f.numerator/f.denominator);
		Double tVal = new Double(this.numerator/this.denominator);
		//System.out.println(f.numerator +" "+f.denominator+" "+f.numerator/f.denominator);
		return tVal.compareTo(oVal);
	}
}

public class p73 
{
	public static void main(String[] args) 
	{
		Set<Fraction> set = new HashSet<Fraction>();
		int d = 8;
		int count = 0;
		Fraction one = new Fraction(1,3);
		Fraction two = new Fraction(1,2);
		for(int i = 1;i <= d; i++)
		{
			for(int j = i+1; j <= d; j++)
			{
				Fraction f = new Fraction(i,j);
				if(f.compareTo(one)> 0 && f.compareTo(two) < 0)
				{
					set.add(f);
					count++;
				}
			}
		}

		System.out.println(set.size());

		
	}
	
}
