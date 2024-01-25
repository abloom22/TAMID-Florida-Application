public class Debug {
    public static void main(String args[]){
        final int DAYS = 30;    //initialize vars
        double money = 0.01;
        int day = 1;
        while(day < DAYS){
            money = 2 * money;  //double money var
            System.out.println("After day " + day +" you have " + money);
            day++; //increment days
        }
    }
}