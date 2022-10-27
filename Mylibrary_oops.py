class Mylibrary:
    def __init__(self,shelf):
        self.shelf = shelf
        self.readers = {}
        self.books = {}

    def my_record(self,user,id):
        readers = list(self.readers.keys())
        if id in readers:
            if user == self.readers[id]['name']:
                print(f"----this is your record in our library:\n ----{user}--{self.readers[id]}")
            else:
                print(f"----this user name does not match the user's id: ")
                input("----enter any key to continue: ")
        else:
            print(f"----this user does not exist in our library records: ----")
            input("----enter any key to continue: ")

    def lend_book(self,user,id,lend,num):
        if self.shelf[lend] == 0:
            print(f"sorry right now we don't have copies of this book: ")
            input("----enter any key to continue: ")
        elif num > self.shelf[lend]:
            print(f"----sorry we only have {self.shelf[lend]} copies:----")
            input("----enter any key to continue: ")
        else:
            readers = list(self.readers.keys())
            if id in readers:
                if user == self.readers[id]['name']:
                    books = list(self.readers[id].keys())
                    shelf_books = list(self.shelf.keys())
                    if lend in shelf_books:
                        if lend in books:
                            self.readers[id][lend] = self.readers[id][lend]+num
                            self.shelf[lend] = self.shelf[lend]-num
                            print(f"----thank you lending from our books:----")
                            input("----enter any key to continue: ")
                        else:
                            self.readers[id].update({lend:num,"name":user})
                            self.shelf[lend] = self.shelf[lend]-num
                            print(f"----thank you lending from our books:----")
                            input("----enter any key to continue: ")
                    else:
                        print(f"----sorry we don't have this book in our collection: ----")
                        input("----enter any key to continue: ")
                else:
                    print(f"----this user name does not match the user's id: ")
                    input("----enter any key to continue: ")
            else:
                shelf_books = list(self.shelf.keys())
                if lend in shelf_books:
                    self.readers[id] = {lend:num,"name":user}
                    self.shelf[lend] = self.shelf[lend]-num
                    print(f"----thank you for lending from our books:----")
                    input("----enter any key to continue: ")
                else:
                    print(f"----sorry we don't have this book in our collection: ----")
                    input("----enter any key to continue: ")

    def give_book(self,user,id,lend,num):
        readers = list(self.readers.keys())
        if id in readers:
            if user == self.readers[id]["name"]:
                shelf_books = list(self.shelf.keys())
                if lend in shelf_books:
                    if num == self.readers[id][lend] or num < self.readers[id][lend]:
                        self.readers[id][lend] = self.readers[id][lend]-num
                        self.shelf[lend] = self.shelf[lend] + num
                        print(f"----thank you for returning this book:\n----hope you have liked it:----")
                        input("----enter any key to continue: ")
                    else:
                        extra = num - self.readers[id][lend]
                        print(f"----oops your giving us {extra} extra copies----still you wanna give extra copies----1.yes\n2.no")
                        opt = int(input("enter your option: 1 or 2: "))
                        if opt == 2:
                            num = num - self.readers[id][lend]
                            self.readers[id][lend] = 0
                            self.shelf[lend] = self.shelf[lend]+num
                            print("ok---no problem---\nwe just have taken number of books you have to give back----\n have a nice day:--- ")
                            input("----enter any key to continue: ")
                        elif opt == 1:
                            self.shelf[lend] = self.shelf[lend]+num
                            self.readers[id][lend] = 0
                            print(f"----thank you for the books:\n----thank you for the extra copies:---\n-----have a nice day---")
                            input("----enter any key to continue: ")
                        else:
                            print("----Invalid input:----")
                            input("----enter any key to continue: ")
                else:
                    print(f"----this book is not taken you still wanna give:----\n1.yes\n2.no")
                    opt = int(input("enter optiion: 1 or 2: "))
                    if opt == 2:
                        print("ok no problem: have a nice day: ---")
                        input("----enter any key to continue: ")
                    elif opt == 1:
                        self.shelf[lend] = num
                        print(f"thank you for giving us books:----have a nice day---:)")
                        input("----enter any key to continue: ")
                    else:
                        print("----Invalid input:----")
                        input("----enter any key to continue: ")
            else:
                print(f"----this user name does not match the user's id: ")
                input("----enter any key to continue: ")
        else:
            print("----you are not among the readers:----\n still you wanna give book----1.yes\n2.no\n")
            opt = int(input("enter your option: 1 or 2: "))
            if opt == 2:
                print("ok---no problem: have a nice day:--- ")
                input("----enter any key to continue: ")
            elif opt == 1:
                shelf_books = list(self.shelf.keys())
                if lend in shelf_books:
                    self.shelf[lend] = self.shelf[lend]+num
                    print(f"----thank you for the books:----")
                    input("----enter any key to continue: ")
                else:
                    self.shelf[lend] = num
                    print(f"----thank you for the books:----")
                    input("----enter any key to continue: ")
            else:
                print("----Invalid input:----")
                input("----enter any key to continue: ")




if __name__ == "__main__":
    pass


# myshelf = {}
# books = int(input("how many books you wanna keep in your library: "))
# for i in range(books):
#     book_name = input("enter book name: ")
#     num = int(input("enter number of books u wanna add to your library: "))
#     myshelf[book_name] = num

myshelf = {"harry":5,"magnum":5,"opus":5}
admins = {"khaja":"kb00"}

mylib = Mylibrary(myshelf)

def myfun():
    print(f"-----Welcome to our library-!!!\n1.Are you an Admin----\n2.Are you a Reader----\n3.leave\n")
    opt = int(input("enter your option:----"))
    if opt == 1:
        admin_name = input("enter admin name: ")
        pwrd = input("enter password: ")
        adm = list(admins.keys())
        if admin_name in adm:
            if pwrd == admins[admin_name]:
                while (True):
                    print("""--------
                    -----1.see library readers records:-----
                    -----2.see books available in library-----
                    -----3.see readers list-----
                    -----4.see admins list-----
                    -----5.quit library------""")
                    try:
                        opt = int(input("enter your option-----\n--"))
                        if opt == 1:
                            print(mylib.readers)
                        elif opt == 2:
                            print(mylib.shelf)
                        elif opt == 3:
                            print(mylib.readers[id]["name"])
                        elif opt == 4:
                            print(admins.keys())
                        elif opt == 5:
                            break
                        else:
                            print("----invalid input:----")
                    except:
                        print('Unhhhh.... no no no!!!\ntry again...')
            else:
                print("----wrong password:----")
        else:
            print("----this admin name does not exist:----")

    elif opt == 2:
        user = input("enter your name: ")
        id = input("enter your unique id:----")
        while (True):
            print("""-----------
            1--lend a book:
            2--return a book:
            3--your record: 
            4--quite library:
            5.data""")
            try:
                opt = int(input("enter your option: "))
                if opt == 1:
                    lend = (input('enter book name u wanna lend: '))
                    num = int(input('enter how many copies u wanna lend: '))
                    mylib.lend_book(user,id,lend,num)

                elif opt == 2:
                    lend = (input('enter book name u wanna return: '))
                    num = int(input('enter how many copies u wanna return: '))
                    mylib.give_book(user,id,lend,num)

                elif opt == 3:
                    mylib.my_record(user,id)

                elif opt == 4:
                    break

                elif opt == 5:
                    print(f"available books in libray {mylib.shelf}")
                
                else:
                    print("----Invalid input:----")
            except:
                print('Unhhhh.... no no no!!!\ntry again...')
    elif opt == 3:
        print("thank you for coming:---bye!!!-----")
        exit()

    else:
        print("invalid input:----")
myfun()

