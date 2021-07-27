 Department
 Display list of department
 This mode is intended for viewing and editing the department list 
Main scenario: 
• User selects item “Department”; 
• Application displays list of department. 

The list displays the following columns: 
• Name department – departament name; 
• Short name of department – short name of deprtament; 
Add department
Main scenario: 
• User clicks the “Add” button in the department list view mode; 
• Application displays form to enter department data; 
• User enters department data and presses “Save” button;
 • If any data is entered incorrectly, incorrect data messages are displayed; 
• If entered data is valid, then record is adding to database; 
• If error occurs, then error message is displaying; 
• If new department record is successfully added, then list of department with added records is displaying. 
Cancel operation scenario: 
• User clicks the “Add” button in the department list view mode;
 • Application displays form to enter department data; 
• User enters department data and presses “Cancel” button;
• Data don’t save in data base, then list of department records is displaying to user. 
• If the user selects the menu item ”Department” or "Employee", the data will not be saved to the database and the corresponding form with updated data will be opened. 

When adding a car, the following details are entered: 
• Name department – departament name; 
• Short name of department – short name of deprtament; 
 Constraints for data validation: 
• Name department – maximum length of 30 characters; 
• Short name of department- unique, maximum length of 10 characters; . 
 Edit department
Main scenario: 
• User clicks the “Edit” button in the department list view mode; 
• Application displays form to enter department data;
 • User enters department data and presses “Save” button; 
• If any data is entered incorrectly, incorrect data messages are displayed; 
• If entered data is valid, then edited data is added to database; 
• If error occurs, then error message is displaying; 
• If the vehicle record is successfully edited, the list of departments with the added records is displayed and the data in the "employees" table is changed.
 Cancel operation scenario: 
• User clicks the “Edit” button in the departments list view mode;
 • Application displays form to enter departmentsdata; 
• User enters car data and presses “Cancel” button; 
• Data don’t save in data base, then list of departments records is displaying to user. 
If the user selects the menu item ”Department” or "Employee", the data will not be saved to the database and the corresponding form with updated data will be opened.

Removing the department
Main scenario: 
• The user, while in the list of departments mode, presses the "Delete" button in the selected department line; 
• Application displays confirmation dialog “Please confirm delete department?”; 
• The user confirms the removal of the department; 
• Record is deleted from database; 
• If error occurs, then error message displays; 
• If a department record is successfully deleted, a list of departments with no deleted records is displayed and employees with the deleted department are deleted.

Cancel operation scenario: 
• User is in display mode of departments list and press “Delete” button; 
• Application displays confirmation dialog “Please confirm delete department?”; 
• User press “Cancel” button; 
• List of departments without changes is displaying. 

