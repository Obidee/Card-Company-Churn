CREATE SCHEMA cardchurnproject;
USE cardchurnproject;
CREATE TABLE BankChurners(
					CLIENTNUM INT, Attrition_Flag VARCHAR(30), Customer_Age INT, Gender VARCHAR(10), 
					Dependent_count INT, Education_Level VARCHAR(30), Marital_Status VARCHAR(10), Income_Category VARCHAR(30), 
					Card_Category VARCHAR(10), Months_on_book INT, Total_Relationship_Count INT, Months_Inactive_12_mon INT, 
					Contacts_Count_12_mon INT, Credit_Limit INT, Total_Revolving_Bal INT, Avg_Open_To_Buy FLOAT, 
					Total_Amt_Chng_Q4_Q1 FLOAT, Total_Trans_Amt FLOAT, Total_Trans_Ct FLOAT, 
					Total_Ct_Chng_Q4_Q1 FLOAT, Avg_Utilization_Ratio FLOAT
                    );
  
 SELECT *
FROM BankChurners; 

-- What is the age range of attrited customers?
SELECT 
	CASE WHEN Customer_Age < 20 THEN 'less than 20' WHEN Customer_Age BETWEEN 20 AND 30 THEN '20-30'
		 WHEN Customer_Age BETWEEN 30 AND 40 THEN '30-40' WHEN Customer_Age BETWEEN 40 AND 50 THEN '40-50'
         WHEN Customer_Age BETWEEN 50 AND 60 THEN '50-60' WHEN Customer_Age BETWEEN 60 AND 70 THEN '60-70'
         WHEN Customer_Age > 70 THEN '70+' END AS Age_Range, 
	COUNT(*)
FROM BankChurners
WHERE Attrition_Flag = 'Attrited Customer'
GROUP BY Age_Range
Order by Age_Range; 

-- What is the average age of attrited customers by gender?
SELECT Gender, AVG(Customer_Age)
FROM BankChurners
WHERE Attrition_Flag = 'Attrited Customer'
GROUP BY Gender;

-- What is the average age of existing customers by gender?
SELECT Gender, AVG(Customer_Age)
FROM BankChurners
WHERE Attrition_Flag = 'Existing Customer'
GROUP BY Gender; 

-- What is the actual number of existing customers and attrited customers by gender?
-- Here we find number of male vs female attrited customers
SELECT 
		SUM(CASE WHEN Gender = 'M' THEN 1 ELSE 0 END) Male_Attrited,
        SUM(CASE WHEN Gender = 'F' THEN 1 ELSE 0 END) Female_attrited
FROM BankChurners
WHERE Attrition_Flag = 'Attrited Customer';
        
SELECT Gender, 
		SUM(CASE WHEN Attrition_Flag = 'Existing Customer' THEN 1 ELSE 0 END) Existing,
		SUM(CASE WHEN Attrition_Flag = 'Attrited Customer' THEN 1 ELSE 0 END) Attrited        
FROM BankChurners
GROUP BY Gender;

-- Number of male vs female existing customers
SELECT 
		SUM(CASE WHEN Gender = 'M' THEN 1 ELSE 0 END) Male_Existing,
        SUM(CASE WHEN Gender = 'F' THEN 1 ELSE 0 END) Female_existing
FROM BankChurners
WHERE Attrition_Flag = 'Existing Customer';

-- Attrited vs Existing customers by education level
SELECT Education_level, SUM(CASE WHEN Attrition_Flag = 'Existing Customer' THEN 1 ELSE 0 END) Existing,
						SUM(CASE WHEN Attrition_Flag = 'Attrited Customer' THEN 1 ELSE 0 END) Attrited
FROM BankChurners
GROUP BY Education_level;

-- %age of attrited customers to existing customers across education levels
WITH CTE AS (
			SELECT Education_level, SUM(CASE WHEN Attrition_Flag = 'Existing Customer' THEN 1 ELSE 0 END) Existing,
									SUM(CASE WHEN Attrition_Flag = 'Attrited Customer' THEN 1 ELSE 0 END) Attrited
			FROM BankChurners
			GROUP BY Education_level
            )
SELECT *, (Attrited/Existing )*100 AS Percentage_attrited
FROM CTE
ORDER BY Percentage_attrited DESC;

-- Distribution of attrited vs existing customers by marital status
SELECT Marital_Status, SUM(CASE WHEN Attrition_Flag = 'Existing Customer' THEN 1 ELSE 0 END) Existing,
					SUM(CASE WHEN Attrition_Flag = 'Attrited Customer' THEN 1 ELSE 0 END) Attrited
FROM BankChurners
GROUP BY Marital_Status;

-- Months on the books of the bank in relation to attrition
SELECT 
	CASE WHEN Months_on_book < 20 THEN '0-20'
		 WHEN Months_on_book BETWEEN 20 AND 30 THEN '20-30' WHEN Customer_Age BETWEEN 30 AND 40 THEN '30-40'
		 WHEN Months_on_book BETWEEN 40 AND 50 THEN '40-50' WHEN Customer_Age BETWEEN 50 AND 60 THEN '50-60'
         WHEN Months_on_book > 60 THEN '60+' END AS Months_on_books_Range, 
	SUM(CASE WHEN Attrition_Flag = 'Attrited Customer' THEN 1 ELSE 0 END) Attrited
FROM BankChurners
GROUP BY Months_on_books_Range
Order by Months_on_books_Range;

-- Average utilization by attrited vs existing customers
SELECT Attrition_Flag, ROUND(AVG(Avg_Utilization_Ratio)*100, 2) '%age of average utilization'
FROM BankChurners
GROUP BY Attrition_Flag;

SELECT COUNT(*)
FROM BankChurners;

