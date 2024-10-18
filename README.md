# Blood Donation Forum Application

## Overview
A Tkinter-based desktop application that connects to a MySQL database to manage blood donor information. Users can search for donors by blood group, sign up as a donor, or log in to manage their account.

## Key Features
- **Search Donors**: Retrieve and display donor details based on blood group.
- **Sign Up**: Register as a blood donor.
- **Login & Manage Account**: Log in to view or delete your account.

## Requirements
- **Python 3.x**
- **MySQL Database** with the following table:
   ```sql
   CREATE DATABASE blooddonation;
   CREATE TABLE bloodgroup (
       Name VARCHAR(50),
       City VARCHAR(50),
       Bloodgroup VARCHAR(5),
       Gender VARCHAR(10),
       Phone_No VARCHAR(15),
       Allergies VARCHAR(100)
   );
   ```
- **MySQL Connector**: Install with:
   ```
   pip install mysql-connector-python
   ```

## Running the Application
1. Set up MySQL and the database.
2. Run the Python script:
   ```bash
   python filename.py
   ```

## Authors
