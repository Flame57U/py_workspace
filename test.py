import requests
# Python 中级工程师课程 - 第1节示例
# 主题：面向对象编程基础（类与对象）

from datetime import date, timedelta


class Book:
    """图书类：包含书名、作者和可借状态"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "已借出" if self.is_borrowed else "可借"
        return f"《{self.title}》 - {self.author} ({status})"
#__str__  表示打印出来的内容

class Member:
    """图书馆会员类"""
    def __init__(self, name):
        self.name = name
        self.borrowed_books = {}

    def borrow(self, book: Book):
        if book.is_borrowed:
            print(f"❌ {book.title} 已被借走了！")
        else:
            book.is_borrowed = True
            due_date = date.today() + timedelta(days=14)
            self.borrowed_books[book.title] = due_date
            print(f"✅ {self.name} 借走了 {book.title}，请在 {due_date} 前归还。")

    def return_book(self, book: Book):
        if book.title in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.pop(book.title)
            print(f"📚 {self.name} 已归还 {book.title}")
        else:
            print(f"⚠️ {self.name} 并没有借 {book.title}")


if __name__ == "__main__":
    # 创建书籍
    book1 = Book("Python核心编程", "Wesley Chun")
    book2 = Book("流畅的Python", "Luciano Ramalho")

    # 创建会员
    alice = Member("Alice")
    bob = Member("Bob")

    # 借书操作
    alice.borrow(book1)
    bob.borrow(book1)  # 冲突：已被借走
    bob.borrow(book2)

    # 查看状态
    print(book1)
    print(book2)

    # 归还
    alice.return_book(book1)
    bob.borrow(book1)
