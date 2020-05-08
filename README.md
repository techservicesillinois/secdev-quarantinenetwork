# SecDev Quarantine Network

## What is this?
This is the source code for an API allowing management of users that have been placed on the quarantine network. 

## How do I build it?
### Prerequisites
- Docker
- Make

### Windows
[Chocolatey](https://chocolatey.org/) is highly recommended for installing prerequisite packages.

[Installing Chocolatey](https://chocolatey.org/docs/installation)

#### After Installing Chocolatey
1. Run choco commands for any of the tools below if you don't already have them installed. 
    ```
    choco install git
    choco install docker-desktop
    choco install make
    ```
1. Add C:\Program Files\Git\usr\bin to PATH, if it not already.

    Note: If running on Apple, install Brew and then replace `choco` with `brew`. If running on Linux, replace `choco` with `apt-get` or your package manager of choice.

1. Clone the repository to a directory of your choice on your machine:

    ```
    > git clone https://github.com/techservicesillinois/secdev-quarantinenetwork.git
    ``` 

1. Build and run Docker image:
    ```
    > make
    ```
    This should result in a build, including any pip installs, and a running dev server. Once the dev server is running try going to http://localhost:5000/canary. You should get an 'Ok' message.

    Once the image is built you can just run:
    ```
    > make run
    ```
    to start the development server. 

    If you change the Makefile, requirements.in, or Dockerfile run:
    ```
    > make clean
    > make
    ```
    to build the images again. 

    You can also run:
    ```
    > make shell
    ```
    to get a bash shell. 