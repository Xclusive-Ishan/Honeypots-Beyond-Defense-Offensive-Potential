
# Attack-Chain Honeypot Framework
This project explores a novel approach to cybersecurity by deploying compromised honeypot machines that are intentionally designed to be utilized by attackers. Unlike traditional honeypots, which are used to detect and analyze attacks, this project flips the script by allowing attackers to exploit these honeypots, which are then used to target other systems. The project focuses on simulating real-world attack vectors, including HTTP/HTTPS, SSH, SMB, FTP, and DNS, to study attacker behavior and improve detection mechanisms.




## Whats's Naive 
Traditional honeypots are designed to detect and analyze attacks passively. This project takes a proactive approach by creating honeypots that attackers can exploit, thereby revealing new methods of attack and helping us develop more robust defenses. 

By hosting these honeypots in Docker environments, we ensure that attackers remain undetected, simulating real-world scenarios where attribution is nearly impossible.
## Features :

- Multi-Protocol Support: Extends beyond HTTP/HTTPS to include SSH, SMB, FTP, and DNS, enabling a broader range of attack simulations.

        FTP Servers: Flooded with binary files to simulate data exfiltration or disruption.

        SMB: Exploited for file-sharing-based attacks.

        DNS Host: Used to redirect compromised websites and launch DDoS attacks.

- Dynamic VM Hosting:

        OS fingerprinting with fake details.

        Dynamic MAC and IP addresses.

        Reverse DNS spoofing to bypass detection.

- Docker-Based Deployment: Hosted in isolated Docker environments to ensure attacker anonymity and prevent traceability in private networks.

- Log Disruption: Designed to disrupt target system logs with fake results, causing abnormal behavior in detection algorithms.
## Prerequisites
To run this program and take advantage of IP masking, it is recommended to run it in a Docker container. Running in Docker ensures that the attacker/user's IP is not detected in the target logs, thus enhancing privacy. Follow the steps below to set up and run the program in a Dockerized environment:

- Install Docker

If you haven't already installed Docker, you can download and install it from the official website:

    Docker Installation Guide

- System Requirements : 

       The Docker image is built on Python 3.11-slim.   
        Based on your system's resources you may need to adjust the Dockerfile configuration.   

- Building the Docker Image

    1.Clone the repository to your local machine.
    
    2.Open a terminal in the project directory where the Dockerfile is located.

    3.Build the Docker image using the following command:

      docker build -t https-honeypot .
    
    This will create a Docker image named https-honeypot.
    Make sure you dont miss last "dot" in the above command . 
- Running the Docker Container

After successfully building the Docker image, you can initialize and set up the container with specific parameters using the following command:

    docker run -d -p 9000:9000 --name my-honeypot https-honeypot

Here:

    -d runs the container in detached mode.
    -p 9000:9000 maps port 9000 of the container to port 9000 of your machine.
    --name my-honeypot gives your container the name "my-honeypot".
    https-honeypot refers to the image you just built.

- Verify the Container is Running

    To verify if the container is running correctly, use the following command to check its status:

      docker ps

- Testing the Honeypot 

    Access the Honeypot

    Ensure that your mobile device and PC are connected to the same Wi-Fi network, as the Honeypot is hosted in a private environment.
    On your mobile device (or any other device), open a browser and navigate to the following URL:

      https://<private_ip_of_PC>/vulnerable?url=<domain_to_target>

Replace <private_ip_of_PC> with the private IP address of your PC and <domain_to_target> with the target domain.
2. Setting up Netcat for Testing

On your PC, you can test the target using a python server hosted at a specific port (e.g., port 9005). To start the python server, open a separate terminal window and run:

    python http.server 9005

This will start a python listener on port 9005.

On your mobile browser, you will use the following URL:

    https://<private_ip_of_PC>:9000/vulnerable?url=https://<private_ip_of_target_server>:9005

Replace <private_ip_of_target_server> with the private IP address of the target server.

- Note: Since the certificate is self-signed, you may encounter browser warnings. To bypass them, click on the "Advanced" button on the warning page and then click "Proceed to [IP]" or the direct link visible.

- Check the Logs

    To monitor incoming requests to the Honeypot, you can view the logs of the running Docker container with the following command:

      docker logs my-honeypot

- This will show you the incoming requests made by the attacker and their interaction with the Honeypot. You will be able to see a list of 1000 request to the target server, which can be triggered by a single click of the search button from the attacker.

- Utilize Other Honeypots: While this guide focuses on an HTTP/HTTPS Honeypot, you can explore and utilize other types of Honeypots (such as SSH, SMB,FTP etc ) to test various attack vectors. Always follow the  ethical guidelines and ensure proper isolation of the testing environment.
## Designed for :

- Cybersecurity Researchers: To study new attack vectors and improve defensive mechanisms.

- Red Teams: To simulate advanced attack scenarios and test organizational defenses.

- Blue Teams: To understand and develop countermeasures against these unconventional attack methods.

- DevOps and Security Engineers: To explore the implications of containerized environments in attack scenarios.
## Applications :

- New Attack Vector Identification: By allowing attackers to utilize compromised honeypots, this project uncovers previously unknown attack vectors that can disrupt traditional detection systems.

- Improved Detection Mechanisms: The insights gained from this project can help refine intrusion detection systems (IDS) and security algorithms to better handle these advanced threats.

- Log Manipulation: Demonstrates how attackers can manipulate logs to create false positives or negatives, forcing security systems to behave abnormally.

- Private Network Testing: Highlights the risks of undetected attacks in private networks, emphasizing the need for enhanced monitoring and detection in such environments.
## Future Scope 
While the current implementation focuses on HTTP/HTTPS, SSH, SMB, FTP, and DNS, the framework can be extended to include additional protocols and attack vectors. The project also opens the door to further research into dynamic VM hosting, log manipulation, and advanced fingerprinting techniques.
## Author

- [@Xclusive-Ishan](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential.git)




## Results 

- ## Http/Https-Honeypot

![Conatiner set up and Ready](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential/blob/main/docker_container.png)

![dcoker is running and server is hosted](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential/blob/main/container_is_running_and_server_is_hosted.png)

![Dos started](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential/blob/main/dos_started.png)

![1000 fire at single point - DOS done - imapcxted system perfomance ](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential/blob/main/dos_1000request_done.png) <br><br>

- ## Ftp-Honeypot
![attacker_device](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential/blob/main/ftp-honeypot/attacker_device.jpeg)
![both_ftp_server_started](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential/blob/main/ftp-honeypot/both_ftp_server_started.png)
![honeypot_used_for_attack_logs](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential/blob/main/ftp-honeypot/honeypot_used_for_attack_logs.png)
![target_logs](https://github.com/Xclusive-Ishan/Honeypots-Beyond-Defense-Offensive-Potential/blob/main/ftp-honeypot/target_logs.png)

## Guildelines
- Ethical Use Only: The Honeypot is for ethical security research. Do not use it for malicious purposes such as unauthorized access or exploitation.
- Respect Privacy: Ensure you have explicit permission before deploying the Honeypot on any system or network. Avoid violating privacy or security.
- Educational Purposes: This tool is designed for educational and research purposes to understand vulnerabilities, not for launching attacks.
- Use in Controlled Environments: Run the Honeypot in isolated environments (e.g., Docker) to prevent any impact on production systems.
- Comply with Laws: Ensure your actions comply with local, national, and international cybersecurity laws and data protection regulations.
- No Malicious Intent: Do not use the Honeypot for illegal activities such as hacking or unauthorized data collection.
