# HindSight
> Hindsight is a comprehensive finance application designed to empower users in managing their financial portfolios efficiently. Hindsight was created by a team of six eager individuals named Sean Skaugen, Rose Ochoa, Daria Bilash, Adrash Ram, Maria Renee, and Dhruve Mistry. With Hindsight, users can create personalized accounts to track various financial assets, including stocks, savings accounts, and other pertinent financial information.
The core of the mission is to provide all of our users with the access to tools to help make informed decisions with their financial resources. We will do this by providing users with actionable insights and intuitive interfaces, we aspire to empower individuals to take charge of thier finacial well-being and build a more secure future for themselves and thier familes. Join Hindsight and embark on the journey towards financial independence.

Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [The Team](#the-team)
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Sprint 1](#sprint-1)
* [Spring 2](#sprint-2)
* [Contributions](#contributions)
* [Screenshots](#screenshots)
* [Usage](#usage)
* [Project Status](#project-status)
* [Contact](#contact)
<!-- * [License](#license) -->

## The Team
- Rose Ochoa
- Sean Skaugen 
- Daria Bilash 
- Adarsh Ram 
- Dhruve Mistry 
- Maria Renee 


## General Information
![project icon](HindSight_logo.png)
- Enhance financial management by utilizing customized accounts to monitor assets.
- The issue we intend to solve is the lack of financial resources available to young people.
- The purpose of our project is to create an easy and accessible platform for trading stocks.
- We undertook this project because we are passionate about increasing financial literacy and empowering the youth.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- [Visual Studios Code](https://code.visualstudio.com/docs/getstarted/userinterface) 
- [polygon.io_API](https://polygon.io/) 
- [finhub.io_API](https://finnhub.io/)
- [GitKraken](https://www.gitkraken.com/) 
- [BitBucket](https://bitbucket.org/product/guides/getting-started/overview#a-brief-overview-of-bitbucket) 
- [Jira](https://www.atlassian.com/software/jira/guides/getting-started/introduction#what-is-jira-software) 
- [Python_11.5](https://www.python.org/) 
- [Terminal](https://en.wikipedia.org/wiki/Command-line_interface)  
- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5) 
- [CSS3](https://www.tutorialspoint.com/css/css3_tutorial.htm) 
- [SQL_Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- [SQL_Alchemy]
- [SQL_Lite]
- [Azure]
- [pypyodbc]


## Features
- Landing Page: The landing page is an eye-catching and organized page for the user to see when they open the web app. On it there is a personal greeting, a navigation bar and some recent trending stocks. The user will be able to scroll and click on buttons on the navigation bar. User Story: Build Landing Page Display.

- Log in Page: The user will be able to log in or create an account. There will be buttons for the user to do this. User Story: Build Landing Page Display. 

- Navigation System: A footer navigation system with buttons that allows the user to go from the landing page to the log-in page. User Story: Build Landing Page Display. 

- User Credentials: User log in tied through unique key in database. User Story: User Registration.

- Implement API request handling: Review polygon documentation and create the http request to acquire data. User Story: Grab Pricing Info From API.

- Database Setup and Management: Set up, design, and manage a relational database system to store educational resources, metadata, and user interactions, implement tasks such as data migration, backups, and performance tuning. User Story: Educational Resource Help Desk.

- Design UI Mockups: Use a tool like Adobe XD or Figma to make models of the user interface. User Story: User Interface.

- Unit Testing for API Request Handling and Database Integration: Test API request handling code for various scenarios and database integration accuracy using pytest for Python and SQLUnit for SQL. User Story: Grab Pricing Info From API User Story.


## Sprint 1 (Feburary 19 - March 1)
![Sprint1](Sprint1.png)

### Retrospective

What went well and what did not?

- Team: 
    - We have our project running locally, as expected. 
    - We fixed all bugs before the demo date.
    - Everyone who had no prior experience in frontend and backend tasks learned and accomplished what was designated to them. 
    - When it came to merging everything most of it was seamless and everyone communicated efficiently to merge their work together.

- Rose: Time could have been directed more towards features.

- Daria: We divided responsibilities into frontend and backend sub teams. 

- Maria Renee: The front end code went well and the communication between me and Daria was very good. We were able to easily merge our branches together and merge the front end with the back end functionality. I think the communication with the back end team could have been better, and we could have done more work if we had communicated better.

- Dhruve: Backend and frontend did not communicate effectively and tasks were too broad. 

- Sean: We lacked communication as we created too specialized groups which resulted in a lack of cohesion which was seen in a subpar demo after the first sprint. 

- Adarsh: The frontend made the page presentable and functional. 


- What Might Be Impeding Us from Performing Better?
    - We have not implemented any feature directly related to our project.
    - We rarely meet outside the class.


- What Can I do to Improve?
    - Rose: Practice good time management to get more features done. 

    - Daria: Actively seek feedback from team members and use their suggestions to improve collaboration, specifically focusing on features related to our project. My team and instructor will observe this improvement through more effective participation in team meetings and clearer articulation of ideas.

    - Sean: I can do better at actively communicating with my group. I plan on making at least three communications with my team outside of class to facilitate this goal.

    - Dhruve: Communicate more with teammates from the frontend. 

    - Maria Renee : In the future I will be a more active communicator and make clearer tasks and story points so that we can organize the tasks better so that we can get more things done.

    - Adarsh: Communicate efficiently to both backend and frontend. 




### Next Sprint 
- Dhruve: 
    - Link Database to server
    - Verify email and password reset option
- Rose: 
    - Add chatbots to learn page 
    - News Curator tab 
- Maria: 
    - Make the features look presentable
    - Manage their account
- Daria: 
    - Implement Youtube videos on Learning Page
- Sean: 
    - Link APIs to features
    - Stock Comparison Tools
- Adarsh: 
    - Net Worth Calculator 


### Contributions

### Rose Ochoa: Researched python, what server to use, and SQL. Worked on the user credentials security and functionality.
#### Jira Task SCRUM-36: User Credentials
- **Jira Link:** [SCRUM-36](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-36?atlOrigin=eyJpIjoiNGY5ZTE5ZDYwZTUwNDM1ZGI0YWFlNWYzYzg3YTVmODkiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-36-user-credentials)

#### Jira Task SCRUM-55: User Credentials: Email
- **Jira Link:** [SCRUM-55](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-36?atlOrigin=eyJpIjoiNTJjN2VhZTJjYjA3NDk0OGJiMjdmYWQ3ODM1Y2M5NGQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-36-user-credentials)

#### Jira Task SCRUM-53: Fix Login SQLite
- **Jira Link:** [SCRUM-53](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-53?atlOrigin=eyJpIjoiYTNiNjRhYTQyNDZiNDcwNWJiN2JhODliYzdlNTQyMWQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-36-user-credentials)

#### Jira Task SCRUM-45: Research Python 
- **Jira Link:** [SCRUM-45](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-45?atlOrigin=eyJpIjoiYWZlNmU5MTQ1ZmMzNDY2MThkMDVkODFjMDBkMGQ4N2UiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-45-research-python)

#### Jira Task SCRUM-44: Research What SQL Server to use
- **Jira Link:** [SCRUM-44](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-44?atlOrigin=eyJpIjoiZjk5MTY2N2FkODM4NDM2YmEzOGNjNTgzNTFiY2VkNWMiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-44-research-what-sql-server-to-use)

#### Jira Task SCRUM-47: Research SQL
- **Jira Link:** [SCRUM-47](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-47?atlOrigin=eyJpIjoiNWE4M2RhMTBlNzgxNGU1NTkxMGJmNDZmOGYyOTQ4NjYiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-47-research-sql)


### Daria Bilash: Created a general layout for the website, worked on design and layout of the registration page, structured routes.
#### Jira Task SCRUM-26: Set up Flask Project
- **Jira Link:** [SCRUM-26](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-26?atlOrigin=eyJpIjoiY2ZlMWU1MTdlNjQzNDI4ZjkwYzM2NjJiMDQwNDhjZjIiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH]( https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/pull-requests/new?source=SCRUM-26-set-up-flask-project)

#### Jira Task SCRUM-27: Design a registration page
- **Jira Link:** [SCRUM-27](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-27?atlOrigin=eyJpIjoiZjIyMDMwODcyYTBmNGI4MGJkOTk2ZGYwMGRhZDc0YzUiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/pull-requests/new?source=SCRUM-27-design-a-registration-page)

#### Jira Task SCRUM-28: Format overall layout
- **Jira Link:** [SCRUM-28](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-28?atlOrigin=eyJpIjoiNjFmN2I4MjU5OWE2NGU5MjkzNDA5YTJlOTUxNTliNzciLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/pull-requests/new?source=SCRUM-28-format-overall-layout)

#### Jira Task SCRUM-49: Research Flask
- **Jira Link:** [SCRUM-49](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-49?atlOrigin=eyJpIjoiZDVmMzA1ZTAzNGM0NDdlM2I5MzVlNTJiOGZjMjY4ZTUiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/pull-requests/new?source=SCRUM-49-research-flask)


### Sean Skaugen: Created graphs from data pulled from various APIs. Also created data parsing functions to obtain data insights
#### Jira Task SCRUM-5: Design API Request Handling for Recommendation Feature
- **Jira Link:** [SCRUM-5](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-5?atlOrigin=eyJpIjoiY2ZkNWU5YzVjYTQ4NDRjYzhmYjQyMjM3MmYyMzk3YzEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/%7B%7D/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-5-design-api-request-handling)

#### Jira Task SCRUM-52: Create data parsing function
- **Jira Link:** [SCRUM-52](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-52?atlOrigin=eyJpIjoiZTg4ZmRiODQ0ZjM1NGEyNmJlNDJjYjE0NTEwYTVlNjkiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/%7B%7D/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-52-create-data-parsing-function)

#### Jira Task SCRUM-57: Research plotting stock data with plotly
- **Jira Link:** [SCRUM-57](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-57?atlOrigin=eyJpIjoiN2IyNzdjMDMzNDU2NGFhMDhjZTUxOTlhM2YyMjE4NzIiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/%7B%7D/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-57-research-plotting-stock-data-wi)


### Adarsh Ram: Research and development of UI components, including navigation bars, buttons, panels, and menus, with focus on modifying HTML for Flask-based applications.
#### Jira Task SCRUM-30: Learning and Researching UI Components (Navigation Bar, Buttons, Panels, and menus)
- **Jira Link:** [SCRUM-30](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-30?atlOrigin=eyJpIjoiMmM3ZDM0NzU4OTZkNGNiNGI4NzdlZDllNTIyOGE2ZTUiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-30-learning-and-researching-ui-com)

#### Jira Task SCRUM-48: HTML Training & Research Flask
- **Jira Link:** [SCRUM-48](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-48?atlOrigin=eyJpIjoiYjZiZGZhNmI3ZTA4NDcxMGE5OTYzMTZjYmQ4NGEwOGMiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-48-research-react-and-flask)

#### Jira Task SCRUM-17: Create login page CSS file layout
- **Jira Link:** [SCRUM-17](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-17?atlOrigin=eyJpIjoiNjRmMTJhZTI2N2RhNDYzNWFhZTgwNTljMzAwOGRmMWEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-17-create-login-page-css-file-layo)

#### Jira Task SCRUM-18: Modify Login HTML link to CSS
- **Jira Link:** [SCRUM-18](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-18?atlOrigin=eyJpIjoiMDUwOWM4ZTUxMTM3NDVhNWJkNjhlZWNiZTNlNmU1MmEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-18-modify-login-html-link-to-css)


### Dhruve Mistry: Created template backend login and registration and added local and remote database functionally.
#### Jira Task SCRUM-24: Create simple terminology definitions
- **Jira Link:** [SCRUM-24](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-60?atlOrigin=eyJpIjoiZTRmYmJjMmNkN2Y1NDJiOGIzN2I0ZTFlYmQ5YzBlNjQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](COMMIT_LINK)

#### Jira Task SCRUM-33: Database Setup and Management
- **Jira Link:** [SCRUM-33](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-33?atlOrigin=eyJpIjoiMzlkMmIzYTJhOWYyNGMyYTgzOTY1MzkyNWI1OTg0NmMiLCJwIjoiaiJ99)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-33-database-setup-and-management)

#### Jira Task SCRUM-56: Requirements.txt
- **Jira Link:** [SCRUM-56](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-56?atlOrigin=eyJpIjoiMzEyYTZiZGVkZDFkNGNjOWIyMTljMzQwY2E3YjhjNzQiLCJwIjoiaiJ9)
- **Reference Commit:** [No COMMIT_HASH as always being updated]()

#### Jira Task SCRUM-54: Backend Create Login Page
- **Jira Link:** [SCRUM-54](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-56?atlOrigin=eyJpIjoiMzEyYTZiZGVkZDFkNGNjOWIyMTljMzQwY2E3YjhjNzQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/hindsightwebapp/branch/create-registration-page-db?dest=Development) 


### Maria Renee San Esteban: Designed UI and implemented UI designs using CSS/HTML for both the landing and login page. Researched stock information visualization and tested graph integration into HTML.
#### Jira Task SCRUM-14: Design UI Mockups
- **Jira Link:** [SCRUM-14](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-14?atlOrigin=eyJpIjoiNjQ1YTc3MTdhMmFjNGM1YzhjMmM2MDYzODc3ZmVkOTQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/hindsightwebapp/branch/SCRUM-14-design-ui-mockups)

#### Jira Task SCRUM-15: Modify login.css based on UI mockups
- **Jira Link:** [SCRUM-15](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-15?atlOrigin=eyJpIjoiMjRjMjYxYzQ0NTQ1NDA4OGFhY2YwNDZiODNkZjg4ZmEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-29-landing-page-css-and-design)

#### Jira Task SCRUM-42: Create Landing Page
- **Jira Link:** [SCRUM-42](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-42?atlOrigin=eyJpIjoiZGZhNzBhMjg1ZDUyNGVhMTgzMmY3MTE2ZmQzN2VhMjMiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](COMMIT_LINK)

#### Jira Task SCRUM-29: Landing page CSS and design
- **Jira Link:** [SCRUM-29](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-29?atlOrigin=eyJpIjoiZWFlZGEzMzVkNmFhNDNjY2IzY2Q0NjE2ZTI0NTYyYjgiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/hindsightwebapp/branch/SCRUM-29-landing-page-css-and-design)

#### Jira Task SCRUM-46: Research plotting stock data and plotly
- **Jira Link:** [SCRUM-46](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-46?atlOrigin=eyJpIjoiOTgwNmE3YjAyMWU3NDMyNGJlMzg0MzE0ZTMxNzFiOTQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/hindsightwebapp/branch/SCRUM-46-research-plotting-stock-data-an)

#### Jira Task SCRUM-59: Research plotting stock data and plotly
- **Jira Link:** [SCRUM-59](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-59?atlOrigin=eyJpIjoiNDc1YWNlMjJlYTU5NGUxYmE1OWQ5MjIxMGMyNzZjMmMiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/hindsightwebapp/branch/SCRUM-59-testing-graph-and-api-data-with)


## Sprint 2 (March 25 - April 5)
![Sprint2](Sprint2.png)

### Retrospective
For this sprint, our primary tasks were to implement key features for our project, including a quiz tab, a shorts page, a forum, and a personalized profile page with an experience and rank system. Also, we aimed to connect to a Microsoft SQL Server database rather than having our database working locally.
- What went well and what did not?
    - Team: 
        - We implemented various features that were ready to be presented at the demo.
        - We were able to resolve all merge conflicts that appeared during pull requests.
        - Our directory structure needs an immediate restructuring since our app.py file currently contains lots of functionalities including routes, models, configurations, forms, etc.
        - We still need to figure out how to deploy our project.
    - Team Members:
        - Rose: Each team member worked on their own feature so that by the end of the Sprint we had plenty of features to present.

        - Daria: All team members were able to connect to a SQL server database.

        - Maria Renee: We were able to implement features that provide a personalized user experience.

        - Dhruve: There was a lot more communication this sprint which overall improved the project.

        - Sean: We incorporated several APIs in our features.

        - Adarsh: We had almost no overlap between each other's tasks so that each team member could work on their task independently. 

- What Might Be Impeding Us from Performing Better?
    - Finishing tasks that may affect others’ work in a timely manner.
    - Distributing tasks evenly and communicating about overall vision for the final product.
    - Not having a weekly time to meet consistently. Normally it's just 2 or 3 of us availible.

- What Can I do to Improve?
    - Rose: Start working on tasks as soon as a sprint starts.

    - Daria: Document my code so that everyone who reads the code later, including me, can figure out what is going on.

    - Sean: I can imporve by communicating more effectively with my group. This can be done by having a mini stand up once or twice a week on discord or after class.

    - Dhruve: Vision alignment, taking the time to understand the project's overall vision and goals.

    - Maria Renee: Document my code better and work in a more timeley manner. Do work consistenly throughout entire sprint.

    - Adarsh: Stay more consistent with doing tasks rather that holding off until days before; communicate a little more with team members.

### Next Sprint 

- Dhruve: 
    - Get the chatbot to reply differently based off skill levels
    - Add more features to the chatbot
    - Start building a user profile that links to the database and functions correctly
    - Allow the database to work with the quizzes
- Rose: 
    - Connect more features to the experience points
    - Add fill in the empty space in the profile page
- Maria: 
    - Add flash cards and quizzes for studying on the learn tab
    - Award user expirience based on time spent learning
    - Provide additional recourses for learning
    - Improve overall UI
- Daria: 
    - Finish implementing profile page features
    - Provide feedback to a user with the flashing system
- Sean: 
    - Make more templates for the shorts page
    - Improve the UI of the welcome page
- Adarsh: 
    - Connect the community forum page to the database
    - Add additional small post fearures for the users

### Contributions

### Daria Bilash: Implemented a profile page with all its functionalities that work with cloud database, including picture upload, displaying user’s info, changing username, resetting a password, and generating username during the signup process.
#### Jira Task SCRUM-73: Add a profile picture
- **Jira Link:** [SCRUM-73](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-73?atlOrigin=eyJpIjoiZTA4YmY5NzJkYmZiNDYxYWFjMmNlMWY0YTEyMjI5ZTAiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-73-add-suggestion-for-username)

#### Jira Task SCRUM-75: Password Reset
- **Jira Link:** [SCRUM-75](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-75?atlOrigin=eyJpIjoiMDk4M2NhYjdkNjhiNDBhNTgzNGNmNDAxOWE1M2RkMDciLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-75-password-reset)

#### Jira Task SCRUM-76: Change Username
- **Jira Link:** [SCRUM-76](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-76?atlOrigin=eyJpIjoiMGRkZWZiMWE0MTEwNDk3OWJhM2FmMzg1MzZkZGFkY2UiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-76-change-username)

#### Jira Task SCRUM-77: Add a profile picture
- **Jira Link:** [SCRUM-77](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-77?atlOrigin=eyJpIjoiZTljMjM3NzcyNTM1NDJiNmFlMzM1N2ZkYjA4MjZiOTYiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-77-add-a-profile-picture)

#### Jira Task SCRUM-95: Create Profile Page
- **Jira Link:** [SCRUM-95](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-95?atlOrigin=eyJpIjoiYTU5NjgyZjJkNmZhNDA5YWI1MTZiYzg2OTMxMTBjYzIiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-95-create-profile-page)


### Rose Ochoa: Set up an experience tracking system, including how users gain experience with visual symbols for different ranks and a progress bar on user profiles to display experience levels.
#### Jira Task SCRUM-83: Create Experience Variable
- **Jira Link:** [SCRUM-83](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-83?atlOrigin=eyJpIjoiOTg3M2YyNTM4YjdkNDljMjgwMjljOTc4ZDk1ZTAyODYiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-83-create-experience-variable)

#### Jira Task SCRUM-84: Determine Experience Gain Mechanism
- **Jira Link:** [SCRUM-84](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-84?atlOrigin=eyJpIjoiYjZhNDJkYmY1YjZiNDhhYmJhNGRmMDM5NmQxOTExOWYiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-84-determine-experience-gain-mecha)

#### Jira Task SCRUM-85: Add symbols to rank
- **Jira Link:** [SCRUM-85](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-85?atlOrigin=eyJpIjoiOGJmZjk3MGVjNjJmNDU2ZDg0NmFiYWE1ODQ2YjZmOTAiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-85-add-symbols-to-rank)

#### Jira Task SCRUM-86: Define Rank Thresholds
- **Jira Link:** [SCRUM-86](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-86?atlOrigin=eyJpIjoiNjVhMDY3ZDZmNGE4NGVjNmI2OWM1ZTZmY2U1NjIwMzgiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-86-define-rank-thresholds)

#### Jira Task SCRUM-87: Implement experience bar on profile
- **Jira Link:** [SCRUM-87](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-87?atlOrigin=eyJpIjoiNjZmNjI2MDNkOTkyNDYyMTgwNDcxMDRmZDI0YzkwNGUiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-87-implement-experience-bar-on-pro)


### Sean Skaugen: Developed Shorts Tab that includes moderation for user prompts, sending openAPI responses to a video API, retrieving and playing videos from the API in a Shorts Tab.
#### Jira Task SCRUM-62: Create front end for initial user prompt
- **Jira Link:** [SCRUM-62](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-62?atlOrigin=eyJpIjoiMzQyOWFkOTg5ZjhhNGQxMzhmMDQ1YTkyM2Y0YmFjYmEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-62-send-user-response-to-open-ai-a)

#### Jira Task SCRUM-63: Add moderation to user prompt
- **Jira Link:** [SCRUM-63](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-63?atlOrigin=eyJpIjoiNDQ4NWRiMzYyN2UxNDZlM2EyYTE3YmVjMjBkMWJiOGQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-63-add-moderation-to-user-prompt)

#### Jira Task SCRUM-64: Send openAPI response to video API
- **Jira Link:** [SCRUM-64](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-64?atlOrigin=eyJpIjoiMTMwZjNjM2RiNmE5NGMyNzllMGVmZjkwMTQxNzU2ZTciLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-64-send-openapi-response-to-video-)

#### Jira Task SCRUM-65: Retrieve video from API and play in Shorts Tab
- **Jira Link:** [SCRUM-65](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-65?atlOrigin=eyJpIjoiNGQzNThkZDgxYjY2NDUwZDhiZGM2ODJkYWI5NGEyN2YiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-65-retrieve-video-from-api-and-pla-real)

#### Jira Task SCRUM-66: Get User Prompt
- **Jira Link:** [SCRUM-66](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-66?atlOrigin=eyJpIjoiM2Y2YTdmYWI4Mzc3NGM0MWFkYWQxMjcxZTg4MjBkOTEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-66-add-route-and-tab-to-website)

#### Jira Task SCRUM-67: Create Aesthetic UI for short tab
- **Jira Link:** [SCRUM-67](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-67?atlOrigin=eyJpIjoiM2VlMTI4NmU0ZWVkNGQ2ZWE2NGQ4NmQ1NTNhZGUwMjAiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-67-create-aesthetic-ui-for-short-t)


### Adarsh Ram: Worked on a forum platform that has like functionality and displaying recent posts, adding a comment feature, and configuring the user interface for the forum.
#### Jira Task SCRUM-88: Create the Forum Platform
- **Jira Link:** [SCRUM-88](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-88?atlOrigin=eyJpIjoiMTI1NjQ1ODcxMDkzNGJiOThmOGExMTQ4NTljMTFlOGQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-88-create-the-forum-platform)

#### Jira Task SCRUM-89: Research Flask Forum Layout
- **Jira Link:** [SCRUM-89](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-89?atlOrigin=eyJpIjoiZGUxNjc3ZmEzZDhkNDgzN2JiYWZhZmE2YTk0NjBhOWQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/4f900819780b4955984af502b19bbc2296ba574e)

#### Jira Task SCRUM-90: Like Functionality and Recent Posts
- **Jira Link:** [SCRUM-90](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-90?atlOrigin=eyJpIjoiNDgyYjY0ZmM4ZjIzNDZlYmI1MGQ5ZjA2ZGVlYjQ5MDYiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-90-like-functionality-and-recent-p)

#### Jira Task SCRUM-91: Add comment feature and functionality
- **Jira Link:** [SCRUM-91](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-91?atlOrigin=eyJpIjoiMTJjYmM3ZjFiYjU2NGJjZjllNTExMDQxZDA5M2QwOTEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-91-add-comment-feature-and-functio)

#### Jira Task SCRUM-92: Forum ui configuration
- **Jira Link:** [SCRUM-92](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-92?atlOrigin=eyJpIjoiNjI4MWU2NDFjZTdmNDU0MGJmYTRjOTJkNWNiMGFiMmYiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-92-flask-forum-ui-configuration)


### Dhruve Mistry: Integrated a chatbot into the website, determining the frontend location for the chatbot. Also, resolved issues with the database server.
#### Jira Task SCRUM-93 Fix Database Server
- **Jira Link:** [SCRUM-93](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-93)
- **Reference Commit:** N/A as this was on Microsoft Azure portal.

#### Jira Task SCRUM-71 Chatbot Frontend
- **Jira Link:** [SCRUM-93](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-71?atlOrigin=eyJpIjoiOTExMzAxOTIxYzlmNDdhMDlhMTgxNmQ4M2EwMzBlZDEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-71-chatbot-frontend-location)

#### Jira Task SCRUM-68 Chatbot Backend
- **Jira Link:** [SCRUM-68](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-68?atlOrigin=eyJpIjoiMGZlMzc2MzFkZjczNDVkOWJhMzk0MWQwZjdhNDVkYWUiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-68-integrate-chatbot-into-our-webs)

#### Jira Task SCRUM-69 Ensure Conversational Flow
- **Jira Link:** [SCRUM-69](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-69?atlOrigin=eyJpIjoiMjczMTg2YzJjYjk3NDhiMmJiN2MwNTM4YjJkYTRkOTIiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-68-integrate-chatbot-into-our-webs)


### Maria Renee San Esteban: Implemented a quiz with JSON questions bank, connecting quiz results to user accounts by awarding experience points and implementing skill level buttons, adding a flag for quizzes, fixing and adding routes for quiz page.
#### Jira Task SCRUM-78: Quiz Questions
- **Jira Link:** [SCRUM-78](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-78?atlOrigin=eyJpIjoiOGMyYTFhNDVjMDBkNDU3NTg1ZDg4NTU4NWYxN2NkYTUiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-78-quiz-questions)

#### Jira Task SCRUM-79: Functional Quiz Questions and results
- **Jira Link:** [SCRUM-79](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-79?atlOrigin=eyJpIjoiNzcyNGUzYTkwMmE4NGI3MzkyN2RkOTY3NGE1NmJhOTQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-79-question-format)

#### Jira Task SCRUM-80: Connect Quiz results to User account by awarding xp and add functionality to set skill level buttons
- **Jira Link:** [SCRUM-80](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-80?atlOrigin=eyJpIjoiYzA3NjNmYjAyZDdmNDcyMzg3MDU4YmU1NzEzYTA0ZDQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-80-connect-quiz-results-to-user-ac)

#### Jira Task SCRUM-81: Add flag for quiz, fix/add routes for quiz/learn html pages and add learn content
- **Jira Link:** [SCRUM-81](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-81?atlOrigin=eyJpIjoiYWZmMzBmN2M1MDVjNGU2Yjk1ZjhhZTJmOTE0OTYwYTkiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/SCRUM-81-add-flag-for-quiz-fix-add-route)

#### Jira Task SCRUM-82: Quiz Option or Manual Selection
- **Jira Link:** [SCRUM-82](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-82?atlOrigin=eyJpIjoiZWVlYzkzOGJmYTc5NGFiYmEwZTU0NzcwMjZlOTYwMjEiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/branch/feature/SCRUM-82-quiz-option-or-manual-selection)


## Sprint 3 (April 12 - April 22)
![Sprint3](Sprint3.png)

### Dhruve Mistry
#### Jira Task SCRUM-127 Create Unit Test
- **Jira Link:** [SCRUM-127](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-127?atlOrigin=eyJpIjoiYTg1NWM0MThhZmJjNDM2ZmE0NGM5YjAwMjZiNzlhNmUiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/7f51d593dc513c60beb688aabe82d72032312ca1)

#### Jira Task SCRUM-124 Response based off user level
- **Jira Link** [SCRUM-124](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-124?atlOrigin=eyJpIjoiMGQ2YTYyNmU2ZTA5NDJmNWE5ZTczMTYwMDI2MDQzZGYiLCJwIjoiaiJ9)
- **Reference Commmit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/eab4eea651983adb71eb3ec8a4367f7e264ef59a)

#### Jira Task SCRUM-134 Chatbot Working on Every Page
- **Jira Link:** [SCRUM-134](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-134?atlOrigin=eyJpIjoiMDAwY2ZhM2FkZDU4NGFkYjkyMDJiYWE0Y2VhNDIzMGIiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/8e71c2dac2efd42b5a95afc774060cef83513863)

#### Jira Task SCRUM-135 Refine Chatbot UI
- **Jira Link:** [SCRUM-135](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-135?atlOrigin=eyJpIjoiY2JjY2NiZTEzNTM4NDE5YjgyZjNkMWIzNWQzYjRiNzQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/8e71c2dac2efd42b5a95afc774060cef83513863) *Same commit as SCRUM-134, both coincided*

#### Jira Task SCRUM-125 Flashcard Schema
- **Jira Link:** [SCRUM-125](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-125?atlOrigin=eyJpIjoiY2IyNWI5YmRkOTc0NDgwZGE4Njc4OGIzYmEzMDZhNTYiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/bb2f590af21c0d353665ea2af6da59a28f8c168f)

#### Jira Task SCRUM-133 Member since stored on database
- **Jira Link:** [SCRUM-133](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-133?atlOrigin=eyJpIjoiY2RkNTJiYjkzZTU5NDE5NGExNDQyNjU0Yjk4NDViNjgiLCJwIjoiaiJ9)
- **Reference Commit:** No commit hash as it was on Azure portal. Check Jira for SQL command.


### Adarsh Ram
#### Jira Task SCRUM-117: Dislike posts function
- **Jira Link:** [SCRUM-117](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-117?atlOrigin=eyJpIjoiNzFhNDE4NmU0YzE0NGNhZGE4MDllZmI2ZGNjMTk4YjMiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/55a80f0aab948afbdfb79118202518d6a80d0270)
#### Jira Task SCRUM-105: Create timestamp for posts
- **Jira Link:** [SCRUM-105](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-105?atlOrigin=eyJpIjoiNDg4MGUxMzY5YzRlNDNlNDhlZjgwNzhlNDBlM2ZmZTYiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/a769e29d187d206fc9716fd1fd469605b586f123)
#### Jira Task SCRUM-119: Display profile picture to posts
- **Jira Link:** [SCRUM-119](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-119?atlOrigin=eyJpIjoiNzA2YjFhODEzMTBlNDE2MmE5ZTEyZDcxN2ZlMmMxYmQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/%7Becfc5013-4c18-4935-a7ed-c74c1aee4caa%7D/commits/abc6aa71286b0451db16f71252f31ff7e285e95f)
#### Jira Task SCRUM-102: Fixing community forum bugs
- **Jira Link:** [SCRUM-119](https://cs3398s24cardassians.atlassian.net/browse/SCRUM-102?atlOrigin=eyJpIjoiZWEzNjc0MDczNWExNGYxNmJjODhkNTFlOTBjZTA2NDQiLCJwIjoiaiJ9)
- **Reference Commit:** [COMMIT_HASH](https://bitbucket.org/cs3398s24cardassians/hindsightwebapp/commits/a0e0474a85ed365f0bc273727385fbab77d3425c)

## Screenshots

### Sprint 3
![Website_Home](Homepage.png)

### Sprint 1
![Website_Home](Screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Usage
Install required dependencies
`pip install -r requirements.txt`

Run the server using
`pip3 runserver.py` or `flask run`


## Project Status
Project is: _in progress_ .


## Contact
- Rose Ochoa rmo44@txstate.edu
- Sean Skaugen qrt16@txstate.edu
- Daria Bilash wnw23@txstate.edu
- Adarsh Ram cho11@txstate.edu
- Dhruve Mistry d_m704@txstate.edu
- Maria Renee ytm8@txstate.edu



<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->