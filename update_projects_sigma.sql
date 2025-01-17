-- Create a new table named ‘projects’
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);
 
-- Add a new column ‘budget’ (of type DECIMAL(10, 2)) to the existing ‘projects’ table.
ALTER TABLE projects
ADD COLUMN budget DECIMAL(10, 2);