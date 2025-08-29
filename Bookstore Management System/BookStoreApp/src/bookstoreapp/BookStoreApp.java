package bookstoreapp;

// Import necessary Java and JavaFX libraries
import java.util.stream.Collectors;
import javafx.geometry.Pos;
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.CheckBoxTableCell;
import javafx.scene.layout.*;
import javafx.geometry.*;
import javafx.collections.*;
import javafx.scene.text.*;
import java.util.*;
import java.io.*;

// Suppress unchecked warnings for JavaFX TableView operations
@SuppressWarnings("unchecked")
public class BookStoreApp extends Application {
    // Main application window
    private Stage primaryStage;
    
    // Different scenes/screens for the application
    private Scene loginScene;           // Login screen
    private Scene ownerStartScene;      // Owner's main menu
    private Scene ownerBooksScene;      // Owner's book management
    private Scene ownerCustomersScene;  // Owner's customer management
    private Scene customerStartScene;   // Customer's main screen
    private Scene customerCostScene;    // Customer's purchase summary
    
    // Data structures to hold application data
    private ObservableList<Book> bookList = FXCollections.observableArrayList();      // List of books
    private ObservableList<Customer> customerList = FXCollections.observableArrayList(); // List of customers
    private Owner owner = new Owner();  // The store owner (single admin)
    private Customer currentCustomer;    // Currently logged-in customer

    // Main method - entry point for JavaFX applications
    public static void main(String[] args) {
        launch(args);  // Launch the JavaFX application
    }
    
    // Main initialization method for JavaFX
    @Override
    public void start(Stage primaryStage) {
        this.primaryStage = primaryStage;  // Store the main window reference
        primaryStage.setTitle("Bookstore App");  // Set window title
        
        // Initialize application components
        loadData();            // Load saved data from files
        createLoginScene();     // Create login screen
        createOwnerScenes();    // Create all owner screens
        createCustomerScenes(); // Create all customer screens
        
        // Start with the login screen
        primaryStage.setScene(loginScene);
        primaryStage.show();  // Display the window
    }
    
    // Loads book and customer data from text files
    private void loadData() {
        // Load books from books.txt
        try (BufferedReader reader = new BufferedReader(new FileReader("books.txt"))) {
            String line;
            // Read each line of the file
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");  // Split by comma
                if (parts.length == 2) {  // Expecting name and price
                    // Create new book and add to list
                    bookList.add(new Book(parts[0], Double.parseDouble(parts[1])));
                }
            }
        } catch (IOException e) {}  // Silently ignore if file doesn't exist
        
        // Load customers from customers.txt
        try (BufferedReader reader = new BufferedReader(new FileReader("customers.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length == 3) {  // Expecting username, password, points
                    // Create customer and set their points
                    Customer customer = new Customer(parts[0], parts[1]);
                    customer.setPoints(Integer.parseInt(parts[2]));
                    customerList.add(customer);
                }
            }
        } catch (IOException e) {}  // Silently ignore if file doesn't exist
    }
    
    // Saves current data to text files when application closes
    private void saveData() {
        // Save books to books.txt
        try (PrintWriter writer = new PrintWriter(new FileWriter("books.txt"))) {
            // Write each book as "name,price"
            for (Book book : bookList) {
                writer.println(book.getName() + "," + book.getPrice());
            }
        } catch (IOException e) {
            e.printStackTrace();  // Print error if saving fails
        }
        
        // Save customers to customers.txt
        try (PrintWriter writer = new PrintWriter(new FileWriter("customers.txt"))) {
            // Write each customer as "username,password,points"
            for (Customer customer : customerList) {
                writer.println(customer.getUsername() + "," + 
                             customer.getPassword() + "," + 
                             customer.getPoints());
            }
        } catch (IOException e) {
            e.printStackTrace();  // Print error if saving fails
        }
    }
    
    // Creates the login screen GUI
    private void createLoginScene() {
        // Create vertical layout container
        VBox layout = new VBox(20);  // 20px spacing between elements
        layout.setPadding(new Insets(20));  // 20px padding around edges
        layout.setAlignment(Pos.CENTER);  // Center all elements
        
        // Create and style title label
        Label title = new Label("Welcome to the BookStore App");
        title.setFont(Font.font("Arial", FontWeight.BOLD, 24));
        
        // Create username input field
        TextField usernameField = new TextField();
        usernameField.setPromptText("Username");  // Hint text
        usernameField.setPrefWidth(200);  // Set width
        
        // Create password input field
        PasswordField passwordField = new PasswordField();
        passwordField.setPromptText("Password");
        passwordField.setPrefWidth(200);
        
        // Create login button
        Button loginButton = new Button("Login");
        loginButton.setPrefWidth(200);
        
        // Set action for login button
        loginButton.setOnAction(e -> {
            String username = usernameField.getText();
            String password = passwordField.getText();
            
            // Check if owner is logging in
            if (owner.getUsername().equals(username) && owner.getPassword().equals(password)) {
                primaryStage.setScene(ownerStartScene);  // Go to owner menu
            } else {
                // Check all customers for matching credentials
                for (Customer customer : customerList) {
                    if (customer.getUsername().equals(username) && 
                        customer.getPassword().equals(password)) {
                        currentCustomer = customer;  // Store logged-in customer
                        updateCustomerStartScene();  // Update customer screen
                        primaryStage.setScene(customerStartScene);  // Go to customer menu
                        return;
                    }
                }
                // Show error if no match found
                showAlert("Login Failed", "Invalid username or password");
            }
        });
        
        // Add all elements to the layout
        layout.getChildren().addAll(title, usernameField, passwordField, loginButton);
        // Create scene with this layout
        loginScene = new Scene(layout, 400, 400);
    }
    
    // Creates all owner-related screens
    private void createOwnerScenes() {
        createOwnerStartScene();    // Owner main menu
        createOwnerBooksScene();   // Book management
        createOwnerCustomersScene(); // Customer management
    }
    
    // Creates owner's main menu screen
    private void createOwnerStartScene() {
        // Vertical layout container
        VBox layout = new VBox(20);
        layout.setPadding(new Insets(20));
        layout.setAlignment(Pos.CENTER);
        
        // Button to access book management
        Button booksButton = new Button("Books");
        booksButton.setPrefWidth(200);
        booksButton.setOnAction(e -> primaryStage.setScene(ownerBooksScene));
        
        // Button to access customer management
        Button customersButton = new Button("Customers");
        customersButton.setPrefWidth(200);
        customersButton.setOnAction(e -> primaryStage.setScene(ownerCustomersScene));
        
        // Button to log out
        Button logoutButton = new Button("Logout");
        logoutButton.setPrefWidth(200);
        logoutButton.setOnAction(e -> primaryStage.setScene(loginScene));
        
        // Add buttons to layout
        layout.getChildren().addAll(booksButton, customersButton, logoutButton);
        // Create scene with this layout
        ownerStartScene = new Scene(layout, 600, 400);
    }
    
    // Creates the book management screen
    private void createOwnerBooksScene() {
        // Vertical layout container
        VBox layout = new VBox(10);
        layout.setPadding(new Insets(10));
        
        // Create table to display books
        TableView<Book> bookTable = new TableView<>();
        bookTable.setItems(bookList);  // Connect to book data
        
        // Column for book names
        TableColumn<Book, String> nameColumn = new TableColumn<>("Book Name");
        nameColumn.setCellValueFactory(cellData -> cellData.getValue().nameProperty());
        
        // Column for book prices
        TableColumn<Book, Double> priceColumn = new TableColumn<>("Book Price");
        priceColumn.setCellValueFactory(cellData -> cellData.getValue().priceProperty().asObject());
        
        // Add columns to table
        bookTable.getColumns().addAll(nameColumn, priceColumn);
        
        // Horizontal container for add book controls
        HBox addBookBox = new HBox(10);
        TextField nameField = new TextField();
        nameField.setPromptText("Name");
        TextField priceField = new TextField();
        priceField.setPromptText("Price");
        Button addButton = new Button("Add");
        
        // Add button action
        addButton.setOnAction(e -> {
            try {
                // Get price and validate
                double price = Double.parseDouble(priceField.getText());
                // Add new book through owner
                owner.addBook(bookList, nameField.getText(), price);
                // Clear input fields
                nameField.clear();
                priceField.clear();
            } catch (NumberFormatException ex) {
                showAlert("Error", "Please enter a valid price");
            } catch (IllegalArgumentException ex) {
                showAlert("Error", ex.getMessage());
            }
        });
        
        // Add controls to container
        addBookBox.getChildren().addAll(nameField, priceField, addButton);
        addBookBox.setAlignment(Pos.CENTER);
        
        // Horizontal container for action buttons
        HBox buttonBox = new HBox(10);
        Button deleteButton = new Button("Delete");
        deleteButton.setOnAction(e -> {
            // Get selected book and delete it
            Book selected = bookTable.getSelectionModel().getSelectedItem();
            owner.deleteBook(bookList, selected);
        });
        
        Button backButton = new Button("Back");
        backButton.setOnAction(e -> primaryStage.setScene(ownerStartScene));
        
        // Add buttons to container
        buttonBox.getChildren().addAll(deleteButton, backButton);
        buttonBox.setAlignment(Pos.CENTER);
        
        // Add all components to main layout
        layout.getChildren().addAll(bookTable, addBookBox, buttonBox);
        // Create scene with this layout
        ownerBooksScene = new Scene(layout, 600, 400);
    }
    
    // Creates the customer management screen
    private void createOwnerCustomersScene() {
        // Vertical layout container
        VBox layout = new VBox(10);
        layout.setPadding(new Insets(10));
        
        // Create table to display customers
        TableView<Customer> customerTable = new TableView<>();
        customerTable.setItems(customerList);  // Connect to customer data
        
        // Column for usernames
        TableColumn<Customer, String> usernameColumn = new TableColumn<>("Username");
        usernameColumn.setCellValueFactory(cellData -> cellData.getValue().usernameProperty());
        
        // Column for passwords
        TableColumn<Customer, String> passwordColumn = new TableColumn<>("Password");
        passwordColumn.setCellValueFactory(cellData -> cellData.getValue().passwordProperty());
        
        // Column for points
        TableColumn<Customer, Integer> pointsColumn = new TableColumn<>("Points");
        pointsColumn.setCellValueFactory(cellData -> cellData.getValue().pointsProperty().asObject());
        
        // Add columns to table
        customerTable.getColumns().addAll(usernameColumn, passwordColumn, pointsColumn);
        
        // Horizontal container for add customer controls
        HBox addCustomerBox = new HBox(10);
        TextField usernameField = new TextField();
        usernameField.setPromptText("Username");
        TextField passwordField = new TextField();
        passwordField.setPromptText("Password");
        Button addButton = new Button("Add");
        
        // Add button action
        addButton.setOnAction(e -> {
            try {
                // Add new customer through owner
                owner.addCustomer(customerList, usernameField.getText(), passwordField.getText());
                // Clear input fields
                usernameField.clear();
                passwordField.clear();
            } catch (IllegalArgumentException ex) {
                showAlert("Error", ex.getMessage());
            }
        });
        
        // Add controls to container
        addCustomerBox.getChildren().addAll(usernameField, passwordField, addButton);
        addCustomerBox.setAlignment(Pos.CENTER);
        
        // Horizontal container for action buttons
        HBox buttonBox = new HBox(10);
        Button deleteButton = new Button("Delete");
        deleteButton.setOnAction(e -> {
            // Get selected customer and delete them
            Customer selected = customerTable.getSelectionModel().getSelectedItem();
            owner.deleteCustomer(customerList, selected);
        });
        
        Button backButton = new Button("Back");
        backButton.setOnAction(e -> primaryStage.setScene(ownerStartScene));
        
        // Add buttons to container
        buttonBox.getChildren().addAll(deleteButton, backButton);
        buttonBox.setAlignment(Pos.CENTER);
        
        // Add all components to main layout
        layout.getChildren().addAll(customerTable, addCustomerBox, buttonBox);
        // Create scene with this layout
        ownerCustomersScene = new Scene(layout, 600, 400);
    }
    
    // Creates all customer-related screens
    private void createCustomerScenes() {
        createCustomerStartScene();  // Customer main screen
        createCustomerCostScene();   // Purchase summary screen
    }
    
    // Updates the customer screen with current data
    private void updateCustomerStartScene() {
        if (currentCustomer == null) return;  // Safety check
        
        // Get the layout and welcome label
        VBox layout = (VBox) customerStartScene.getRoot();
        Label welcomeLabel = (Label) layout.getChildren().get(0);
        
        // Update welcome message with current customer info
        welcomeLabel.setText("Welcome " + currentCustomer.getUsername() + 
                           ". You have " + currentCustomer.getPoints() + 
                           " points. Your status is " + currentCustomer.getStatus());
        
        // Get the book table and refresh its data
        TableView<Book> bookTable = (TableView<Book>) ((VBox) layout.getChildren().get(1)).getChildren().get(0);
        bookTable.setItems(bookList);
    }
    
    // Creates the customer's main screen
    private void createCustomerStartScene() {
        // Vertical layout container
        VBox layout = new VBox(20);
        layout.setPadding(new Insets(20));
        
        // Welcome label (will be updated when customer logs in)
        Label welcomeLabel = new Label();
        welcomeLabel.setFont(Font.font("Arial", FontWeight.BOLD, 16));
        
        // Create book table
        TableView<Book> bookTable = new TableView<>();
        bookTable.setEditable(true);  // Allow editing checkboxes
        bookTable.setSelectionModel(null);  // Disable row selection
        
        // Column for book names
        TableColumn<Book, String> nameColumn = new TableColumn<>("Book Name");
        nameColumn.setCellValueFactory(cellData -> cellData.getValue().nameProperty());
        nameColumn.setEditable(false);  // Can't edit names
        
        // Column for book prices
        TableColumn<Book, Double> priceColumn = new TableColumn<>("Book Price");
        priceColumn.setCellValueFactory(cellData -> cellData.getValue().priceProperty().asObject());
        priceColumn.setEditable(false);  // Can't edit prices
        
        // Column for selection checkboxes
        TableColumn<Book, Boolean> selectColumn = new TableColumn<>("Select");
        selectColumn.setEditable(true);  // Allow editing checkboxes
        selectColumn.setCellValueFactory(cellData -> cellData.getValue().selectedProperty());
        // Custom cell factory for checkboxes
        selectColumn.setCellFactory(column -> {
            CheckBoxTableCell<Book, Boolean> cell = new CheckBoxTableCell<>(index -> {
                Book book = bookTable.getItems().get(index);
                return book.selectedProperty();
            });
            cell.setAlignment(Pos.CENTER);  // Center the checkbox
            return cell;
        });
        
        // Add all columns to table
        bookTable.getColumns().addAll(nameColumn, priceColumn, selectColumn);
        
        // Container for table
        VBox tableBox = new VBox(bookTable);
        tableBox.setPadding(new Insets(10));
        
        // Horizontal container for action buttons
        HBox buttonBox = new HBox(20);
        Button buyButton = new Button("Buy");
        Button redeemButton = new Button("Redeem points and Buy");
        Button logoutButton = new Button("Logout");
        
        // Logout button action
        logoutButton.setOnAction(e -> {
            currentCustomer = null;  // Clear current customer
            primaryStage.setScene(loginScene);  // Return to login
        });
        
        // Buy button action
        buyButton.setOnAction(e -> {
            // Get all selected books
            List<Book> selectedBooks = bookList.stream()
                .filter(Book::isSelected)
                .collect(Collectors.toList());
            
            // Check if any books were selected
            if (selectedBooks.isEmpty()) {
                showAlert("Error", "Please select at least one book");
                return;
            }
            
            // Process purchase
            currentCustomer.buyBooks(selectedBooks);
            // Clear selections
            selectedBooks.forEach(book -> book.setSelected(false));
            // Update and show cost screen
            updateCustomerCostScene(selectedBooks.stream().mapToDouble(Book::getPrice).sum());
            primaryStage.setScene(customerCostScene);
        });
        
        // Redeem and buy button action
        redeemButton.setOnAction(e -> {
            // Get all selected books
            List<Book> selectedBooks = bookList.stream()
                .filter(Book::isSelected)
                .collect(Collectors.toList());
            
            // Check if any books were selected
            if (selectedBooks.isEmpty()) {
                showAlert("Error", "Please select at least one book");
                return;
            }
            
            // Process redemption purchase
            double[] paymentDetails = currentCustomer.redeemPointsAndBuy(selectedBooks);
            // Clear selections
            selectedBooks.forEach(book -> book.setSelected(false));
            // Update and show cost screen with amount actually paid
            updateCustomerCostScene(paymentDetails[2]);
            primaryStage.setScene(customerCostScene);
        });
        
        // Add buttons to container
        buttonBox.getChildren().addAll(buyButton, redeemButton, logoutButton);
        buttonBox.setAlignment(Pos.CENTER);
        
        // Add all components to main layout
        layout.getChildren().addAll(welcomeLabel, tableBox, buttonBox);
        // Create scene with this layout
        customerStartScene = new Scene(layout, 600, 500);
    }
    
    // Updates the cost screen with purchase information
    private void updateCustomerCostScene(double amountPaid) {
        if (currentCustomer == null) return;  // Safety check
        
        // Get layout and labels
        VBox layout = (VBox) customerCostScene.getRoot();
        Label totalCostLabel = (Label) layout.getChildren().get(0);
        Label pointsLabel = (Label) layout.getChildren().get(1);
        
        // Update labels with current information
        totalCostLabel.setText("Total Cost: " + String.format("%.2f", amountPaid));
        pointsLabel.setText("Points: " + currentCustomer.getPoints() + 
                          ", Status: " + currentCustomer.getStatus());
    }
    
    // Creates the purchase summary screen
    private void createCustomerCostScene() {
        // Vertical layout container
        VBox layout = new VBox(20);
        layout.setPadding(new Insets(20));
        layout.setAlignment(Pos.CENTER);
        
        // Label for total cost (will be updated)
        Label totalCostLabel = new Label();
        totalCostLabel.setFont(Font.font("Arial", FontWeight.BOLD, 16));
        
        // Label for points and status (will be updated)
        Label pointsLabel = new Label();
        pointsLabel.setFont(Font.font("Arial", 14));
        
        // Logout button
        Button logoutButton = new Button("Logout");
        logoutButton.setOnAction(e -> {
            currentCustomer = null;  // Clear current customer
            primaryStage.setScene(loginScene);  // Return to login
        });
        
        // Add all components to layout
        layout.getChildren().addAll(totalCostLabel, pointsLabel, logoutButton);
        // Create scene with this layout
        customerCostScene = new Scene(layout, 400, 300);
    }
    
    // Helper method to show error messages
    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle(title);
        alert.setHeaderText(null);  // No header
        alert.setContentText(message);
        alert.showAndWait();  // Show and wait for dismissal
    }
    
    // Called when application is closing
    @Override
    public void stop() {
        saveData();  // Save all data to files
    }
}