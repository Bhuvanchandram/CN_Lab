import java.net.*;
import java.io.*;

public class TCP_Server{
    public static void main(String[] args) {
        ServerSocket sersock= new ServerSocket(4000);
        System.out.println("Server connected, waiting for client");
        Socket sock=sersock.accept();
        System.out.println("Connection accepted, waiting for chatting");
        BufferedReader namReader=new BufferedReader(new InputStreamReader(sock.getInputStream()));
        String fname=nameRead.readLine();
        PrintWriter pwrite=new PrintWriter(sock.getOutputStream(),true);
        try{
            BufferedReader contentRead=new BufferedReader(new FileReader(fname));
            String str;
            while()
        }
        catch{

        }
        finally{

        }
    }   
}