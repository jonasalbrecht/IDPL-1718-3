package com.textkey;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class JsonArray {

    public static TextKeyData[] getJsonArray(String[] args) {
        System.out.println(System.getProperty("user.dir"));

        File file = new File(System.getProperty("user.dir") + "\\Data\\data_arrays_classes.json");
        String s = getFile(file);

        JSONParser parser = new JSONParser();

        TextKeyData[] dataarray = null;
        try{
            Object obj = parser.parse(s);
            JSONArray array = (JSONArray)obj;
            dataarray = new TextKeyData[array.size()];


            for ( int i = 0; i < array.size() ; i++)
            {
                JSONObject jobj = (JSONObject)array.get(i);
                dataarray[i] = new TextKeyData(jobj.get("code").toString(), jobj.get("text").toString());
                System.out.println((dataarray[i].toString()));
            }



        }catch(ParseException pe){

            System.out.println("position: " + pe.getPosition());
            System.out.println(pe);
        }

        return dataarray;
    }

    static private String getFile(File file) {

        StringBuilder result = new StringBuilder("");

        try (Scanner scanner = new Scanner(file)) {

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                result.append(line).append("\n");
            }

            scanner.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

        return result.toString();
    }
}
