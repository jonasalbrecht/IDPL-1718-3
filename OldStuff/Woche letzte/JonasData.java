package com.company;

public class JonasData {

    public String getCode() {
        return code;
    }

    private String code;

    public String getText() {
        return text;
    }

    private String text;

    private JonasData(){}
    public JonasData(String code, String text)
    {
        this.code = code;
        this.text = text;
    }

    @Override
    public String toString() {
        return "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" +
                "code:\n\t" + this.code + "\n" + "text:\n\t" + this.text +
                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";
    }
}
