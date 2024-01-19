#include <iostream>
using namespace std;
struct Node {
int marks;
Node* prev;
Node* next;
};
void insertMarks(Node*& head, int marks, int position) {
Node* newNode = new Node;
newNode->marks = marks;
if (position == 1) {
newNode->prev = nullptr;
newNode->next = head;
if (head != nullptr) {
head->prev = newNode;
}
head = newNode;
} else {
Node* current = head;
int currentPosition = 1;
while (currentPosition < position - 1 && current != nullptr) {
current = current->next;
currentPosition++;
}
if (current == nullptr) {
cout << "Invalid position. Marks not inserted." << endl;
delete newNode;
return;
}
newNode->prev = current;
newNode->next = current->next;
if (current->next != nullptr) {
current->next->prev = newNode;
}
current->next = newNode;
}
}
void displayMarks(Node* head) {
if (head == nullptr) {
cout << "List is empty." << endl;
return;
}

Node* current = head;
while (current != nullptr) {
cout << current->marks << " ";
current = current->next;
}
cout << endl;
}

int main() {
Node* head = nullptr;
int numStudents = 8; 
for (int i = 0; i < numStudents; i++) {
int marks;
cout << "Enter the marks for student " << i + 1 << ": ";
cin >> marks;
insertMarks(head, marks, i + 1);
}
int missingStudentMarks;
cout << "Enter the marks for the missing student: ";
cin >> missingStudentMarks;
insertMarks(head, missingStudentMarks, 3);

cout << "Final list of marks: ";
displayMarks(head);

return 0;
}