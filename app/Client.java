import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
 
 
public class Client {
     
    Socket socket;
    PrintWriter out;
    BufferedReader in;

    public void listenSocket(){
	//System.setProperty("java.net.preferIPv4Stack" , "true");
        //Create socket connection
        try{
            socket = new Socket( "129.215.164.16", 7777 ); //("172.20.9.71", 4444);
            out = new PrintWriter(socket.getOutputStream(),
                    true);
            in = new BufferedReader(new InputStreamReader(
                    socket.getInputStream()));
        } catch (UnknownHostException e) {
            System.out.println("Unknown host: 129.215.5.255");
            System.exit(1);
        } catch  (IOException e) {
            e.printStackTrace();
            System.out.println("No I/O");
            System.exit(1);
        }
    }
 
    public void getSentiment( String tweet ){
//System.out.println( tweet );
        out.println( tweet );
         
        //Receive text from server
        try{
            String line = in.readLine();
            System.out.println( line );
            socket.close();
        } catch (IOException e){
            e.printStackTrace();
            System.out.println("Read failed");
            System.exit(1);
        }
    }
     
     
    public static void main(String [] args) {
        Client client = new Client();
        client.listenSocket();
        client.getSentiment( args[0] );
    }
     
     
}
