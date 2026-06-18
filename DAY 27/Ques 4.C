#include <stdio.h>

int main() {
    char name[50];
        int rollNo;
            float marks[5], total = 0, percentage;
                char grade;

                    printf("Enter Student Name: ");
                        scanf("%s", name);

                            printf("Enter Roll Number: ");
                                scanf("%d", &rollNo);

                                    printf("Enter marks for 5 subjects:\n");
                                        for (int i = 0; i < 5; i++) {
                                                printf("Subject %d: ", i + 1);
                                                        scanf("%f", &marks[i]);
                                                                total += marks[i];
                                                                    }

                                                                        percentage = total / 5;

                                                                            // Grade Calculation
                                                                                if (percentage >= 90)
                                                                                        grade = 'A';
                                                                                            else if (percentage >= 80)
                                                                                                    grade = 'B';
                                                                                                        else if (percentage >= 70)
                                                                                                                grade = 'C';
                                                                                                                    else if (percentage >= 60)
                                                                                                                            grade = 'D';
                                                                                                                                else
                                                                                                                                        grade = 'F';

                                                                                                                                            // Display Marksheet
                                                                                                                                                printf("\n====================================\n");
                                                                                                                                                    printf("           MARKSHEET\n");
                                                                                                                                                        printf("====================================\n");
                                                                                                                                                            printf("Name      : %s\n", name);
                                                                                                                                                                printf("Roll No   : %d\n", rollNo);

                                                                                                                                                                    for (int i = 0; i < 5; i++) {
                                                                                                                                                                            printf("Subject %d : %.2f\n", i + 1, marks[i]);
                                                                                                                                                                                }

                                                                                                                                                                                    printf("------------------------------------\n");
                                                                                                                                                                                        printf("Total Marks : %.2f / 500\n", total);
                                                                                                                                                                                            printf("Percentage  : %.2f%%\n", percentage);
                                                                                                                                                                                                printf("Grade       : %c\n", grade);
                                                                                                                                                                                                    printf("====================================\n");

                                                                                                                                                                                                        return 0;
                                                                                                                                                                                                        }