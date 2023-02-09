import java.util.Arrays;

class Stock implements Comparable {
    private String symbol;
    private String name;
    private double previousClosingPrice;
    private double currentPrice;
    private int changePercent;
    
    public Stock(String symbol,String name,double previousClosingPrice,double currentPrice){
        this.symbol = symbol;
        this.name = name;
        this.previousClosingPrice = previousClosingPrice;
        this.currentPrice = currentPrice;
        changePercent = (currentPrice - previousClosingPrice)/previousClosingPrice;
    }
    public String toString(){
        return "Symbol: " + this.symbol + " Name: " + this.name + " Percent Change: " + this.changePercent;
    }
    public int compareTo(Object o){
        return changePercent - ((Stock)o).changePercent;
    }
}

public class Main{
    Stock[] array = new Stock[3];
    Stock[0] = new Stock("ORCL","Oracle Corporation",34.5,34.35);
    Stock[1] = new Stock("AAPL","Apple",152.21,151.54);
    Stock[2] = new Stock("LTHM","Livent",25.01,24.53);
    Arrays.sort(array);
    for (Object o:array){
        System.out.println(o.toString());
    }
}
