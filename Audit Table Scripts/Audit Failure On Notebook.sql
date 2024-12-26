SELECT 
    NEWID() AS Id,                                    -- Generate unique ID
    '@{pipeline().RunId}' AS Process_Id,              -- Pipeline run ID
    '@{pipeline().Pipeline}' AS Process_Name,         -- Pipeline name
    CASE 
        WHEN '@{activity('Test Note Book').Status}' = 'Failed' THEN 'Databricks Notebook'
        ELSE 'Unknown'
    END AS Activity_Name,                             -- Name of the failed activity
    
    '@{pipeline().TriggerTime}' AS Start_Time,        -- Pipeline start time
    '@{utcNow()}' AS End_Time,                        -- Pipeline end time
    CASE 
        WHEN '@{activity('Test Note Book').Status}' = 'Failed' THEN 'Failure'
        ELSE 'Success'
    END AS Status,                                    -- Execution status
    CASE 
        WHEN '@{activity('Test Note Book').Status}' = 'Failed' THEN '@{activity('Test Note Book').Error.errorCode}'
        ELSE NULL
    END AS Error_Code,                                -- Error code of the failed activity
    CASE 
        WHEN '@{activity('Test Note Book').Status}' = 'Failed' THEN '@{replace(activity('Test Note Book').Error.message,'''','')}'
        ELSE 'Execution successful'
    END AS Error_Message,                             -- Error message
    '@{utcNow()}' AS Log_Time                         -- Log timestamp
