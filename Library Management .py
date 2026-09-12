class Book :
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def _str_(self):
        return f"'{self.title}' by {self.author} | Available: {self.is_available}"

class User :
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_book = []
    def _str_(self):
        return f"User: {self.name} | ID: {self.user_id}"

class Library :
    def __init__(self):
        self.books = []
        self.users = [] 
    def add_book(self,book):
        self.books.append(book)
       
    def register_user(self, register_user):
        self.users.append(register_user)
        
    def borrow_book(self, user, book):
        if book.is_available:
            book.is_available = False
            user.borrowed_book.append(book)
            print(f"Success: '{book.title}' borrowed by {user.name}.")
        else:
            print(f"Failed: '{book.title}' is already borrowed.")
   
    def return_book(self, user, book):
        if book in user.borrowed_book:
            user.borrowed_book.remove(book)
            book.is_available = True
            print(f"Success: '{book.title}' returned by {user.name}.")
        else:
            print(f"Failed: '{user.name}' did not borrow '{book.title}'.")
my_library = Library()

while True :
    print("""1. add book
2. register user
3. borrow book
4. return book
5. exit""")
    try :
     choice = int(input('Enter choice: '))    
    except:
     print('invalid input')
     continue

    if choice == 1:
         title = input("Enter book title: ")
         author = input('Enter book author: ')
         new_book = Book(title,author)
         my_library.add_book(new_book)
         print(f"Book '{title}' added successfully.")

    elif choice ==2:
        name = input("enter name: ")
        user_id = input('Enter user_id: ')     
        new_register = User(name,user_id)
        my_library.register_user(new_register)
        print(f"user'{name}' with ID'{user_id}' registered successfully")

    elif choice == 3:
        user_id = input('user_id: ')
        book_title = input('Enter book title: ')

        found_user = None
        found_book = None

        for u in my_library.users :
            if u.user_id == user_id: found_user = u
        for b in my_library.books:    
            if b.title == book_title: found_book = b
        if found_user and found_book:
            my_library.borrow_book(found_user,found_book)
        else:
            print('user or book not found')  

    elif choice == 4:
        user_id = input("Enter user ID: ")
        book_title = input("Enter book title: ")

        found_user = None
        found_book = None

        for u in my_library.users:
            if u.user_id == user_id:
                found_user = u

        for b in my_library.books:
            if b.title == book_title:
                found_book = b

        if found_user and found_book:
            my_library.return_book(found_user, found_book)
        else:
            print("User or Book not found.")

    elif choice == 5:
        print("Exixting...")
        break
    else:
        print("invalid choice")

    



     





        
          
        

