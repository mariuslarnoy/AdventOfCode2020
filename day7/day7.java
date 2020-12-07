import java.util.Scanner;
import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.Set;

public class day7 {

    private static ArrayList<String> readFile() {

        ArrayList<String> input = new ArrayList<>();
        try {
            final File file = new File("day7/inputDay7.txt");
            final Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                input.add(scanner.nextLine());
            }
            scanner.close();
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        
        return input;
    
    }

    private static Hashtable<String, ArrayList<String>> processFile(final ArrayList<String> input) {
        
        Hashtable<String, ArrayList<String>> table = new Hashtable();
        
        for (final String line : input) {

            //remove "." from each line
            final String lineNoDot = line.substring(0, line.length()-1);

            final String[] elements = lineNoDot.split(",");
            
            final String currentBag = elements[0].split(" ")[0] + " " +  
                elements[0].split(" ")[1];

            //either one or zero children
            if (elements.length == 1) {

                //one child
                if (containsInt(elements[0])) {
                    
                    final String[] tempList = elements[0].split(" ");
                    final String childName = tempList[tempList.length - 3] + " " +  tempList[tempList.length - 2];
                    ArrayList<String> child = new ArrayList<>();
                    
                    child.add(childName);

                    table.put(currentBag, child);

                }
                //no children
                else 
                    table.put(currentBag, new ArrayList<>());
            }
            // >1 child
            else {
                ArrayList<String> children = new ArrayList<String>();
                
                for (String ele : elements) {
                    String[] words = ele.split(" ");
                    String color = words[words.length-3] + " " + words[words.length-2];
                    children.add(color);
                }
                table.put(currentBag, children);
            }

            

        }

        return table;
    }    

    private static boolean containsInt(final String string) {

        for (int i = 0; i < string.length(); i++) {
            if (Character.isDigit(string.charAt(i)))
                return true;
        }
        return false;
    }

    private static int searchTable(final Hashtable<String, ArrayList<String>> table, String myBag) {

        Iterator<String> keyIter = table.keys().asIterator();
        
        int counter = 0;
        while (keyIter.hasNext()) {

            if(searchTable(counter, myBag, keyIter.next(), table))
                counter++;
        }

        return counter;
    }

    private static boolean searchTable(int counter, final String myBag, 
            final String currentBag, 
            final Hashtable<String, ArrayList<String>> table) {
        
        int currCounter = counter;
        
        if (!table.get(currentBag).isEmpty()) {

            if (table.get(currentBag).contains(myBag))
                return true;

            for (String color : table.get(currentBag)) {

                if (searchTable(currCounter, myBag, color, table))
                    return true;
                
            }
        }
        return false;

    }


    private static ArrayList<String> readFile_p2() {

        ArrayList<String> input = new ArrayList<>();
        try {
            final File file = new File("day7/inputDay7.txt");
            final Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                input.add(scanner.nextLine());
            }
            scanner.close();
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        
        return input;
    
    }

    private static Hashtable<String, Hashtable<String, Integer>> processFile_p2(final ArrayList<String> input) {
        
        Hashtable<String, Hashtable<String, Integer>> table = new Hashtable();
        
        for (final String line : input) {

            //remove "." from each line
            final String lineNoDot = line.substring(0, line.length()-1);

            final String[] elements = lineNoDot.split(",");
            
            final String currentBag = elements[0].split(" ")[0] + " " +  
                elements[0].split(" ")[1];

            //either one or zero children
            if (elements.length == 1) {

                //one child
                if (containsInt(elements[0])) {
                    
                    final String[] tempList = elements[0].split(" ");
                    final String childName = tempList[tempList.length - 3] + " " +  
                                             tempList[tempList.length - 2];

                    Hashtable<String, Integer> child = new Hashtable<>();
                    
                    child.put(childName, Integer.parseInt(tempList[tempList.length - 4]));

                    table.put(currentBag, child);

                }
                //no children
                else 
                    table.put(currentBag, new Hashtable<>());
            }
            // >1 child
            else {
                Hashtable<String, Integer> children = new Hashtable<>();
                
                for (String ele : elements) {
                    String[] words = ele.split(" ");
                    String color =  words[words.length-3] + " " + words[words.length-2];
                    children.put(color, Integer.parseInt(words[words.length-4]));
                }
                table.put(currentBag, children);
            }

            

        }

        return table;
    }

    private static int searchTable_p2(final Hashtable<String, Hashtable<String, Integer>> table,
        final String bagName) {
        
        Hashtable<String, Integer> currentBag = table.get(bagName);

        if (!currentBag.elements().hasMoreElements())
            return 0;
            
        Iterator<String> bagIter = currentBag.keys().asIterator();

        int currCounter = 0;
        while (bagIter.hasNext()) {
            String bagType = bagIter.next();
            currCounter += currentBag.get(bagType) + (currentBag.get(bagType) * searchTable_p2(table, bagType));

        }

        
        return currCounter;
    }
    public static void main(String[] args) {
        
        final String myBag = "shiny gold";

        //preprocessing
        final ArrayList<String> input = readFile();
        Hashtable<String, ArrayList<String>> table = processFile(input);
        //Part 1, how many different bags can hold a 'shiny gold'
        int count = searchTable(table, myBag);
        System.out.println("Part 1: " + count);

        //Part 2, how many bags does a 'shiny gold' contain
        //preprocessing, too lazy to make first implementation work on both
        final ArrayList<String> input2 = readFile_p2();
        Hashtable<String, Hashtable<String,Integer>> table2 = processFile_p2(input2);

        System.out.println("Part 2: " + searchTable_p2(table2, myBag));
    }



}