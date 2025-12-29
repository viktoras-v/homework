FROM ubuntu:24.04

# Avoid interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Install OpenSSH Server
RUN apt-get update && apt-get install -y --no-install-recommends \
    openssh-server \
    sudo \
    python3.12 \
    && rm -rf /var/lib/apt/lists/*

# Create SSH directory
RUN mkdir /var/run/sshd

# Create a non-root user for SSH
RUN useradd -m -s /bin/bash ansible
RUN echo "ansible:ansible" | chpasswd

# (Optional security) Allow password authentication
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Allow root login ONLY if you uncomment this
# RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config

RUN usermod -aG sudo ansible
RUN mkdir -p /etc/sudoers.d/
RUN echo "ansible ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ansible
RUN chmod 440 /etc/sudoers.d/ansible
RUN mkdir -p /home/ansible/.ssh/
COPY id_ed25519.pub /home/ansible/.ssh/authorized_keys
RUN chown -R ansible:ansible /home/ansible/.ssh
RUN chmod 700 /home/ansible/.ssh
RUN chmod 600 /home/ansible/.ssh/authorized_keys


# Expose SSH port
EXPOSE 22

# Start SSH server in foreground
CMD ["/usr/sbin/sshd", "-D"]
