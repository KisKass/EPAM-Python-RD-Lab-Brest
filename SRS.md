2. Employees  
  2.1. Display list of Employees  
    This mode is intended for viewing and editing the employees list.  
    Main scenario:
      1. User selects item "Employees";
      2. Application dispalys list of employees.

    ![image](https://user-images.githubusercontent.com/83345134/127285130-2928a7fa-dd6e-4b84-a077-ff80b723aa25.png "Employees list")  
    Pic 2.1 View the employees list.  
  
    The list displays following employees' information:  
      1. Department - place, where employee is working;
      2. Name of the employee;
      3. Date of birth of the employee;
      4. Employee's salary.  
    
    Filtering by date:  
      1. In the employees list view mode, the user sets a date filter and presses the refresh list button (to the right of the date entry field);  
      2. The application will show the employees only for a certain period of time.  

    Restrictions:  
       Start date of the period should be less then end date of the period;  
       If start date is blank, then filtering by end date only.  
       If end date is blank, then filtering by start date only.  
       Updating data after selecting the filtering conditions is carried out by pressing the “Refresh” button.  
    2.2. Add employee  
    Main scenario:  
       User clicks the “Add” button in the employees list view mode;  
       Application displays form to enter employee data;  
       User enters employee’s data and presses “Save” button;  
       If any data is entered incorrectly, incorrect data messages are displayed;  
       If entered data is valid, then record is adding to database;  
       If error occurs, then error message is displaying;
       If new employee record is successfully added, then list of employees with added records is displaying.  
    Cancel operation scenario:  
       User clicks the “Add” button in the employees list view mode;  
       Application displays form to enter employee’s data;  
       User enters employee’s data and presses “Cancel” button;  
       Data don’t save in database, then list of employees' records is displaying to user.  
       If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and         the corresponding form with updated data will be opened.  
    ![image](https://user-images.githubusercontent.com/83345134/127285174-8b015c12-a1b2-4ff9-a32c-d93a516a4bbb.png "Add employee")  
      Pic 2.2 Add employee.
  
    When adding a employee, the following details are entered:  
       Department – employee’s work place;  
       Name – employee’s name;  
       Salary – employee’s salary;  
       Date of birth – employee’s date of birth.  
  
    Constraints for data validation:  
       Department – one of the departments;  
       Name –  maximum length of 45 characters;  
       Salary – maximum value is 2000;  
       Date of birth – date in format dd/mm/yyyy.  

  2.3 Edit employee
    Main scenario:  
       User clicks the “Edit” button in the employees list view mode;  
       Application displays form to enter employee data;  
       User enters cemployee’s data and presses “Save” button;  
       If any data is entered incorrectly, incorrect data messages are displayed;  
       If entered data is valid, then edited data is added to database;  
       If error occurs, then error message is displaying;  
       If employee’s record is successfully edited, then list of employees with added records is displaying.
    Cancel operation scenario:
       User clicks the “Edit” button in the employees list view mode;  
       Application displays form to enter employee data;
       User enters employee data and presses “Cancel” button;  
       Data don’t save in database, then list of employees records is displaying to user.  
       If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and         the corresponding form with updated data will be opened.  
![image](https://user-images.githubusercontent.com/83345134/127285373-3f14cb74-9510-4dc3-8e3a-2c2c01dee4a4.png "Edit employee")
    Pic. 2.3 Edit employee.  
    
  2.4 Removing employee
    Main scenario:
       The user, while in the list of employees mode, presses the "Delete" button in the selected employee line;  
       Application displays confirmation dialog “Please confirm delete employee?”;  
       The user confirms the removal of the employee;
       Record is deleted from database;  
       If error occurs, then error message displays;  
       If employee record is successfully deleted, then list of employees without deleted records is displaying.  
      
      ![image](https://user-images.githubusercontent.com/83345134/127285318-fc4847d6-ff49-4f51-863a-19ffafd29391.png "Delete employee")
    Pic 2.4 Delete employee dialog. 
    
    Cancel operation scenario:  
     User is in display mode of employees list and press “Delete” button;  
     Application displays confirmation dialog “Please confirm delete employee?”;
     User press “Cancel” button;  
     List of employees without changes is displaying.
    
