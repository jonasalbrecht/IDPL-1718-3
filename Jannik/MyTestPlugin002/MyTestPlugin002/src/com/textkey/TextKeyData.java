package com.textkey;

public class TextKeyData {

    public String getCode() {
        return code;
    }

    private String code;

    public String getText() {
        return text;
    }

    private String text;

    private TextKeyData(){}
    public TextKeyData(String code, String text)
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
