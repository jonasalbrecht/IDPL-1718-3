package myPlugin;

import com.wcohen.ss.*;
import com.wcohen.ss.Jaccard;

import java.util.ArrayList;


public class Eval {

    static ArrayList<String[]> ct = new ArrayList<>();
    public static ArrayList<String[]> topFive = new ArrayList<>();


    public static void getTopFive(ArrayList<String[]> arrlist) {
        String[] highest;
        highest = arrlist.get(0);

        int index=0;

        for(int i=0; i<3; i++)
        {
            for (String[] s : arrlist) {
                if (Double.valueOf(s[2]) > Double.valueOf(highest[2])) {
                    highest = s;
                    index = arrlist.indexOf(s);
                }
            }
            topFive.add(highest);
            arrlist.remove(index);
            highest = arrlist.get(0);
            index = 0;
        }
    }


// feedback -> question asked & chosen codesnippet

    public static void main(String[] args) {
        // some setup
        ct.add(new String[]{"matrix.I", "Returns the (multiplicative) inverse of invertible self."});
        ct.add(new String[]{"matrix.A","Return self as an ndarray object."});
        ct.add(new String[]{"matrix","Returns a matrix from an array-like object, or from a string of data."});
        ct.add(new String[]{"asmatrix(data[, dtype])","Interpret the input as a matrix."});
        ct.add(new String[]{"bmat(obj[, ldict, gdict])","Build a matrix object from a string, nested sequence, or array."});
        ct.add(new String[]{"memmap","Create a memory-map to an array stored in a binary file on disk."});
        ct.add(new String[]{"memmap.flush()","Write any changes in the array to the file on disk."});
        ct.add(new String[]{"chararray","Provides a convenient view on arrays of string and unicode values."});
        ct.add(new String[]{"core.defchararray.array(obj[, itemsize, ...])","Create a chararray"});
        ct.add(new String[]{"recarray","Construct an ndarray that allows field access using attributes."});

        String evalString = "input as matrix";


        // consists of code, textkey, score (textkey<>evalString);
        ArrayList<String[]> ctsList = new ArrayList<>();


        // evaluate algorithms

        // Levenstein
        Levenstein LV = new Levenstein();
        System.out.println("Evaluate: Levenstein");
        for(String[] c: ct) {
            System.out.println(c[1] + " ----COMPARED TO----- " + evalString + ". Score: " + LV.score(c[1],evalString));
        }
        System.out.println("Evaulation end.");

        // Jaro
        Jaro J = new Jaro();
        System.out.println("Evaluate: Jaro");
        for(String[] c: ct) {
            System.out.println(c[1] + " ----COMPARED TO----- " + evalString + ". Score: " + J.score(c[1],evalString));
        }
        System.out.println("Evaulation end.");

        // Jaccard
        Jaccard JAC = new Jaccard();
        System.out.println("Evaluate: Jaccard");
        for(String[] c: ct) {
            System.out.println(c[1] + " ----COMPARED TO----- " + evalString + ". Score: " + JAC.score(c[1],evalString));
        }
        System.out.println("Evaulation end.");

        // MongeElkan
        MongeElkan ME = new MongeElkan();
        System.out.println("Evaluate: MongeElkan");
        for(String[] c: ct) {
            System.out.println(c[1] + " ----COMPARED TO----- " + evalString + ". Score: " + ME.score(c[1],evalString));
        }
        System.out.println("Evaulation end.");


        // Smith-Waterman (seems to be the best one)
        SmithWaterman SM = new SmithWaterman();
        System.out.println("Evaluate: Smith-Waterman");
        for(String[] c: ct) {
            System.out.println(c[1] + " ----COMPARED TO----- " + evalString + ". Score: " + SM.score(c[1],evalString));
            ctsList.add(new String[]{c[0], c[1], String.valueOf(SM.score(c[1], evalString))});
        }
        System.out.println("Evaulation end.");

        getTopFive(ctsList);

        for (String[] s: topFive) {
            System.out.println(s[2]);
        }
    }
}
