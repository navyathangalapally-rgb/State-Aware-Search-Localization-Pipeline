🎨 abi.css (Frontend Architecture)
This stylesheet handles the visual presentation of the manuals within the Microsoft WebView2 environment.  

Responsive Screenshots: Uses the .standard-screenshot class with max-width: 100% and height: auto to prevent horizontal scrolling on small screens.  

Sticky UI: Implements position: sticky for the search header so navigation remains accessible during long scrolls.  

Search Visuals: Defines the .highlight class with a yellow background to clearly mark search results.  

🔍 search.js (Interactive Logic)
This file executes a "zero-dependency" search engine designed to work locally without external libraries.  

State Preservation: On page load, it captures document.body.innerHTML into originalState to prevent permanent DOM corruption during highlighting.  

RegEx Engine: Uses a global, case-insensitive Regular Expression to identify user keywords.  

Automatic Navigation: Includes a scrollIntoView function that smoothly moves the browser window to the first match found.  

🤖 localize.py (Automation Pipeline)
A Python script using the BeautifulSoup4 library to automate the transition from English to German and Polish.  

DOM Parsing: Traverses the HTML tree to extract text specifically from <p>, <td>, and <h> tags while ignoring functional attributes.  

Path Flattening: Automatically strips complex relative paths and replaces them with local references, ensuring documentation portability.  

Asset Repair: Identifies <img> tags and re-maps their source attributes to a standardized local images directory.  
