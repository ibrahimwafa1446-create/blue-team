
log_tokens = "Aug 12 10:06:01 sshd[1234]: Failed password for " \
"guest from 192.0.2.15 port 22 ssh2".split()
Month, Day, Time, Host, *Message_ports = log_tokens

print(f"[PARSED] Date: {Month} {Day} {Time}, Host: {Host}")
print(f"[MESSAGE]: {' '.join(Message_ports)}")
