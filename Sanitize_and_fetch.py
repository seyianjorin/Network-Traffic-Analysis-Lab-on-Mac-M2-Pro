import paramiko
import os
from datetime import datetime

# main configurations
ubuntu_ip = "ip address"
ubuntu_user = "ubuntu_username"
ssh_key_path = os.path.expanduser("~/.ssh/id_rsa") # ssh key public/private key path

# creating filename with time stamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"final_conn_{timestamp}.log"
remote_path = f"/home/{ubuntu_user}/{log_filename}"
mac_desktop = os.path.expanduser(f"~/Desktop/{log_filename}")

# sanitizing data
sanitize_cmd = f"""
cd ~
sed -e 's/0\\.0\\.0\\.[0-300]\\+/REDACTED_IP/g' \\
    -e 's/0\\.0\\.1\\.[0-9]\\+/REDACTED_IP/g' \\
    -e 's/f::[0-9a-f:]\\+/REDACTED_IPV6/g' \\
    -e 's/f::[0-9a-f:]\\+/REDACTED_IPV6/g' \\
    -e 's/ubuntu_username/analyst/g' conn.log > {log_filename}
"""

#function to fetch data
def sanitize_and_download():
    print("Connecting to Ubuntu server...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ubuntu_ip, username=ubuntu_user, key_filename=ssh_key_path)

    print("Running sanitize command...")
    stdin, stdout, stderr = ssh.exec_command(sanitize_cmd)
    stdout. channel.recv_exit_status()

    print("Fetching sanitized log file...")
    sftp = ssh.open_sftp()
    sftp.get(remote_path, mac_desktop)

    sftp.close()
    ssh.close()
    print(f"Done! File saved to: {mac_desktop}")

if __name__ == "__main__":
    sanitize_and_download()
