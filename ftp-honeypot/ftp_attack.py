# modules required for hosting compromised ftp honeypot
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
import os

# this will define the logs and its format in ftp_honeypot.log file as - timestamp  message/command by attacker
logging.basicConfig(filename='ftp_honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class MaliciousFtpHandler(FTPHandler):
    def on_file_received(self, file):
        # Log file uploads
        logging.info(f"File uploaded: {file} by {self.username}")
        self.fire_file_towards_target(file)

    def fire_file_towards_target(self, file):
        # Read target FTP server configuration
        config = self.read_target_config()
        target_host = config["FTP_TARGET_HOST"]
        target_port = int(config["FTP_TARGET_PORT"])  # Convert port to integer
        target_user = config["FTP_TARGET_USER"]
        target_password = config["FTP_TARGET_PASSWORD"]
        target_dir = config["FTP_TARGET_DIR"]

        from ftplib import FTP
        try:
            # Connect to the target FTP server
            ftp = FTP()
            logging.info(f"Connecting to target FTP server at {target_host}:{target_port}...")
            ftp.connect(target_host, target_port)
            logging.info(f"Logged in to target FTP server as {target_user}.")
            ftp.login(target_user, target_password)
            ftp.cwd(target_dir)

            # Upload the file to the target server
            with open(file, 'rb') as f:
                logging.info(f"Uploading file: {file} to {target_host}:{target_port}...")
                ftp.storbinary(f'STOR {os.path.basename(file)}', f)
            ftp.quit()
            logging.info(f"File {file} successfully delivered to target FTP server at {target_host}:{target_port}.")
        except Exception as e:
            logging.error(f"Failed to deliver file to target FTP server: {e}")

    def read_target_config(self):
        # Read the target FTP server configuration from config.txt
        config = {}
        with open("config.txt", "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                config[key] = value
        return config

# Set up the FTP honeypot
def set_my_host_ftp_server_and_attack():
    authorizer = DummyAuthorizer()
    # Define the user "attacker" with full permissions
    authorizer.add_user('attacker', 'password', "./attacker_ftp_root", perm='elradfmw')

    handler = MaliciousFtpHandler
    handler.authorizer = authorizer
    server = FTPServer(('0.0.0.0', 2121), handler)
    print("FTP honeypot started on ftp://0.0.0.0:2121")
    server.serve_forever()

if __name__ == '__main__':
    # Create the FTP root directory if it doesn't exist
    if not os.path.exists("./ftp_root"):
        os.makedirs("./ftp_root")
    
    # Start the FTP honeypot
    set_my_host_ftp_server_and_attack()