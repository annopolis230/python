import java.io.*;
import java.util.*;
public class DevoreZaneA3 {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        ArrayList<Employee> list =  new ArrayList<Employee>();
        try (
                ObjectInputStream serial1 = new ObjectInputStream(new FileInputStream("serialEmp1.dat"));
                ObjectInputStream serial2 = new ObjectInputStream(new FileInputStream("serialEmp2.dat"));
                ) {
            System.out.println(" ");
            System.out.println("Reading from serialEmp1.dat:");

            boolean read = true;
            while (read){
                try {
                    Employee emp = (Employee) serial1.readObject();
                    list.add(emp);
                    System.out.println(emp);
                } catch (EOFException e) {
                    read = false;
                }
            }
            System.out.println(" ");
            System.out.println("Reading from serialEmp2.dat:");
            read = true;
            while (read){
                try {
                    Employee emp1 = (Employee) serial2.readObject();
                    list.add(emp1);
                    System.out.println(emp1);
                } catch (EOFException e) {
                    read = false;
                }
            }
            Collections.sort(list);
        }
        try (
                ObjectOutputStream output = new ObjectOutputStream(new FileOutputStream("serialEmpSorted.dat"));
                ){
            System.out.println(" ");
            System.out.println("Employees in order:");
            for (Employee i:list){
                System.out.println(i);
                output.writeObject(i);
            }
        }
    }
}
