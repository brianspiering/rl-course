<center><h2>Topics in Artificial Intelligence: Reinforcement Learning <br> University of San Francisco's MSDS 631-01 Summer 2021</h2></center>

<center><img src="https://imgs.xkcd.com/comics/progeny.png" style="width: 40%"/></center>

----
Course Description
----

This course will cover techniques in applied Reinforcement Learning (RL). Reinforcement Learning is one the most successful subdomains within Artificial Intelligence (AI). The fundamental idea in Reinforcement Learning is - agents learn to take successful actions within an environment. 

Reinforcement Learning extends the usefulness of Machine Learning into new domains, such as video games, board games, and robotics. The course will focus on contemporary, practical applications of Reinforcement Learning. 

Topics will include fundamental Reinforcement Learning algorithms, such as multi-arm bandits and q-learning, and Deep Reinforcement Learning. 

This course is part of the [MS in Data Science program at the University of San Francisco](https://www.usfca.edu/arts-sciences/graduate-programs/data-science).

----
Logistics
----

__Instructor:__ Brian Spiering   
__Contact__: [Slack @BrianSpiering](https://msan-usf.slack.com/messages/DAMAXHTL5) (more preferred) | [bspiering@usfca.edu](mailto:bspiering@usfca.edu) (less preferred)  
__Office hours__:  TBD| By Appointment. Link on Canvas in Syllabus section.  

__Website__: [github.com/brianspiering/
rl-course](https://github.com/brianspiering/rl-course)    
__Communication__: Slack [`#msds621_reinforcement_learning_2021`](https://msan-usf.slack.com/archives/C010GN8CQ3W)  
__Section__: TBD  
__Location__: Classes will be held online. Link on Canvas in Zoom section.

Prerequisite Knowledge
----

- Working knowledge of probability, statistics, machine learning, and deep learning.
- Intermediate level of Python (e.g., ability to create to classes).

Learning Outcomes
----

By the end of the course, you should be able to:  

1. Apply Reinforcement Learning techniques to solve complex, applied problems.
1. Define and identify examples of common Reinforcement Learning terms (e.g., agent, environment, state, and rewards).
1. Implement common Reinforcement Learning techniques (e.g., multi-arm bandits and q-learning) from scratch.
1. Create end-to-end Deep Reinforcement Learning applications.

----
Tentative Course Schedule
----

1.  (XX/XX) Welcome ∧ Intro to RL ∧ Markov Decision Processes (MDP) 
2.  (XX/XX) Policy ∧ Value Iteration
3.  (XX/XX) Multi-armed Bandits for AB testing
4.  (XX/XX) Contextual Bandits for Recommendation Systems
5.  (XX/XX) Dynamic Programming ∧ Monte Carlo ∧ Temporal Difference
6.  (XX/XX) Q-Learning
7.  (XX/XX) Value Function Approximation ∧ Deep Learning (DL) Refresher
8.  (XX/XX) Deep Reinforcement Learning (DRL) ^ Deep Q-learning
9.  (XX/XX) Deep Reinforcement Learning Applications
10. (XX/XX) Proximal Policy Optimization (PPO)
11. (XX/XX) Alpha Go 
12. (XX/XX) Future of RL ∧ Student's Choice

The Deep Learning section will be in [Keras](https://www.tensorflow.org/guide/keras).

This course is not a [complete survey of RL methods](http://louiskirsch.com/assets/posts/map-reinforcement-learning/methods.svg).

Topics Not Covered
-----

- Artificial General Intelligence (AGI)
- “Good Old Fashioned AI”, aka expert / ruled-based systems
- Cutting-edge research 
- General discrete and continuous space search / optimization
- Game Theory, including minimax
- Psychology
- Neuroscience
- Genetic algorithms
- Simulated annealing
- Robotics
- Multiple agents

----
Textbooks
----

1. Reinforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto. The standard textbook for RL [pdf](http://incompleteideas.net/book/bookdraft2017nov5.pdf)
1. Algorithms for Reinforcement Learning by Csaba Szepesvari. A delightful walk-through of the most common RL algorithms [pdf](https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf)
1. [Artificial Intelligence: A Modern Approach 4ᵗʰ Edition](https://www.amazon.com/Artificial-Intelligence-A-Modern-Approach/dp/0134610997/) by Stewart Russell and Peter Norvig. Should be published on May 8, 2020.
 
----
Grading
----

| Item           | Weight   |
|:---------------|:--------:|
| Prework Check  | 10%      |
| Participation  | 10%      |
| Exam           | 20%      |
| Labs           | 30%      |
| Final Project  | 30%      |
| __Total__      | __100%__ |

Each item's contribution is capped its respective percentage. The total course percentage is capped at 100%.

Currently, there is no extra credit. If there is any extra credit, it entirely at the discretion of the instructor.

We'll be using Canvas as the learning management system (LMS), aka gradebook. The current canvas course is [here](https://usfca.instructure.com/courses/1593428).The instructional team will do their best to have Canvas accurately reflect your current scores in the course. However, Canvas may not 100% accurate all the time. In other words, your actual grade maybe significant different than it appears on Canvas. 

### Participation

I try to create an active learning environment in my classroom, which is incentivized with the _Participation_ grade. Attendance is mandatory, you can't participate if you don't attend. It is the responsibility of the student to attend all classes. If you have to miss class, due to sickness, job interviewing, or other circumstances, please notify your instructor by Slack in advance. Supporting documents (e.g., doctor’s notes) may be asked for to accompany absences.

Tardiness negatively impacts an active learning environment, thus will impact your participation grade.

You must show up to each session prepared. Each person is important to the dynamic of the class, and therefore students are required to participate in class activities. Expect to be "cold called". I call on students at random not to put you on the spot but to keep you engaged in the material at all times.

I expect you to be fully present and engaged at all times.  

I except you follow the [etiquette guidelines](https://github.com/brianspiering/teaching_materials/blob/master/online_class_etiquette_guidelines.md) throughout the entire course. This is your warning. Every violation will result in a loss of participation points, negatively impacting your total grade. 

### Auditing Policy

If you are a current MSDS student, you are welcome to audit any or all classes without my explicit permission. 

If you are not a current MSDS student, you are also welcome to enroll this course. Please email for permission [bspiering@usfca.edu](mailto:bspiering@usfca.edu).

If you are auditing, your work will not be graded.

### Prework Check

There will be a required prework __before__ each class. The prework will check that you have watch the videos, read the reading, and are prepared for the in-class activities. The prework check also allows be to get a sense for the current  understanding of the class. I know which material I can skim/skip and which material to over in greater detail.

The prework will be online in Canvas.

### Exam

The single exam will be a take-home exam. The exam will be released on XX-XX-21 at the end of class and due XX-XX-21 8p.

### Labs

The labs will be hands-on activities. The focus will be implementing algorithms from scratch or applying common libraries.

| Lab                      | Due Date & Time|
|:-------------------------|:--------------:|
| 1. Tower of Hanoi        | XX-XX-21 6p|
| 2. Grid World            | XX-XX-21 6p|
| 3. Pyramid Escape        | XX-XX-21 6p|
| 4. Tic, Tac, Toe         | XX-XX-21 6p|
| 5. Basket Catch          | XX-XX-21 6p|
| 6. Cart Pole             | XX-XX-21 6p|

Late assignments will only be accepted for medical emergencies.

### Final Project 

In lieu of a Final Exam, there will be a Final Project. The Final Project will be implement a Reinforcement Learning solution for a __novel__ task. By novel, I mean a task that has no existing Reinforcement Learning solutions. The task could be game, dataset, or business problem.

Details and due dates are in Final Project Folder.

----
Grading standards
----

The MSDS program considers a grade of "A" to represent exceptional work with respect to both the instructor's expectations and peer student achievements. I consider an "A" grade to be above and beyond what most students achieve. A grade of "B" represents the expected outcome, what is called "competence" in a business setting. A "C" grade represents achievements lower than the instructor's expectations for competence in the subject. A grade of "F" represents little or no work in the course.

Students with disabilities
-----

If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact [USF Student Disability Services](https://myusf.usfca.edu/sds) (SDS) for information about accommodations.

Behavioral Expectations
----

All students are expected to behave in accordance with the [Student Conduct Code](https://myusf.usfca.edu/fogcutter) and other University policies.

Academic Integrity
-----

USF upholds the standards of honesty and integrity from all members of the academic community. All students are expected to know and adhere to the University's [Honor Code](https://myusf.usfca.edu/academic-integrity/).

You may not copy code from other current or previous students. All suspicious activity will be investigated and, if warranted, passed to the Dean of Sciences for action.  Copying answers or code from other students or sources during a quiz, exam, or for a project is a violation of the university’s honor code and will be treated as such. Plagiarism consists of copying material from any source and passing off that material as your own original work. Plagiarism is plagiarism: it does not matter if the source being copied is on the Internet, from a book or textbook, or from quizzes or problem sets written up by other students. Giving code or showing code to another student is also considered a violation. You must also abide by the copyright laws of the United States.

The golden rule: **You must never represent another person’s work as your own.** Credit to [Terence Parr](https://github.com/parrt/msds689).

I generously post all my materials to a public GitHub repo. However, you should not post any solutions to GitHub (or anywhere else on the Internet). __Publicly posting any solutions to any problems for this course will result in a failing grade for this course.__

If you ever have questions about what constitutes plagiarism, cheating, or academic dishonesty in my course, please feel free to ask me.

Counseling and Psychological Services (CAPS)
-----

CAPS provides confidential, free [counseling](https://myusf.usfca.edu/student-health-safety/caps) to student members of our community.

Confidentiality, Mandatory Reporting, and Sexual Assault
-------

For information and resources regarding sexual misconduct or assault visit the [Title IX](https://myusf.usfca.edu/TITLE-IX) coordinator or USF's [Callisto website](http://usfca.callistocampus.org/).
