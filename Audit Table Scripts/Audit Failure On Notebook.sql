SELECT 
    -- Generate unique ID
    NEWID() AS Id,     

    -- Pipeline run ID                       
    '@{pipeline().RunId}' AS Process_Id, 

    -- Pipeline name             
    '@{pipeline().Pipeline}' AS Process_Name,

    -- Name of the activity       
    'Test Copy Data' AS Activity_Name,                
    
    -- Pipeline start time
    '@{pipeline().TriggerTime}' AS Start_Time,

    -- Pipeline end time        
    '@{utcNow()}' AS End_Time, 

    -- Execution status                        
    CASE 
        WHEN '@{activity('Test Copy Data').Status}' = 'Failed' THEN 'Failure'
        ELSE 'Success'
    END AS Status,   
    
    -- Error code of the failed activity (NULL for success)                                
    CASE 
        WHEN '@{activity('Test Copy Data').Status}' = 'Failed' THEN 
            '@{if(not(equals(activity('Test Copy Data').Error, null)), activity('Test Copy Data').Error.errorCode, '')}'
        ELSE NULL
    END AS Error_Code, 

     
    -- Error message (success message for successful execution)                              
    CASE 
        WHEN '@{activity('Test Copy Data').Status}' = 'Failed' THEN 
            '@{if(not(equals(activity('Test Copy Data').Error, null)), replace(activity('Test Copy Data').Error.message, '''', ''), '')}'
        ELSE 'Execution successful'
    END AS Error_Message,  

    -- Log timestamp                           
    '@{utcNow()}' AS Log_Time                         
