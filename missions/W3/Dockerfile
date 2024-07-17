FROM ubuntu:jammy

# port for HDFS
EXPOSE 9870
# port for Resource Manager
EXPOSE 8088

# hadoop user
ENV USERNAME=hdoop
ENV USERPASSWORD=hadoop

USER root

# apt update and install
RUN apt update -y && \
    apt upgrade -y && \
    apt install openjdk-8-jdk ssh pdsh -y

RUN service ssh start

RUN useradd ${USERNAME} -m -s /bin/bash -p ${USERPASSWORD}

USER ${USERNAME}
WORKDIR /home/${USERNAME}

RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN chmod 0600 ~/.ssh/authorized_keys

RUN echo "Host *\n\
    StrictHostKeyChecking no" >> ~/.ssh/config
RUN chmod 400 ~/.ssh/config

COPY hadoop-3.4.0-aarch64.tar.gz /home/${USERNAME}/
# RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0-aarch64.tar.gz
RUN tar -xzvf hadoop-3.4.0-aarch64.tar.gz
RUN mv hadoop-3.4.0 hadoop
RUN rm hadoop-3.4.0-aarch64.tar.gz

WORKDIR /home/${USERNAME}/hadoop

RUN echo "export JAVA_HOME=$(readlink -f $(which java) | sed 's/\/bin\/java//g')" >> etc/hadoop/hadoop-env.sh
RUN echo "export PDSH_RCMD_TYPE=ssh" >> etc/hadoop/hadoop-env.sh

# overwrite config files
COPY etc/hadoop/*.xml etc/hadoop

USER root

# RUN bin/hdfs namenode -format
# RUN sbin/start-dfs.sh
# RUN sbin/start-yarn.sh