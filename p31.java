public class p31 {
   
    static int count = 0;
    static int highest = 200;
    public static void combo(int[] coins,int index,int total,String 
answer){
        if(total == highest){
            //System.out.println(answer);
            count++;
            return;
        }
        if(total > highest){
            return;
        }
       
        while(true){
            combo(coins,index,total+coins[index],answer+coins[index]+",");
            index++;
            if(index == coins.length){
                break;
            }
        }
    }
   
    public static void main(String[] args) {
        int[] coins ={1,2,5,10,20,50,100,200};
        combo(coins,0,0,"");
        System.out.println("total count "+count);
    }

}
