# Project Demo Video

https://psu.zoom.us/rec/share/3yZLFQ8mFpGMDoqAWNybdSdz5jGrTIgj4XGMTLT5a4_2GVeGr5NHEP-wBTogujn6.0zIJyEPJZo1krOIX

#   🎓 Unified Academic Support Platform for Online Universities 

###  🧭 Project Overview
This project presents a software design solution for improving how students at online universities access academic support services such as tutoring, advising, and mentoring. The design is based on Object-Oriented Analysis and Design (OOAD), domain modeling, and industry design patterns to produce a maintainable, scalable system.

###  📌 Problem Statement
Online university students often face difficulty accessing academic help due to support services being scattered across various platforms. This leads to missed opportunities, confusion, and low engagement. The proposed solution is a unified academic support platform that brings all academic help services into one consistent and easy-to-use system.

### 🎯  Project Goals

*  Apply OOAD principles to model the problem effectively.

*  Use domain-driven design to identify key entities and their relationships.

*  Apply design patterns and best practices for reusability and modularity.

*  Provide complete UML diagrams and documentation, without code-level implementation.


### 📂  Repository Structure

AcademicSupportPlatform/

├── README.md – Project overview and documentation

├── Images – All UML diagrams and architecture visuals

│ ├── use_case_diagram.png

│ ├── domain_model.png

│ ├── class_diagram.png

│ ├── sequence_diagram.png

│ ├── state_diagram.png

│ ├── activity_diagram.png

│ ├── component_diagram.png

│ └── deployment_diagram.png

├── Scripts – Skeleton classes and pseudocode

│ ├── classes_and_methods.py

│ └── database_schema.sql

├── PowerPoint – Final presentation slides

│ └── Final_Presentation.pptx

└── Word – Project documentation

│ ├── Problem_Statement.docx

│ ├── Design_Explanation.docx




### 📘  Design Artifacts and Explanations

1.  UML Use Case Diagram
Visualizes the interactions between users (students, tutors, faculty) and the system functions such as session booking and feedback.

2. UML Domain Model
Defines the main objects such as Student, Tutor, Session, and Feedback, along with their relationships.

3.  UML Class Diagram
Describes the internal structure of classes, their attributes, methods, and how they interact.

4.  UML Sequence Diagrams
Show the sequence of messages between objects during key use cases like booking or canceling a session.

5.  UML State Diagram
Displays the lifecycle of a Session object with transitions such as scheduled, in progress, completed, and canceled.

6.  UML Activity Diagram (Swimlane)
Illustrates the flow of actions for processes like submitting feedback, assigning each role its responsibilities.

7.  UML Component Diagram
Presents a high-level view of system modules such as Authentication, Session Management, Notification, etc.

8.  UML Cloud Deployment Diagram
Illustrates deployment architecture on platforms like AWS, showing how frontend, backend, and external services integrate.

### 📐 Skeleton Classes and Tables

- Classes are defined using object-oriented principles with proper abstraction and encapsulation.
- Tables outline database schemas including fields for `Users`, `Sessions`, `Feedback`, etc.
- Relationships (1-to-many, many-to-many) modeled using appropriate keys.


### 🧠 Design Patterns & Principles

#### GRASP & SOLID Principles Applied:
- **Controller** and **Information Expert** for managing use cases
- **Single Responsibility** and **Open/Closed** principles in class structure

#### GOF Design Patterns:
- **Factory** Pattern to instantiate user roles (Student, Tutor, Faculty)
- **Singleton** for managing system-wide session scheduler
- **Observer** for real-time updates and notifications

#### Architecture Pattern:
- **Layered Architecture (MVC)**: Separation of concerns between UI, business logic, and data layer.
- Future support for **Microservices** and **Serverless Components** on cloud platforms like AWS or Azure.


### 📊 Non-Functional Requirements

- **Scalability**: Handle 10,000+ users simultaneously
- **Performance**: Sub-2-second response times
- **Security**: Role-based access, secure authentication, data encryption
- **Maintainability**: Modular code, unit tests, version control, CI/CD

###  📌 Note
This project focuses on *design*, not implementation. No coding is required or included beyond structural pseudocode and class skeletons.

  
