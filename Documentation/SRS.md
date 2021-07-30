
#### Department
##### Display list of department
This mode is intended for viewing and editing the departments list 

___Main scenario:___ 
* User selects item “Departments”; 
* Application displays list of department. 

![1](https://user-images.githubusercontent.com/65542353/127387862-ace08915-3504-4c30-b775-319e18a02409.png)

The list displays the following columns: 
* Department name – departament name; 
* Average salary – Average wages of employees; 


##### Add department
___Main scenario:___ 
* User clicks the “Add” button in the department list view mode; 
* Application displays form to enter department data; 
* User enters department data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed; 
* If entered data is valid, then record is adding to database; 
* If error occurs, then error message is displaying; 

![adderr](https://user-images.githubusercontent.com/65542353/127623054-bbb46552-5e15-42a8-9fc1-4cd6db64c6dd.png)

* If new department record is successfully added, then list of department with added records is displaying. 
Cancel operation scenario: 
* User clicks the “Add” button in the department list view mode;
* Application displays form to enter department data; 
* User enters department data and presses “Cancel” button;
* Data don’t save in data base, then list of department records is displaying to user. 
* If the user selects the menu item ”Department” or "Employee", the data will not be saved to the database and the corresponding form with updated data will be opened. 

![2](https://user-images.githubusercontent.com/65542353/127388666-6bee0a67-c101-4f5c-a217-d147a66aa396.png)

When adding a department, the following details are entered: 
* Name department – departament name; 

Constraints for data validation:

* Name department – maximum length of 30 characters; 
* Average salary- maximum length of 5 characters; . 
 ##### Edit department
___Main scenario:___ 
* User clicks the “Edit” button in the department list view mode; 
* Application displays form to enter department data;
* User enters department data and presses “Save” button; 
* If any data is entered incorrectly, incorrect data messages are displayed; 
* If entered data is valid, then edited data is added to database; 
* If error occurs, then error message is displaying; 

![editerr](https://user-images.githubusercontent.com/65542353/127623114-dfcbe175-3ad4-457f-b636-5ee2f2a22282.png)

* If the departments record is successfully edited, the list of departments with the added records is displayed and the data in the "depatments" table is changed.

![редактировать](https://user-images.githubusercontent.com/65542353/127388771-dee34b02-ea34-49c5-9511-cdb05d5894e1.png)

If the user selects the menu item ”Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.


##### Removing the department
___Main scenario:___ 
* The user, while in the list of departments mode, presses the "Delete" button in the selected department line; 
* Application displays confirmation dialog “Please confirm delete department?”; 
* The user confirms the removal of the department;
* The user confirms the removal of employees of this department; 
* Record is deleted from database; 
* If error occurs, then error message displays; 

![err](https://user-images.githubusercontent.com/65542353/127623171-73bc29b8-388f-4d7b-ac23-aa9d82a2664b.png)

* If a department record is successfully deleted, a list of departments with no deleted records is displayed and employees with the deleted department are deleted.

![удалить](https://user-images.githubusercontent.com/65542353/127388802-c8d1113f-3bb6-4fa5-b2ad-f5633a0da100.png)

___Cancel operation scenario:___
* User is in display mode of departments list and press “Delete”,“Edit”, “Add” button; 
* The application displays the selected window; 
* User press “Cancel” button; 
* List of departments without changes is displaying. 



One of the site feature is managing employee resourses. This feature will take "employees" tab in main menu. The following tab requires big table for 
describing every employee and button "add" - for adding new eployees.  

On the following picture situated eployee's tab:  

![image](https://user-images.githubusercontent.com/83345134/127285130-2928a7fa-dd6e-4b84-a077-ff80b723aa25.png "Employees list")


By clicking green button user will add new employee. To add new employee user should write down his department, some personal data and his salary.
Then user should press green button "save" to store this data in database.  

![image](https://user-images.githubusercontent.com/83345134/127285174-8b015c12-a1b2-4ff9-a32c-d93a516a4bbb.png "Add employee")

To edit enployee's information the user should double click employee in the table, fill in the required info and press "Yes", otherwise press "Cancel" to return back: 

![image](https://user-images.githubusercontent.com/83345134/127285373-3f14cb74-9510-4dc3-8e3a-2c2c01dee4a4.png "Edit employee")

To delete an employee user should right-click eployee in the table and press delete button. Otherwise, hi will need to press "Cancel" button to return back to employees' list:

![image](https://user-images.githubusercontent.com/83345134/127285318-fc4847d6-ff49-4f51-863a-19ffafd29391.png "Delete employee")

