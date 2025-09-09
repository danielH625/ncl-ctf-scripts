file_handle = open("payments.log", "rt")
all_lines = file_handle.readlines()
file_handle.close()

total_transactions = 0
index = -1
states = []
money = {}

for line in all_lines:
  if "TransactionID" in line:
    total_transactions += 1

for line in all_lines:
  index += 1
  if "currencyID" in line:
    start_index = line.find("USD") + 5
    money[(line[start_index:start_index + 5])] = index
highest_key = max(money)
highest_money_line = money[highest_key]
highest_transactionID_index = highest_money_line + 6

highest_transactionID_line = all_lines[highest_transactionID_index]
start_index = highest_transactionID_line.find("TransactionID") + 14
highest_transactionID = highest_transactionID_line[start_index:start_index +
                                                   36]

for line in all_lines:
  if "StateOrProvince" in line:
    start_index = line.find("StateOrProvince") + 16
    states.append(line[start_index:start_index + 2])
most_common_state = max(states, key=states.count)

print("===============================================================")
print("The amount of transactions in this log is:", total_transactions)
print("===============================================================")
print("The transactionID for the highest purchase is:", highest_transactionID)
print("===============================================================")
print("State that made the most number of purchases:", most_common_state)
print("===============================================================")
