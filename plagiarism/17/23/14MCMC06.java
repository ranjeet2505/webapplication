import java.util.*;
import java.lang.*;
class Point
{
int x,y;
         Point()
         {
          x=0;
          y=0;
          }

         Point(int a, int b)
             {
                 x=a;
                 y=b;
             }
}
class Quad
{
   Point P1,P2,P3,P4;
   double ab,bc,cd,de;
   
		Quad()
		{
                 Point P1=new Point();
                 Point P2=new Point();
                 Point P3=new Point();
                 Point P4=new Point();
                 ab=bc=cd=de=0.0;
                 }
     Quad (Point a,Point b ,Point c ,Point d)
	{
         P1=a;P2=b;P3=c;P4=d;
         ab=length(a,b);
	 bc=length(b,c);
	 cd=length(c,d);
	 de=length(d,a);
       }
   double length(Point a, Point b)
	{ 
		 return Math.sqrt((b.x-a.x)*(b.x-a.x)+(b.y-a.y)*(b.y-a.y));
	}	
           
 
void primeter()
{
double p=ab+bc+cd+de;
System.out.println(Math.round(p));
}


	void area()
        {
		double d1 =length(P2,P4);
                double s = (ab+de+d1)/2;
                double u_area=Math.sqrt(s*(s-ab)*(s-de)*(s-d1));
                
		 s= (bc+cd+d1)/2;
		double l_area=Math.sqrt(s*(s-bc)*(s-cd)*(s-d1));
		System.out.println(Math.round(u_area+l_area));
	}
}
class areafigure
{
public static void main(String args[])
{
	Scanner in=new Scanner(System.in);
	int x,y;
	x=in.nextInt();
	y=in.nextInt();
	Point P1=new Point(x,y);
	x=in.nextInt();
	y=in.nextInt();
	Point P2=new Point(x,y);
	x=in.nextInt();
	y=in.nextInt();
	Point P3=new Point(x,y);
	x=in.nextInt();
	y=in.nextInt();
	Point P4=new Point(x,y);
	Quad Q=new Quad(P1,P2,P3,P4);
	int ch=in.nextInt();
	Q.primeter();
	Q.area();
}
}
	


              



			





















