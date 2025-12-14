<h1 align="center">🏧 ATM Simulator (Python)</h1>

<p align="center">
  A console-based ATM simulator written in Python using core programming concepts:
  functions, loops, conditionals, input validation, and in-memory data handling.
</p>

<h2>📘 Project Overview</h2>

<p>
  This program simulates a realistic ATM system for
  <strong>registered bank account holders</strong>.
  Each user can securely log in using their account number and PIN,
  perform multiple banking operations, and receive a detailed receipt
  at the end of the session.
</p>

<p>
  All account data is stored in Python lists and dictionaries during runtime.
  No files, databases, or external libraries are used.
</p>

<h2>🧰 Technologies Used</h2>

<ul>
  <li>Python (functions, loops, conditionals)</li>
  <li>Lists and dictionaries for account storage</li>
  <li>Input validation using string methods</li>
  <li>No external libraries required</li>
</ul>

<h2>📂 Program Execution Flow</h2>

<ol>
  <li>
    Main menu is displayed with options to:
    <ul>
      <li>Perform an ATM operation</li>
      <li>Exit the program</li>
    </ul>
  </li>
  <li>User enters an account number to log in.</li>
  <li>The system searches for the account in stored records.</li>
  <li>User enters PIN with a maximum of three attempts.</li>
  <li>On successful authentication, the ATM menu is displayed.</li>
  <li>All transactions are tracked during the session.</li>
  <li>A receipt is generated before exiting the session.</li>
</ol>

<h2>🔐 Login & PIN System</h2>

<ul>
  <li>Login requires a valid account number and PIN.</li>
  <li>PIN must contain only digits.</li>
  <li>Maximum of <strong>three incorrect attempts</strong> allowed.</li>
  <li>Account access is denied after exceeding attempts.</li>
</ul>

<h2>👤 Registered User Accounts</h2>

<p>
  The system maintains predefined bank accounts in memory:
</p>

<pre>
accounts = [
  {
    "name": "Ahmed",
    "account_no": "49217385",
    "pin": "1234",
    "balance": 12000,
    "initial_balance": 12000
  },
  ...
]
</pre>

<ul>
  <li>Accounts are searched by account number.</li>
  <li>PINs are stored as strings for validation consistency.</li>
  <li>Each account tracks its initial balance for receipt generation.</li>
</ul>

<h2>📋 ATM Menu Options</h2>

<p>Once logged in, the account holder can:</p>

<ol>
  <li>View Balance</li>
  <li>Deposit Money</li>
  <li>Withdraw Money</li>
  <li>Pay Utility Bills</li>
  <li>Change ATM PIN</li>
  <li>Exit Session</li>
</ol>

<h2>💰 Banking Features</h2>

<ul>
  <li>
    <strong>Balance Inquiry:</strong>
    Displays current balance and logs the action.
  </li>
  <li>
    <strong>Deposit:</strong>
    Allows only positive numeric amounts.
  </li>
  <li>
    <strong>Withdrawal:</strong>
    Prevents overdrawing the account.
  </li>
  <li>
    <strong>Utility Bill Payments:</strong>
    <ul>
      <li>Electricity</li>
      <li>Gas</li>
      <li>Water</li>
      <li>Internet / WiFi</li>
      <li>Telephone / Mobile</li>
    </ul>
  </li>
  <li>
    <strong>PIN Change:</strong>
    Requires old PIN verification and confirmation.
  </li>
</ul>

<h2>🧾 Transaction Receipt</h2>

<p>
  At the end of each session, a receipt is automatically generated showing:
</p>

<ul>
  <li>Account holder name</li>
  <li>Starting balance</li>
  <li>Closing balance</li>
  <li>Complete transaction history</li>
</ul>

<p>
  If no actions were performed, the receipt clearly indicates this.
</p>

<h2>🧠 Learning Objectives</h2>

<ul>
  <li>Design menu-driven console applications.</li>
  <li>Implement secure authentication logic.</li>
  <li>Track and manage session-based state.</li>
  <li>Apply input validation and error handling.</li>
  <li>Simulate real-world ATM workflows using Python.</li>
</ul>

<h3 align="center">✨ Thank You for Visiting! ✨</h3>

<p align="center">
  Feel free to explore, refactor, and extend this ATM simulator
  to enhance your Python programming skills.
</p>
