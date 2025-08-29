package bookstoreapp; // Package declaration for organization

// GoldState represents the state of a customer who has a "Gold" status
// Like SilverState, it implements the CustomerState interface to define the behavior of a Gold customer.
class GoldState implements CustomerState {

    // Method to get the customer's status. This will always return "Gold" for this class.
    @Override
    public String getStatus() {
        return "Gold"; // The status of the customer is Gold
    }
}
