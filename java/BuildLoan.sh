#!/bin/bash
#set -x
rm -f *.class
javac UnitTestHarness.java
javac LoanTest.java
java LoanTest | ./annotater.py loantest-run-1
echo "Hey that looked ok, but maybe some tests are flaky?"
echo "Lets run it again ... "
java LoanTest | ./annotater.py loantest-run-2
if [ $? ]
then
  echo "Build failed"
else
  javac Loan.java
  echo "Ready to execute Loan"
fi
