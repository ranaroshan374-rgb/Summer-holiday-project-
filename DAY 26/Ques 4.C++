#include <iostream>
using namespace std;

int main() {
    int score = 0, answer;

        cout << "===== Welcome to the Quiz =====\n";

            // Question 1
                cout << "\n1. What is the capital of India?\n";
                    cout << "1. Mumbai\n2. New Delhi\n3. Kolkata\n4. Chennai\n";
                        cout << "Enter your answer: ";
                            cin >> answer;

                                if (answer == 2)
                                        score++;

                                            // Question 2
                                                cout << "\n2. Which language is used for C++ programming?\n";
                                                    cout << "1. Markup Language\n2. Query Language\n3. Programming Language\n4. Styling Language\n";
                                                        cout << "Enter your answer: ";
                                                            cin >> answer;

                                                                if (answer == 3)
                                                                        score++;

                                                                            // Question 3
                                                                                cout << "\n3. How many days are there in a leap year?\n";
                                                                                    cout << "1. 365\n2. 364\n3. 366\n4. 367\n";
                                                                                        cout << "Enter your answer: ";
                                                                                            cin >> answer;

                                                                                                if (answer == 3)
                                                                                                        score++;

                                                                                                            // Result
                                                                                                                cout << "\n===== Quiz Result =====\n";
                                                                                                                    cout << "Your Score: " << score << "/3\n";

                                                                                                                        if (score == 3)
                                                                                                                                cout << "Excellent!\n";
                                                                                                                                    else if (score >= 2)
                                                                                                                                            cout << "Good Job!\n";
                                                                                                                                                else
                                                                                                                                                        cout << "Keep Practicing!\n";

                                                                                                                                                            return 0;
                                                                                                                                                            }