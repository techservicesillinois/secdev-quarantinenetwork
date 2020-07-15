# Clearpass API Postman Collection

This is a collection of calls to the clearpass API used during development of the quarantine API. This file can be imported into Postman. Postman is an API development environment. We are mostly using it to design and test. 

### Prerequisites

- [Postman](#Windows)
- [Quarantine Network Dev environment file](#Quarantine-Network-Dev-environment-file)

### Windows

[Chocolatey](https://chocolatey.org/) is highly recommended for installing prerequisite packages.

[Installing Chocolatey](https://chocolatey.org/docs/installation)

##### After Installing Chocolatey
1. Run the choco command to install Postman. 
    ```
    choco install postman
    ```
### Mac
https://learning.postman.com/docs/postman/launching-postman/installation-and-updates/#installing-postman-on-mac

### Linux
https://learning.postman.com/docs/postman/launching-postman/installation-and-updates/#installing-postman-on-linux

### Importing the collection

1. Clone the repository to a directory of your choice on your machine:

    ```
    > git clone https://github.com/techservicesillinois/secdev-quarantinenetwork.git
    ```

1. Open Postman and choose import
    ![image](https://user-images.githubusercontent.com/4566388/82709416-2aec6280-9c46-11ea-8fae-f197ca728b0f.png)

1. Drag and drop (or click Upload Files and browse to) the /test/postman/ClearPass API.postman_collection.json file in the repo. 

1. Double check the file information and click the import button.

The collection should now appear in the Collections panel on the left. Expand it to see the list of requests.

#### Quarantine Network Dev environment file

- A member of the SecDev team can help you get the dev environment and key imported and set up. 

#### Example

1. Open the ApiAuthentication request and click send. 
    ![image](https://user-images.githubusercontent.com/4566388/83040870-6354bd80-a005-11ea-9211-01e6fd2d2ad3.png)

1. The JSON response should contain an access_token. Add this token to the Quarantine Network dev environment in the bearer_token variable.
    - To edit the Quarantine Network dev environment in Postman, click the eye icon next to the environment drop down. 
    ![image](https://user-images.githubusercontent.com/4566388/83041076-af9ffd80-a005-11ea-99ba-1c816492f942.png)

1. Try another request that uses the bearer token, such as the Role request, which should return a list of available roles. 