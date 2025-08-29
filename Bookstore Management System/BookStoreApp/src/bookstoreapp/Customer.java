package bookstoreapp;

import javafx.beans.property.IntegerProperty;
import javafx.beans.property.SimpleIntegerProperty;
import java.util.List;

// The Customer class represents a customer in the bookstore app. 
// It extends the User class and adds functionality for points and customer state.
public class Customer extends User {
    // The points property holds the customer's points (earned through purchases)
    private final IntegerProperty points;

    // The state property represents the customer's status (Silver/Gold)
    private CustomerState state;

    // Constructor to initialize a new Customer object with a username and password
    public Customer(String username, String password) {
        super(username, password);  // Call the constructor of the parent class (User)
        this.points = new SimpleIntegerProperty(0);  // Start with 0 points
        this.state = new SilverState();  // Set the initial state to Silver
    }

    // Getter for points
    public int getPoints() { 
        return points.get(); 
    }

    // Getter for the customer's status (Silver/Gold)
    public String getStatus() { 
        return state.getStatus(); 
    }

    // Setter for points (also updates the customer state based on points)
    public void setPoints(int points) { 
        this.points.set(points);  // Set the points value
        updateState();  // Update the customer's state (Silver/Gold) based on the new points
    }

    // Getter for the IntegerProperty of points (used for bindings in JavaFX)
    public IntegerProperty pointsProperty() { 
        return points; 
    }

    // Method to simulate a customer buying a list of books and earning points
    public void buyBooks(List<Book> books) {
        // Calculate the total cost of the books
        double total = calculateTotalCost(books);
        // Earn points based on the total cost (10 points per dollar spent)
        int earnedPoints = (int)(total * 10);
        points.set(points.get() + earnedPoints);  // Add earned points to the total
        updateState();  // Update the state based on the new points
    }

    // Method to redeem points and buy books with a discount
    public double[] redeemPointsAndBuy(List<Book> books) {
        // Calculate the total cost of the books
        double totalCost = calculateTotalCost(books);
        // Get the current points of the customer
        int currentPoints = points.get();
        
        // Calculate how many points can be redeemed (100 points for each dollar)
        int redeemablePoints = (currentPoints / 100) * 100;  // Only redeem full 100-point increments
        double maxDiscount = redeemablePoints / 100.0;  // Calculate the discount based on redeemable points
        
        // Apply the discount, but it can't exceed the total cost
        double actualDiscount = Math.min(totalCost, maxDiscount);
        double amountToPay = totalCost - actualDiscount;  // The amount the customer actually needs to pay
        
        // Deduct the used points (points spent on the discount)
        int pointsUsed = (int)(actualDiscount * 100);
        points.set(currentPoints - pointsUsed);
        
        // Earn points based on the amount paid after applying the discount
        int pointsEarned = (int)(amountToPay * 10);
        points.set(points.get() + pointsEarned);
        
        // Update the state after the transaction
        updateState();
        
        // For debugging: Output the transaction details
        System.out.printf("[DEBUG] Total: $%.2f | Discount: $%.2f | Paid: $%.2f | Points: %d->%d%n",
                         totalCost, actualDiscount, amountToPay, currentPoints, points.get());
        
        // Return an array with the total cost, discount applied, and amount the customer paid
        return new double[]{totalCost, actualDiscount, amountToPay};
    }

    // Helper method to calculate the total cost of a list of books
    private double calculateTotalCost(List<Book> books) {
        // Sum the prices of all the books in the list
        return books.stream().mapToDouble(Book::getPrice).sum();
    }

    // Update the customer's state (Silver or Gold) based on their points
    private void updateState() {
        // If the customer has 1000 or more points, they become a Gold customer
        this.state = (points.get() >= 1000) ? new GoldState() : new SilverState();
    }
}
