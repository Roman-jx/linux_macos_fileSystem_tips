# #Import modules
import unittest     #Import main module for testing

#Takes value from modules
from unittest import TestCase           #Take only TestCase, main modules to recalculate our arguments
from main import *                      #Take all functions from the module

#Test for main class
class LsTest(TestCase):
    #Correct tests
    def test_get_path(self):
        self.assertEqual(Ls.get_path(Ls.SCRIPT_PATH), f"{Path('main.py').parent.absolute()}/")
        self.assertEqual(Ls.get_path(Ls.RUN_PATH), f"{Path('main.py').parent.absolute()}/main.py")
        self.assertTrue(Ls.get_path(Ls.DEFINED_PATH) in Ls.find_path(Ls.get_path(Ls.DEFINED_PATH)))

    def test_get_file_list(self):
        self.assertTrue(Ls.get_directory_list("./"))
        self.assertTrue(Ls.get_directory_list("../.././"))
        self.assertTrue(Ls.get_directory_list("../"))

    def test_get_directory_list(self):
        self.assertTrue(Ls.get_directory_list("./"))
        self.assertTrue(Ls.get_directory_list("."))
        self.assertTrue(Ls.get_directory_list(".././"))

    def test_get_file_info(self):
        self.assertTrue(Ls.get_directory_list("./"))
        self.assertTrue(Ls.get_directory_list("../.././"))
        self.assertTrue(Ls.get_directory_list("../"))

    def test_get_directory_info(self):
        self.assertTrue(Ls.get_directory_list("./"))
        self.assertTrue(Ls.get_directory_list("."))
        self.assertTrue(Ls.get_directory_list(".././"))

    def test_save_as_txt(self):
        self.assertEqual(TEXT_FILE_NAME, None)
        self.assertNotEqual(TEXT_FILE_NAME, "text.txt")
        self.assertNotEqual(TEXT_FILE_NAME, "root.txt")

    def test_save_as_csv(self):
        self.assertEqual(CSV_FILE_NAME, None)
        self.assertNotEqual(CSV_FILE_NAME, "text.csv")
        self.assertNotEqual(CSV_FILE_NAME, "root.csv")

    def test_save_as_json(self):
        self.assertEqual(JSON_FILE_NAME, None)
        self.assertNotEqual(JSON_FILE_NAME, "text.json")
        self.assertNotEqual(JSON_FILE_NAME, "root.json")

    def test_save_as_html(self):
        self.assertEqual(HTML_FILE_NAME, None)
        self.assertNotEqual(HTML_FILE_NAME, "text.html")
        self.assertNotEqual(HTML_FILE_NAME, "root.html" )

    def test_get_task_status(self):
        self.assertEqual(Ls.get_task_status(GET_TASK_STATUS), GET_TASK_STATUS)
        self.assertNotEqual(Ls.get_task_status(GET_TASK_STATUS), 100)
        self.assertNotEqual(Ls.get_task_status(GET_TASK_STATUS), 300)
        self.assertNotEqual(Ls.get_task_status(GET_TASK_STATUS), 400)
        self.assertNotEqual(Ls.get_task_status(GET_TASK_STATUS), 500)

    def test_get_report_content(self):
        self.assertTrue(Ls.get_report_content("main.py") != '')
        self.assertTrue(Ls.get_report_content("test_unit.py") != '')


#Run main func
if __name__ == "__main__":
    unittest.main()