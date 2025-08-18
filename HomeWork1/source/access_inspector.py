with open('./HomeWork1/data/sample_data.log','r') as R:
    log_file_lines = R.readlines()

total_requests = 0
for line in log_file_lines:
    total_requests += 1
    print(line[0])

print("== Totals ==")
print("total requests = " + str(total_requests))
