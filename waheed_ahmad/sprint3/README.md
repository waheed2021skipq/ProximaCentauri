<div id="top"></div>

<h3 align="center">SPRINT3 PROEJECT SKIPQ</h3>

  <p align="center">
    This project is to create public CRUD api gateway to read/write update the target list
    <br />

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Usage</a></l1>
    <li><a href="#contact">Contact</a></li>
    </li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

CRUD stands for Create, Read, Update, and Delete. But put more simply, in regards to its use in RESTful APIs, CRUD is the standardized use of HTTP Action Verbs. This means that if you want to create a new record you should be using “POST.” If you are trying to read a record, you should be using “GET.” To update a record utilizing “PUT” or “PATCH.” And to delete a record, using “DELETE.”
 `waheed2021skipq`, `ProximaCentauri`




### built-with

* [aws amazon](https://aws.amazon.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You need to goto amazon aws webiste 'https://aws.amazon.com/' and sign up with a IAM user account, 
set up an environment with your required specifications and get started with aws command line interface.



### Prerequisites


* npm
  ```sh
  npm install npm@latest -g
  ```
 * aws latest version
 * for linux
  ```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
  ```
* for windows
    ``` 
    msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
    ```
* Python latest version
  ``` 
  python --version
  ```
### Installation

1. goto aws.amazon.com
2. Clone the repo
   ```
   sh
   git clone 'your repo '
   ```
3. Install NPM packages
   ```
   sh
   npm install
   ```
4. Create api gateway 
  ```
  Create api "https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway.html" as reference
  ```
 
5. Add testing 
  ```
  add testing (unit,integrations) by following reference "https://docs.aws.amazon.com/cdk/api/v1/python/modules.html"
  ```

6. Try CRUD operations
  ```
  "GET, POST,PUT etc"
  ```
  
7. Deploy
   ```
   Use cdk deploy 'name' to deploy the pipeline
   ```
  
## Note
Always git push to make the changes work through pipeline




<!-- USAGE EXAMPLES -->
## Usage


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] S3 to dynamoDB
- [] Implement Crud commands on dynamoDB
- [] Testing stages
    - [] Unit testing
    - [] Integration testing
- [] Documentation












<!-- CONTACT -->
## Contact

Waheed - [https://twitter.com/BetaOokay]

Project Link: [https://github.com/waheed2021skipq/ProximaCentauri](https://github.com/waheed2021skipq/ProximaCentauri)

<p align="right">(<a href="#top">back to top</a>)</p>



## References

[https://docs.aws.amazon.com/cdk/api/v1/python/modules.html]
[https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway.html]







