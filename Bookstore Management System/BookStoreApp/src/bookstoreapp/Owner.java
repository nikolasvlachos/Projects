package bookstoreapp; // Package name, which is the folder location for this class

import javafx.collections.ObservableList; // Importing ObservableList, which is a list that can be observed for changes

// The Owner class extends User, meaning Owner is a type of User with extra capabilities.
// An Owner is in charge of managing books and customers.
public class Owner extends User {

    // The constructor for the Owner class, calling the constructor of the User class
    // with the default credentials "admin" for username and password.
    public Owner() {
        super("admin", "admin"); // Calling the parent class constructor to initialize username and password
    }

    // Method to add a new book to the bookstore
    public void addBook(ObservableList<Book> bookList, String name, double price) {
        // If the name is empty, throw an error
        if (name == null || name.isEmpty()) {
            throw new IllegalArgumentException("Book name cannot be empty");
        }
        // If the price is not positive, throw an error
        if (price <= 0) {
            throw new IllegalArgumentException("Price must be positive");
        }

        // Check if the book already exists in the list. If it does, throw an error.
        for (Book book : bookList) {
            if (book.getName().equalsIgnoreCase(name)) {
                throw new IllegalArgumentException("Book already exists");
            }
        }

        // If no issues, add the book to the list
        bookList.add(new Book(name, price));
    }

    // Method to delete a book from the list
    public void deleteBook(ObservableList<Book> bookList, Book book) {
        if (book == null) return; // If no book is selected, do nothing
        bookList.remove(book); // Remove the selected book from the list
    }

    // Method to add a new customer to the bookstore
    public void addCustomer(ObservableList<Customer> customerList, String username, String password) {
        if (username == null || username.isEmpty()) {
            throw new IllegalArgumentException("Username cannot be empty");
        }
        if (password == null || password.isEmpty()) {
            throw new IllegalArgumentException("Password cannot be empty");
        }

        // Check if the customer already exists
        for (Customer customer : customerList) {
            if (customer.getUsername().equalsIgnoreCase(username)) {
                throw new IllegalArgumentException("Customer already exists");
            }
        }

        // Add the new customer if no issues
        customerList.add(new Customer(username, password));
    }

    // Method to delete a customer from the list
    public void deleteCustomer(ObservableList<Customer> customerList, Customer customer) {
        if (customer == null) return; // If no customer is selected, do nothing
        customerList.remove(customer); // Remove the selected customer from the list
    }
}
