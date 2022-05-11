import unittest

import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
from Python_curs.curs_10_Assert_ImplicitExplicit.Tema9 import Login

# 1.	Faceti o suita care sa contina testele voastre de la tema 9 + testele de la intalnirea 10
# (care au clasa). Generati raportul

class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_tema9 = unittest.TestSuite()
        test_tema9.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login)

        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports = True,
            report_title = 'Raport1',
            report_name = 'Raport_tema9'
        )

        runner.run(test_tema9)

# 2.	Scrieti cu sintaxa gherkin toate testele de la tema9 (mai putin 12)
# 3.	Ganditi voi o clasa de test din paginile sugerate in tema 8 (ce doriti voi, cate functii de test doriti, freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test). Folositi firefox in loc de chrome
#
# https://www.phptravels.net/
# http://automationpractice.com/index.php
# https://formy-project.herokuapp.com/
# https://the-internet.herokuapp.com/
# https://www.techlistic.com/p/selenium-practice-form.html
#
# Sau puteti alege voi ce pagina doriti
