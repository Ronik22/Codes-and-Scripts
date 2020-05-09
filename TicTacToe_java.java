/*  
    Tic-Tac-Toe java code for 2 by Ronik Bhattacharjee
    (WUP)
*/
import java.util.*;
import java.util.List;
import java.util.Arrays;
class tictactoe
{
    static ArrayList<Integer> player1=new ArrayList<Integer>();
    static ArrayList<Integer> player2=new ArrayList<Integer>();
    
    public static void main(String args[])
    {
        char [][] board= {{' ','|',' ','|',' '},
                          {'-','+','-','+','-'},
                          {' ','|',' ','|',' '},
                          {'-','+','-','+','-'},
                          {' ','|',' ','|',' '}};
        System.out.println("\n-----Welcome to Tic tac toe (RB)-----");
        gameboard(board);

        while(true)
        {
            int pos1=-1,pos2=-1;
            Scanner sc=new Scanner(System.in);
            System.out.println("Enter player 1 position(1-9): ");
            pos1=sc.nextInt();
            while(player1.contains(pos1)||player2.contains(pos1))
            {
                System.out.println("Position taken! Enter a correct position: ");
                pos1=sc.nextInt();
            }
            placechar(board, pos1, "player1");
            gameboard(board);
            String result = winner();
            if(result.length()>0)
            {
                System.out.println(result);
                break;
            }


            System.out.println("Enter player 2 position(1-9): ");
            pos2=sc.nextInt();
            while(player1.contains(pos2)||player2.contains(pos2))
            {
                System.out.println("Position taken! Enter a correct position: ");
                pos2=sc.nextInt();
            }
            placechar(board, pos2, "player2");
            gameboard(board);
            result = winner();
            if(result.length()>0)
            {
                System.out.println(result);
                break;
            }
        }
        
    }
    public static void gameboard(char[][]board)
    {
        System.out.println();
        
        for(char[] row: board)
        {
            for(char c: row)
            {
                System.out.print(c);
            }
            System.out.println();
        }
        System.out.println();
    }
    public static void placechar(char board[][], int pos, String user)
    {
        char pc=' ';
        if(user.equals("player1"))
           {
                pc='X';
                player1.add(pos);
           }
        else if(user.equals("player2"))
           {
                pc='O';
                player2.add(pos);
           }
        switch(pos)
        {
            case 1:
                board[0][0]=pc;
                break;
            case 2:
                board[0][2]=pc;
                break;
            case 3:
                board[0][4]=pc;
                break;
            case 4:
                board[2][0]=pc;
                break;
            case 5:
                board[2][2]=pc;
                break;
            case 6:
                board[2][4]=pc;
                break;
            case 7:
                board[4][0]=pc;
                break;
            case 8:
                board[4][2]=pc;
                break;
            case 9:
                board[4][4]=pc;
                break;
            default:
                break;
        }
    }
    public static String winner()
    {
        List toprow=Arrays.asList(1,2,3);
        List midrow=Arrays.asList(4,5,6);
        List botrow=Arrays.asList(7,8,9);
        List leftcol=Arrays.asList(1,4,7);
        List midcol=Arrays.asList(2,5,8);
        List rightcol=Arrays.asList(3,6,9);
        List diag1=Arrays.asList(1,5,9);
        List diag2=Arrays.asList(3,5,7);

        List<List> winning=new ArrayList<List>();
        winning.add(toprow);
        winning.add(midrow);
        winning.add(botrow);
        winning.add(leftcol);
        winning.add(midcol);
        winning.add(rightcol);
        winning.add(diag1);
        winning.add(diag2);

        for(List l: winning)
        {
            if(player1.containsAll(l))
            {
                return "Congratulations! Player 1 has won";
            }
            else if(player2.containsAll(l))
            {
                return "Congratulations! Player 2 has won";
            }
            else if(player1.size() + player2.size()==9)
            {
                return "It's a Draw";
            }
        }
        return "";

    }
}