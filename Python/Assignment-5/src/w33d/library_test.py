import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        # 重置 Library 类的类变量，以确保测试间的独立性
        Library.total_books = 0
        # 初始化两个图书馆实例，用于测试
        self.lib1 = Library("Downtown", ["1984", "To Kill a Mockingbird"])
        self.lib2 = Library("Uptown", ["The Great Gatsby"])

    def test_initialization(self):
        # 测试图书馆实例是否正确初始化
        self.assertEqual(self.lib1.name, "Downtown")
        self.assertEqual(self.lib1.books, ["1984", "To Kill a Mockingbird"])
        self.assertEqual(self.lib2.name, "Uptown")
        self.assertEqual(self.lib2.books, ["The Great Gatsby"])
        # 测试类变量是否正确更新
        self.assertEqual(Library.total_books, 3)  # 总书籍数应为3

    def test_add_book(self):
        # 测试添加书籍功能
        self.lib1.add_book("Pride and Prejudice")
        self.assertIn("Pride and Prejudice", self.lib1.books)
        self.assertEqual(Library.total_books, 4)  # 总书籍数应更新为4

    def test_display_total_books(self):
        # 使用 `unittest.mock` 模块来捕获输出
        from io import StringIO
        import sys
        capturedOutput = StringIO()          # 创建 StringIO 对象捕获输出
        sys.stdout = capturedOutput          # 重定向 stdout
        Library.display_total_books()        # 调用方法
        sys.stdout = sys.__stdout__          # 重置重定向
        self.assertIn("Total books in all libraries: 3", capturedOutput.getvalue().strip())

    def test_info(self):
        # 测试 info 静态方法的输出
        from io import StringIO
        import sys
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        Library.info()
        sys.stdout = sys.__stdout__
        expected_output = "A library is a collection of books and resources in digital or printed formats that is organized for use and maintained by a public body, an institution, or a private individual."
        self.assertIn(expected_output, capturedOutput.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
