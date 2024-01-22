/**
 * The Book class represents a book with a title and an author.
 */
class Book {
    private String title;
    private String author;

    /**
     * Constructor for Book.
     * @param title The title of the book.
     * @param author The author of the book.
     */
    Book(String _title, String _author) {
        title = _title;
        author = _author;
    }

    /**
     * Displays information about the book.
     */
    public void displayBookInfo() {
        System.out.println("Book Title: " + title);
        System.out.println("Author: " + author);
    }
}

public class BookTest {
    public static void main(String[] args) {
        Book myBook = new Book("The Great Gatsby", "F. Scott Fitzgerald");
        myBook.displayBookInfo();
    }
}