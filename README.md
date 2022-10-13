# Security Tool - Fireball v1.0

**Fireball** is a multipurpose command line tool designed for use by both the Offensive and Defensive Security Teams.

Fireball's functionalities include:

- Scanning ports fast and efficiently
- Listening and establishing connection with open ports on a network
- Monitoring and capturing a network traffic in real time (In process).

Below here are some illustrations on the installation and usage of the tool.

## Installation

git clone https://github.com/Nimbusshub/Fireball.git

## Usage

To use the tool, navigate to the terminal and use the following commands:

```bash
cd Fireball
./fireball

```

#### Output

Below is the output that results from runnig the commands above:

```bash
███████╗ ██╗ ██████   ██████  █████╗    ██████   ██  ██
██╔════╝ ██╔═██ ╗██   ██╗     ██╔══██   ██  ██   ██║ ██
███████╗ ██  █████╔   ██████  ██████   ████████  ██║ ██
║██╔═══╝ ██╔═██╗ ██   ██║     ██╔  ═██ ██╔═ ═██  ██║ ██
║██║     ██║ ██║  ██║ ██████║ ██████  ████║║████ ███████████ ║
╚══╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═══════╝  ╚═╝╚═╝╚═╝╚═╝╚═══════════╝


Welcome to fireball shell. Type 'man fireball' to see the usage

<FireB>  exit

Thank you for using fireball
```

Other syntaxes:

- To scan for open ports on an IP address

```
scan {target IP address}
```

- To scan for open ports on a domain name

```
scan {domain name}
```

- To scan specific ports on a target IP or domain name

```
scan {target IP address/domain name}  -p {port(s)}
```

- To listen on a port and establish connection

```
listen -l -p{port number} -c
```

For more information and examples see the Documentation here.

## Contributors

The tool is designed and created by **Nimota Ogunbanjo**, **Purity Njeri**, **Olamiposi Fasina**, **Yemisi Aponjolosun**. You can help make it better by sending bug reports to ogubanjonimotabusayo@gmail.com.
