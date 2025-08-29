package bookstoreapp;

import javafx.beans.property.BooleanProperty;
import javafx.beans.property.SimpleBooleanProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.beans.property.DoubleProperty;
import javafx.beans.property.SimpleDoubleProperty;

// The Book class represents a book in the bookstore app.
public class Book {
    // The name property holds the name of the book (a String).
    private final StringProperty name;

    // The price property holds the price of the book (a double).
    private final DoubleProperty price;

    // The selected property indicates whether the book is selected (true or false).
    private final BooleanProperty selected;
    
    // Constructor to initialize a new Book object with a name and price.
    public Book(String name, double price) {
        this.name = new SimpleStringProperty(name);  // Initialize the book's name.
        this.price = new SimpleDoubleProperty(price);  // Initialize the book's price.
        this.selected = new SimpleBooleanProperty(false);  // Set the initial selected status to false (not selected).
    }
    
    // Getter method for the book's name.
    public String getName() { 
        return name.get(); 
    }

    // Getter method for the book's price.
    public double getPrice() { 
        return price.get(); 
    }

    // Getter method for the book's selected status (true or false).
    public boolean isSelected() { 
        return selected.get(); 
    }
    
    // Setter method to set the book's selected status.
    public void setSelected(boolean selected) { 
        this.selected.set(selected);  // Set the selected status (true or false).
    }
    
    // Property accessors (useful for data binding in JavaFX).
    
    // Accessor for the book's name property.
    public StringProperty nameProperty() { 
        return name; 
    }
    
    // Accessor for the book's price property.
    public DoubleProperty priceProperty() { 
        return price; 
    }
    
    // Accessor for the book's selected status property.
    public BooleanProperty selectedProperty() { 
        return selected; 
    }
}
