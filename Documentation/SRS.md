## 2. Employees  
  ### 2.1. Display list of Employees  
  This mode is intended for viewing and editing the employees list.  
  
  __Main scenario:__
  1. User selects item "Employees";
  2. Application dispalys list of employees.  
      
  ![image](https://user-images.githubusercontent.com/83345134/127665649-7972b0b3-22ea-421e-9dfa-fc800c72069c.png "Employees list")  
    Pic 2.1.1 View the employees list.
    
  __The list displays following employees' information:__  
  1. Department - place, where employee is working;  
  2. Name of the employee;  
  3. Date of birth of the employee;  
  4. Employee's salary.  
    
  __Filtering by date:__  
  1. In the employees list view mode, the user sets a date filter and presses the refresh list button (to the right of the date entry field);  
  2. The application will show the employees only for a certain period of time.
  3. If user wants to get employees, that are born below any date, he/she should set only end date and press refresh button.
  4. If user wants to get employees, that are born after any date, he/she should set only start date and press refresh button.
  5. To reset filter, user should press the reset button.

  __Restrictions:__  
  * Start date of the period should be less then end date of the period, but if the user will make a mistake, he/she will see the invalid date message
  ![image](https://user-images.githubusercontent.com/83345134/127665988-e414e59f-72dd-4dfb-acea-45c86dfafb68.png)
  Pic 2.1.2 Invalid date message
  * Updating data after selecting the filtering conditions is carried out by pressing the “Refresh” button.  

      
  ### 2.2. Add employee  
     
   ![image](https://user-images.githubusercontent.com/83345134/127285174-8b015c12-a1b2-4ff9-a32c-d93a516a4bbb.png "Add employee")  
      Pic 2.2.1 Add employee.  
      
  __Main scenario:__  
  * User clicks the “Add” button in the employees list view mode;  
  * Application displays form to enter employee data;  
  * User enters employee’s data and presses “Save” button;  
  * If any data is entered incorrectly, incorrect data messages are displayed:  
  ![image](https://user-images.githubusercontent.com/83345134/127649375-0ce328e1-11a7-494b-a3c3-54e2081a6185.png)  
  Pic 2.2.2 Adding validation error  
  * If entered data is valid, then record is adding to database;  
  * If error occurs, then error message is displaying, the message is following:  
  ![image](https://user-images.githubusercontent.com/83345134/127639007-3ceae0d9-212e-4714-8424-e515f535e0e3.png)  
  Pic 2.2.3 Adding system error  
  * If new employee record is successfully added, then list of employees with added records is displaying.   
      
  __When adding a employee, the following details are entered:__  
  * Department – employee’s work place;  
  * Name – employee’s name;  
  * Salary – employee’s salary;  
  * Date of birth – employee’s date of birth.  

  __Constraints for data validation:__  
  * Department – one of the departments;  
  * Name –  maximum length of 45 characters;  
  * Salary – maximum value is 2000;  
  * Date of birth – date in format dd/mm/yyyy.   
      
  ### 2.3 Edit employee  
        
![image](https://user-images.githubusercontent.com/83345134/127285373-3f14cb74-9510-4dc3-8e3a-2c2c01dee4a4.png "Edit employee")  
    Pic. 2.3.1 Edit employee.  
    
  __Main scenario:__  
  * User clicks the “Edit” button in the employees list view mode;  
  * Application displays form to enter employee data;  
  * User enters cemployee’s data and presses “Save” button;  
  * If any data is entered incorrectly, incorrect data messages are displayed  
  ![image](https://user-images.githubusercontent.com/83345134/127649385-d249277f-5c6b-499c-bfdc-eb31d32e981a.png)  
  Pic 2.3.2 Editing validation error  
  * If entered data is valid, then edited data is added to database;  
  * If error occurs, then error message is displaying  
  ![image](https://user-images.githubusercontent.com/83345134/127639014-e66fa490-4b0f-487c-8006-6faf4f215ced.png)  
  Pic 2.3.3 Editing system error  
  * If employee’s record is successfully edited, then list of employees with added records is displaying.   

  ### 2.4 Removing employee  
        
  ![image](https://user-images.githubusercontent.com/83345134/127285318-fc4847d6-ff49-4f51-863a-19ffafd29391.png)  
    Pic 2.4.1 Delete employee dialog.  
    
  __Main scenario:__  
  * The user, while in the list of employees mode, presses the "Delete" button in the selected employee line;  
  * Application displays confirmation dialog “Please confirm delete employee?”;  
  * The user confirms the removal of the employee;  
  * Record is deleted from database;  
  * If error occurs, then error message displays  
  ![delete error](https://user-images.githubusercontent.com/83345134/127639021-fb06c230-6baa-466c-a253-d553aeb58a00.png)
  Pic 2.4.2 Deleting error occurs   
  * If employee record is successfully deleted, then list of employees without deleted records is displaying.     
    
   ### 2.5 Canceling operation
   If user wants to cancel Adding/Editing/Deleting operation, there are several ways:
   * User can press button "Cancel", then user will be returned to employees list;
   * User can switch to "Departments" menu item and chnges won't get in database.
