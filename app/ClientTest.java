import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;


public class ClientTest {
	
	Socket socket;
	PrintWriter out;
	BufferedReader in;

	public void listenSocket(){
		//Create socket connection
		try{
			socket = new Socket( "129.215.164.16", 5555 ); //("172.20.9.71", 4444);
			out = new PrintWriter(socket.getOutputStream(), 
					true);
			in = new BufferedReader(new InputStreamReader(
					socket.getInputStream()));
		} catch (UnknownHostException e) {
			System.out.println("Unknown host: 129.215.164.16");
			System.exit(1);
		} catch  (IOException e) {
			e.printStackTrace();
			System.out.println("No I/O");
			System.exit(1);
		}
	}

	public void runMe(){
		String text = "@Edinburgh_CC The recycling bins at Hopetoun Cres are outrageous. Need to be emptied http://t.co/gESk1tGGD1";
		out.println( text );
		
		//Receive text from server
		try{
			String line = in.readLine();
			System.out.println("Text received: " + line);
			socket.close();
		} catch (IOException e){
			System.out.println("Read failed");
			System.exit(1);
		}
	} 
	
	
	public static void main(String [] args) {
		ClientTest client = new ClientTest();
		client.listenSocket();
		client.runMe();
	}
	
	
}
