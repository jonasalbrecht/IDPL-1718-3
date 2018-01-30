package myPlugin;

public class DataPair {
    public DataPair(String code, String description){
        this.code = code;
        this.description = description;
    }

    private String description = "";
    private String code = "";
    private double score = 0.0;

    public String getDescription(){
        return this.description;
    }
    public void setDescription(String description){
        this.description = description;
    }

    public String getCode(){
        return this.code;
    }
    public void setCode(String code){
        this.code = code;
    }

    public double getScore(){
        return this.score;
    }
    public void setScore(double score){
        this.score = score;
    }
}
