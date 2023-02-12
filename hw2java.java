import java.util.*;
public class Stock implements Comparable<Stock> {
    private String symbol;
    private String name;
    private double previousClosingPrice;
    private double currentPrice;
    private double changePercent;

    public Stock(String symbol,String name,double previousClosingPrice,double currentPrice){
        this.symbol = symbol;
        this.name = name;
        this.previousClosingPrice = previousClosingPrice;
        this.currentPrice = currentPrice;
        this.changePercent = ((currentPrice - previousClosingPrice)/previousClosingPrice)*100;
    }
    @Override
    public String toString(){
        return "Symbol: " + this.symbol + " Name: " + this.name + " -- Percent Change: " + this.changePercent;
    }
    @Override
    public int compareTo(Stock o){
        if (this.changePercent > o.changePercent){
            return 1;
        } else if (this.changePercent < o.changePercent) {
            return -1;
        } else {
            return 0;
        }
    }
    public static void main(String[] args) {
        Stock[] tickers = {
                new Stock("ORCL","Oracle",34.5,34.35),
                new Stock("LTHM","Livent",24.45,25),
                new Stock("AAPL","Apple",151.23,150.43),
                new Stock("TSLA","Tesla",194.58,192.20),
                new Stock("ECL","Ecolab",146.02,145.12)
        };
        Arrays.sort(tickers);
        System.out.println("Stocks in order:");
        for (Stock stock:tickers){
            System.out.println(stock.toString());
        }
    }
}
