#!/usr/bin/env python3
import os
import sys
#from turtle import st
import unittest
import subprocess
import datetime

FAILED=1
PASSED=0

global grade

grade = 0

def date(): # returns string approximating *nix date command output
    return datetime.datetime.now().strftime('%a %b %d %H:%M:%S %z %Y')

def checkFileExists(pathname):
    if os.path.exists(pathname):
        return True
    else:
        print(f"I expected to find a file called {pathname} but it did not exist")
        print("(or was not a regular file)")
        print("Here are the files that I can find:")
        print(os.listdir())
        return False

def runTests(testCases):
    suite = unittest.TestSuite()
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(testCases)
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    success = len(result.failures) == 0 and len(result.errors) == 0 and result.testsRun > 0
    return success

required_files = ["election.py"]

def read_file(name): 
    with open(name) as f: 
        return f.read()

class TestElectionEvalPregrader(unittest.TestCase):
    def test_checkAnswersExist(self):
        """Check expected files provided"""
        for filename in required_files:
            r = self.assertTrue(checkFileExists(filename),filename + " not found")

    def run_program_provided_data(self, test_name, state_info_file, vote_info_file):
        command = "python3 -u election.py " + state_info_file + " " + vote_info_file
        student_result = subprocess.run(command.split(),stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        student_recounts = read_file("./recounts.txt")

        solution_python_file =  "solution.py"
        solution_command = "python3 -u "+ solution_python_file + " " + state_info_file + " " + vote_info_file
        solution_result = subprocess.run(solution_command.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')  
        solution_recounts = read_file("./recounts.txt")                    
        self.assertEqual(student_result.stdout, solution_result.stdout, test_name+ ": output does not match the expected output.")
        self.assertEqual(student_recounts,solution_recounts,test_name+ ": recounts.txt does not match the expected contents")
        #global grade
        #grade += 20

    def test_simple_states_diff(self):
        """Tests Simple States"""
        self.run_program_provided_data("Simple States","Simple_States.txt","SimpleVotes1.txt")
        global grade
        grade += 25

    def test_us_states_1(self):
        """Tests US States"""
        self.run_program_provided_data("US States-1","US_States.txt","USVotes1.txt")
        global grade
        grade += 25

    def test_us_states_2(self):
        """Tests US States"""
        self.run_program_provided_data("US States-2","US_States.txt","USVotes2.txt")
        global grade
        grade += 25

    def test_us_states_3(self):
        """Tests US States"""
        self.run_program_provided_data("US States-3","US_States.txt","USVotes3.txt")
        global grade
        grade += 25

if __name__ == '__main__':
    print('Grading at',date())
    if len(sys.argv) == 1:
        success = runTests(TestElectionEvalPregrader)
        sys.exit(grade)
