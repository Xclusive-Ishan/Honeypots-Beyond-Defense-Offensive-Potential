# modules required for hosting target FTP server
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
import os

# Set up logging
logging.basicConfig(filename='target_ftp_server.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class LoggingFTPHandler(FTPHandler):
    def on_file_received(self, file):
        # Log file uploads
        logging.info(f"File received: {file} from {self.remote_ip}")
        super().on_file_received(file)

def setup_ftp_server():
    # Create a dummy authorizer for managing users
    authorizer = DummyAuthorizer()
    
    # Add a user with full permissions (adjust as needed)
    authorizer.add_user("user", "passwrd", "./target_ftp_server_root", perm="elradfmw")
    
    # Instantiate the FTP handler
    handler = LoggingFTPHandler
    handler.authorizer = authorizer
    
    # Set up the server
    server = FTPServer(("10.40.0.60", 2122), handler)
    print("Target FTP server started on ftp://10.40.0.60:2122")
    server.serve_forever()

if __name__ == "__main__":
    # Create the FTP root directory if it doesn't exist
    if not os.path.exists("./ftp_server_root"):
        os.makedirs("./ftp_server_root")
    
    # Start the target FTP server
    setup_ftp_server()