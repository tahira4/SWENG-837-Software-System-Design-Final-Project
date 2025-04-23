#   🎓 Unified Academic Support Platform for Online Universities ##  🧭 Project Overview
This project presents a software design solution for improving how students at online universities access academic support services such as tutoring, advising, and mentoring. The solution is grounded in Object-Oriented Analysis and Design (OOAD), domain modeling, and established design patterns to create a unified, maintainable, and scalable system.


## 📌 Problem Statement
Online university students often face difficulty accessing academic help due to scattered support services across multiple platforms. This leads to missed opportunities, confusion, and low engagement. The proposed solution is a **unified academic support platform** that streamlines access to tutoring, mentoring, and advising sessions within a single, consistent system interface.


## 🎯 Project Goals
- Apply **OOAD principles** to model the problem and system effectively.
- Use **domain-driven design** to identify key entities and their relationships.
- Leverage **design patterns and best practices** for reusability, modularity, and scalability.
- Deliver a complete set of UML diagrams and design documentation, avoiding implementation-level detail.

---

## 📂 Repository Structure

/AcademicSupportPlatform │ ├── README.md # Project overview and documentation ├── /Images # UML diagrams and architecture visuals │ └── use_case_diagram.png │ └── domain_model.png │ └── class_diagram.png │ └── sequence_diagram.png │ └── state_diagram.png │ └── activity_diagram.png │ └── component_diagram.png │ └── deployment_diagram.png │ ├── /Scripts # Skeleton classes and pseudocode │ └── classes_and_methods.py │ └── database_schema.sql │ ├── /PowerPoint # Final presentation slides │ └── Final_Presentation.pptx │ └── /Word # Project documents └── Problem_Statement.docx └── Design_Explanation.docx


---

## 📘 Design Artifacts and Explanations

### ✅ UML Use Case Diagram
Visualizes the core interactions between actors (students, tutors, faculty) and the system functions like session booking, feedback submission, and availability management.

### ✅ UML Domain Model
Represents key entities like `Student`, `Tutor`, `Session`, and `Feedback`, and their relationships. Captures the core problem domain without focusing on technologies.

### ✅ UML Class Diagram
Converts the domain model into classes with attributes and methods, showcasing object behavior and relationships within the system.

### ✅ UML Sequence Diagrams
Illustrates how objects interact in specific use cases (e.g., "Book a Tutoring Session") with focus on message flow and method calls.

### ✅ UML State Diagram
Demonstrates the lifecycle of a `Session` object as it transitions between states like Scheduled, Completed, or Canceled.

### ✅ UML Activity (Swimlane) Diagram
Depicts a process flow (e.g., “Submit Feedback”) while clearly assigning responsibilities to different actors using swimlanes.

### ✅ UML Component Diagram
Shows the system as a set of components like Authentication, Session Scheduler, and Feedback Processor, emphasizing modularity and dependency.

### ✅ Cloud Deployment Diagram
Illustrates the deployment architecture (e.g., on AWS) including web front-end, backend services, databases, and third-party APIs (e.g., Zoom).

---

## 📐 Skeleton Classes and Tables

- Classes are defined using object-oriented principles with proper abstraction and encapsulation.
- Tables outline database schemas including fields for `Users`, `Sessions`, `Feedback`, etc.
- Relationships (1-to-many, many-to-many) modeled using appropriate keys.

---

## 🧠 Design Patterns & Principles

### GRASP & SOLID Principles Applied:
- **Controller** and **Information Expert** for managing use cases
- **Single Responsibility** and **Open/Closed** principles in class structure

### GOF Design Patterns:
- **Factory** Pattern to instantiate user roles (Student, Tutor, Faculty)
- **Singleton** for managing system-wide session scheduler
- **Observer** for real-time updates and notifications

### Architecture Pattern:
- **Layered Architecture (MVC)**: Separation of concerns between UI, business logic, and data layer.
- Future support for **Microservices** and **Serverless Components** on cloud platforms like AWS or Azure.

---

## 📊 Non-Functional Requirements

- **Scalability**: Handle 10,000+ users simultaneously
- **Performance**: Sub-2-second response times
- **Security**: Role-based access, secure authentication, data encryption
- **Maintainability**: Modular code, unit tests, version control, CI/CD

---

## 🔗 Related Resources and Inspiration

### Sample Projects
- [AWS Samples Repository](https://github.com/aws-samples)
- [Amazon Bedrock Chatbot Example](https://github.com/aws-samples/amazon-bedrock-kendra-lex-chatbot)

### Sample Blogs
- [Deploying Gen-AI QnA with Amazon Bedrock & Lex](https://aws.amazon.com/blogs/machine-learning/deploy-generative-ai-self-service-question-answering-using-the-qnabot-on-aws-solution-powered-by-amazon-lex-with-amazon-kendra-and-amazon-bedrock/)
- [System Design Primer on GitHub](https://github.com/donnemartin/system-design-primer)

---

## 🎥 Video Presentation Guide

A separate 8–16 minute recorded video will:
- Introduce the project and the problem.
- Walk through each diagram using visuals.
- Explain design choices, patterns, and architecture.
- Reflect on lessons learned and how this project enhances software design skills.

---

## 🙋‍♀️ Author
**Name:** Tahira Malik  
**Course:** SWENG 837 – Software System Design  
**Institution:** Penn State]  
**Role:** System Designer & Document Author

---

## 📌 Note
This project focuses on *design*, not implementation. No coding is required or included beyond structural pseudocode and class skeletons.


