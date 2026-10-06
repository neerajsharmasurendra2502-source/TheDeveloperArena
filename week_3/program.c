#include <stdio.h>
int main()
{
 char name[50], rollno[20], school[100];
 int hindi, phy, chem, maths, eng, total;
 float percentage;
 printf("Enter Student Name: ");
 scanf(" %[^\n]", name);
 printf("Enter Roll Number: ");
 scanf("%s", rollno);
 printf("Enter School Name: ");
 scanf(" %[^\n]", school);
 printf("Enter marks in Hindi: ");
 scanf("%d", &hindi);
 printf("Enter marks in English: ");
 scanf("%d", &eng);
 printf("Enter marks in Physics: ");
 scanf("%d", &phy);
 printf("Enter marks in Chemistry: ");
 scanf("%d", &chem);
 printf("Enter marks in Mathematics: ");
 scanf("%d", &maths);
 total = hindi + phy + chem + maths + eng;
 percentage = total / 5.0;
 printf("\n\n");
 printf("====================================================\n");
 printf("       CENTRAL BOARD OF SECONDARY EDUCATION\n");
 printf("           SENIOR SCHOOL CERTIFICATE\n");
 printf("              EXAMINATION - 2026\n");
 printf("====================================================\n");
 printf("School Name : %s\n", school);
 printf("Roll Number : %s\n", rollno);
 printf("Student Name: %s\n", name);
 printf("----------------------------------------------------\n");
 printf(" Subject        Maximum Marks         Marks Obtained\n");
 printf("----------------------------------------------------\n");
 printf(" Hindi                 100                 %d\n", hindi);
 printf(" English               100                 %d\n", eng);
 printf(" Physics               100                 %d\n", phy);
 printf(" Chemistry             100                 %d\n", chem);
 printf(" Mathematics           100                 %d\n", maths);
 printf("----------------------------------------------------\n");
 printf(" Total Marks: %d / 500\n", total);
 printf(" Percentage : %.2f%%\n", percentage);
 if (percentage >= 33)
 printf(" Result    : PASS\n");
 else
 printf(" Result    : FAIL\n");
 printf("====================================================\n");
 printf("           *** MARK SHEET ***\n");
 printf("====================================================\n");
 return 0;
}