+---------------------------------------+
|                Bank                   |
+---------------------------------------+
| - accounts: List<Account>             |
+---------------------------------------+
| + createAccount(password: String):    |
|   Account                              |
| + closeAccount(account: Account):     |
| + processTransaction(transaction:    |
|   Transaction): boolean               |
+---------------------------------------+
                    |
                    |
                    V
+---------------------------------------+
|              Account                  |
+---------------------------------------+
| - accountId: String                   |
| - balance: float                      |
| - customer: Customer                  |
+---------------------------------------+
| + deposit(amount: float):             |
| + withdraw(amount: float): boolean    |
| + queryBalance(): float               |
+---------------------------------------+
                    |
                    |
                    V
+---------------------------------------+
|             Customer                  |
+---------------------------------------+
| - customerId: String                  |
| - name: String                        |
| - address: String                     |
+---------------------------------------+
| + changePassword(newPassword:        |
|   String): boolean                    |
| + transferMoney(receiverId: String,   |
|   amount: float): boolean             |
+---------------------------------------+
                    |
                    |
                    V
+---------------------------------------+
|                ATM                    |
+---------------------------------------+
| - atmId: String                       |
| - bank: Bank                          |
+---------------------------------------+
| + insertCard(cardId: String):         |
| + returnCard():                       |
| + depositCash(amount: float):         |
| + withdrawCash(amount: float,         |
|   password: String): boolean          |
+---------------------------------------+
                    |
                    |
                    V
+---------------------------------------+
|                App                    |
+---------------------------------------+
| - appId: String                       |
| - customer: Customer                  |
+---------------------------------------+
| + logIn(customerId: String,           |
|   password: String): boolean          |
| + logOut():                           |
| + closeApp():                         |
| + changePassword(newPassword:        |
|   String): boolean                    |
| + transferMoney(receiverId: String,   |
|   amount: float): boolean             |
| + query(): float                      |
+---------------------------------------+