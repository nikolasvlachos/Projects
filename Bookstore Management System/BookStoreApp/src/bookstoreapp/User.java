package bookstoreapp;

import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

// The User class is abstract, meaning it cannot be instantiated directly.
// Other classes, like Owner or Customer, will extend this class.
public abstract class User {
    // username and password are properties of a User, stored as StringProperties
    protected final StringProperty username;
    protected final StringProperty password;
 
    // Constructor to initialize username and password when creating a User   
    public User(String username, String password) {
        this.username = new SimpleStringProperty(username);// Set username using SimpleStringProperty
        this.password = new SimpleStringProperty(password);// Set password using SimpleStringProperty
    }
    // Getter method for username, returns the username property
    // Getter method for password, returns the password property
    public String getUsername() { return username.get(); }
    public String getPassword() { return password.get(); }

    // Property methods allow other classes to listen for changes to username and password   
    public StringProperty usernameProperty() { return username; }
    public StringProperty passwordProperty() { return password; }
}