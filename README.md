<h1 align="center">🏧 ATM Simulator (Python)</h1>
<p align="center">
  A console-based ATM simulator written in Python using only core programming concepts:
  loops, conditionals, functions, and basic data structures.
</p>

<h2>📘 Project Overview</h2>
<p>
  This program simulates a realistic ATM system with two modes of operation:
</p>
<ul>
  <li><strong>Registered Account Holder</strong> – uses stored accounts with PIN and balance.</li>
  <li><strong>General User</strong> – temporary account created for the session only.</li>
</ul>
<p>
  All data is stored in Python lists and dictionaries in memory, without using files or databases.
  The entire workflow runs through the terminal using menus and simple user input.
</p>

<h2>🧰 Technologies Used</h2>
<ul>
  <li>Python (functions, loops, conditionals)</li>
  <li>Lists and dictionaries for user account storage</li>
  <li>No external libraries required</li>
</ul>

<h2>📂 Program Execution Flow</h2>
<ol>
  <li>Show main screen with three options:
    <ul>
      <li>Registered Account Holder</li>
      <li>General User</li>
      <li>Exit</li>
    </ul>
  </li>
  <li>User selects a type and the system proceeds with PIN authentication.</li>
  <li>On successful login, the user accesses their banking menu.</li>
  <li>All updates are stored in memory until the program exits.</li>
</ol>

<h2>🔐 Login & PIN System</h2>
<ul>
  <li>User must enter the correct PIN to proceed.</li>
  <li>Maximum of <strong>three attempts</strong> allowed.</li>
  <li>Failure results in access being denied for that session.</li>
</ul>

<h2>👤 Registered User Accounts</h2>
<p>
  A list of stored accounts is maintained in memory:
</p>
<pre>
accounts = [
    {"name": "Ali", "account_no": "49217385", "pin": 1234, "balance": 12000},
    {"name": "Ayesha", "account_no": "83726149", "pin": 6789, "balance": 18000},
    ...
]
</pre>
<ul>
  <li>Accounts are searchable by account number.</li>
  <li>Changes apply immediately to this list until the program ends.</li>
</ul>

<h2>📋 Main Menu Options</h2>
<p>Once logged in, the user can choose:</p>
<ol>
  <li>Check Balance</li>
  <li>Deposit Money</li>
  <li>Withdraw Money</li>
  <li>Change PIN</li>
  <li>Pay Utility Bills </li>
  <li>Logout / Exit</li>
</ol>

<h2>💰 Banking Features</h2>
<ul>
  <li><strong>Balance Updates:</strong> Deposits and withdrawals instantly update the balance.</li>
  <li><strong>Insufficient Balance Handling:</strong> Withdrawals only succeed if enough funds exist.</li>
  <li><strong>Guest Mode:</strong> General user data is wiped after logout.</li>
  <li><strong>PIN Change Support:</strong> Users can update their PIN after authentication.</li>
</ul>

<h2>🧾 Optional Receipt</h2>
<p>
  On logout, the system can generate a session summary showing:
</p>
<ul>
  <li>Opening balance</li>
  <li>Total deposits</li>
  <li>Total withdrawals</li>
  <li>Final balance</li>
</ul>

<h2>🎯 Learning Objectives</h2>
<ul>
  <li>Build multi-screen program logic using functions.</li>
  <li>Practice input validation and secure access flow.</li>
  <li>Understand how state is stored and updated in memory.</li>
  <li>Simulate real-world ATM behavior in a console environment.</li>
</ul>

<h3 align="center">✨ Thank You for Visiting! ✨</h3>
<p align="center">
  Explore the code, learn from it, and modify the logic for your own Python projects!
</p>
