package bookstoreapp; // Package declaration for organization

// SilverState represents the state of a customer who has a "Silver" status
// It implements the CustomerState interface, meaning it defines the behavior of a Silver customer.
class SilverState implements CustomerState {

    // Method to get the customer's status. This will always return "Silver" for this class.
    @Override
    public String getStatus() {
        return "Silver"; // The status of the customer is Silver
    }
}
