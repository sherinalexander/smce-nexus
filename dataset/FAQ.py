class CollegeQA:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

# Sample college-related questions and answers
college_qa_list = [
    CollegeQA("What programs does the college offer?", 
              "The college offers various undergraduate and graduate programs in fields such as engineering, business, arts, sciences, etc."),
    CollegeQA("What are the admission requirements?", 
              "Admission requirements vary depending on the program and level of study. Generally, applicants need to submit transcripts, standardized test scores, letters of recommendation, and a personal statement."),
    CollegeQA("Is financial aid available?", 
              "Yes, the college offers various forms of financial aid, including scholarships, grants, loans, and work-study programs. Eligibility for financial aid is based on factors such as financial need, academic achievement, and other criteria."),
    CollegeQA("Are there on-campus housing options?", 
              "Yes, the college provides on-campus housing options for students. These include dormitories, apartments, and residential colleges."),
    CollegeQA("What student support services are available?", 
              "The college offers a range of student support services, including academic advising, counseling and mental health services, career services, tutoring, disability support, and more."),
    CollegeQA("What activities does the coding club organize?", 
              "The coding club organizes various activities such as coding competitions, hackathons, workshops, guest lectures by industry professionals, and collaborative coding projects."),
    CollegeQA("How can I join the coding club?",
                "To join the coding club, you can attend one of their meetings or events and sign up for membership. Membership is open to all students who are interested in coding and programming."),
    CollegeQA("What are the benefits of joining the coding club?", 
                "Joining the coding club can help you improve your coding skills, network with other students interested in programming, gain hands-on experience with coding projects, and participate in coding competitions and hackathons."),
    CollegeQA("Who created nexus?",
                "Nexus was created by sherin,aknel,nimisha,d who wanted to provide a platform for sharing information, resources, and opportunities related to coding and programming."),
]

# Function to find answer for a given question
def find_answer(question):
    for qa in college_qa_list:
        if question.lower() in qa.question.lower():
            return qa.answer
    return "Sorry, I couldn't find an answer to that question."

# Function to display questions and answers
def display_college_qa():
    for index, qa in enumerate(college_qa_list, 1):
        print(f"Question {index}: {qa.question}")
        print(f"Answer: {qa.answer}")
        print()

# Display college-related questions and answers
display_college_qa()

# Ask user for input
user_question = input("Ask a question about the college: ")

# Find and display the answer
answer = find_answer(user_question)
print(answer)
