import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class sample {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the name of the file: ");
        String fileName = input.nextLine();

        // File to be read
        File file = new File(fileName);

        try {
            // Create a scanner to read the file
            Scanner sc = new Scanner(file);

            // Read the contents of the file line by line
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                System.out.println(line);
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + file.toString());
        }
    }
}
