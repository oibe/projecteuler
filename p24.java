import java.util.LinkedList;


public class p24 {
	static int count= 0;
    public static void permute(int[] list,boolean[] check,int index){
        if(index == check.length){
        	
        	
            for(int i = 0;i < check.length;i++){
                System.out.print(list[i]);
            }
            	System.out.println();
        		
        		
       
            return;
        }
        int choice = 0;
        for(int i = 0; i < check.length;i++){
            if(check[i] == true){
                choice= i;
                //check[i]= false;
                break;
            }
        }
       
        switch(choice){
            case 0:
                if(check[0]!=false){
                    check[0] = false;
                    list[index]= 0;
                    permute(list,check,index+1);
                    check[0] = true;
                }
            case 1:
                if(check[1]!=false){
                    check[1] = false;
                    list[index]= 1;
                    permute(list,check,index+1);
                    check[1] = true;
                }
            case 2:
                if(check[2] != false){
                    check[2] = false;
                    list[index]= 2;
                    permute(list,check,index+1);
                    check[2]= true;
                }
            case 3:
                if(check[3] != false){
                    check[3] = false;
                    list[index]= 3;
                    permute(list,check,index+1);
                    check[3]= true;
                }
            case 4:
                if(check[4] != false){
                    check[4] = false;
                    list[index]= 4;
                    permute(list,check,index+1);
                    check[4]= true;
                }
            case 5:
                if(check[5] != false){
                    check[5] = false;
                    list[index]= 5;
                    permute(list,check,index+1);
                    check[5]= true;
                }
            case 6:
                if(check[6] != false){
                    check[6] = false;
                    list[index]= 6;
                    permute(list,check,index+1);
                    check[6]= true;
                }
            case 7:
                if(check[7] != false){
                    check[7] = false;
                    list[index]= 7;
                    permute(list,check,index+1);
                    check[7]= true;
                }
            case 8:
                if(check[8] != false){
                    check[8] = false;
                    list[index]= 8;
                    permute(list,check,index+1);
                    check[8]= true;
                }
            case 9:
                if(check[9] != false){
                    check[9] = false;
                    list[index]= 9;
                    permute(list,check,index+1);
                    check[9]= true;
                }
        }
        return;
    }
    public static void main(String[] args){
        int[] list = new int[10];
        boolean[] check = {true,true,true, 
true,true,true,true,true,true,true};
        System.out.println("Starting...");
        permute(list,check,0);
        System.out.println("Finished");
    }
}
