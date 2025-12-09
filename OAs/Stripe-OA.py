'''
### Account Balance Manager

Imagine you are creating the backend for an app called StripePay,
a peer-to-peer payment method. Stripe users send each other money
and transfer money to and from their bank accounts.

Stripe users make thousands of transactions daily, so we need
functionality that handles:
- balance changes,
- transactions,
- balance reads.

Please read the entire prompt before coding. Some test cases will
not pass unless all constraints are met.

We will implement the core backend logic: users sending money.

However, the network can be unreliable. Sometimes we get
transactions out of order. Therefore, all commands must be executed
in **chronological order** (sorted by timestamp).

StripePay users also move money to/from their connected banks.

You are given a list of commands for an account balance API.
You must:

1. Parse each command.
2. Execute them in **timestamp order**.
3. Return a **comma-separated string** of command results in the
   order the commands were received as input.
4. There is at most one command per timestamp.

Supported commands:

----------------------------------------------------------------------
INIT
----------------------------------------------------------------------
Usage:
  INIT, name, balance, bank_1, bank_2, ..., bank_n

- Creates a user’s starting balance.
- Values after the balance are the banks the user uses.
- All INIT commands appear before any GET or POST.
- Banks will never share the same name as a user.
- INIT has no output (does not produce a result).

----------------------------------------------------------------------  
POST
----------------------------------------------------------------------
Usage:
  POST, timestamp, sender, receiver, amount

Meaning:
- Sender sends `amount` to receiver at `timestamp`.

Rules:
- If sender’s balance would become negative → return "FAILURE".
- If sender is a bank:
    → treat as deposit to receiver’s Stripe account.
    → receiver must have this bank in their bank list.
- If receiver is a bank:
    → treat as withdrawal from sender’s account.
    → sender must have this bank in their bank list.
- If both sender AND receiver are banks → return "FAILURE".
- If sender or receiver does not exist (no INIT) → "FAILURE".
- Otherwise, return "SUCCESS".

Example:
  POST, 1689800812, Bob, Alice, 50
means Bob sent Alice $50 at timestamp 1689800812.

----------------------------------------------------------------------  
GET
----------------------------------------------------------------------
Usage:
  GET, timestamp, name

Meaning:
- Return the current balance of the user at that timestamp.

Rules:
- If the user does not exist → return "FAILURE".
- Example:
    GET, 2, Alice
  returns Alice’s balance at time 2.

----------------------------------------------------------------------

Input:
- A list of command strings.

Output:
- A comma-separated string of results (in input order), but
  commands must be executed in **chronological** timestamp order.

You may assume all timestamps and commands are properly formatted.

Use this as good practice to create your own test cases.

'''

'''
input: ['INIT, ali, 40, bofa, jpm, wf']
output: results in og order
need to sort by timestamp 

dsa to store: 
{personName: balance, {bank: name}}

init: 
banks don't share same name as user
no output
'''

'''
test case: 
input = ['INIT, ali, 40, bofa, jpm', 'INIT, bob, 30, bofa', 'POST, time, bob, ali, 10', 'GET, time, ali']

'''

'''
notes: 

goal: for users to send money
commands most execute in order based on timestamp

commands: 
INIT
- init user 
- inits always appear before get and post
- no output 

POST
- sender -> to reciever at timestamp
- sender = bank 
    -> add money to balance 
    -> bank in reciever list
- reciever = bank 
    -> minus money from balance 
    -> bank in reciever list

reciever and sender = bank return failture 
not either ^ return failture 
output: success/failture

GET
output: balance of user at timestamp
if not user -> failture

input ex) ["INIT, ali, 40, bofa, jpm", "POST, 1689800812, bofa, ali, 30", "GET, 1689800812, ali"]


structure: 
- process all inits first 
- process gets and posts in the order they came
store user info like this: 
{
    name: {
        balance: amount,
        banks: set()
    },

}
'''
