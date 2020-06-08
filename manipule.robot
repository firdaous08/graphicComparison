*** Settings ***
Library    Process

*** Test Cases ***
#Capture
      # ${result}=  run process   python  C:/Robot/ImageMagick-20200513T143214Z-001/ImageMagick/PythonTest/captureScreenshot.py
      # Should be equal as integers | ${result.rc} | 0
      # Should be equal as strings       ${result.stdout}      Done.: Capturing http://www.pp.lahalle.com screenshot as screen_staging.png ...  Done.    Capturing http://www.lahalle.com screenshot as screen_production.png ... Done.


Grid
       ${result}=  run process   python  C:/Robot/ImageMagick-20200513T143214Z-001/ImageMagick/PythonTest/Grid.py
      # Should be equal as integers | ${result.rc} | 0
      # Should be equal as strings       ${result.stdout}      Done.: Capturing http://www.pp.lahalle.com screenshot as screen_staging.png ...  Done.    Capturing http://www.lahalle.com screenshot as screen_production.png ... Done.      
