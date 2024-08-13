moduleList = """
### MODULE: Purchase Orders

Colour Theme:
- Primary Color: Orange (#FFA500)
- Secondary Color: White (#FFFFFF)

---

### PAGE 1: Purchase Order Creation Page

- **Logic**: 
  - **Form Validation**: Ensure all required fields (date, shipping address, company name, and at least one item in the table) are filled before allowing the user to save or download the purchase order.
  - **PDF/Excel Generation**: Implement functions to generate a PDF or Excel file with the filled information, including the company logo and color scheme.
  - **Local Storage**: Save the purchase order details in local storage for future reference when the user clicks the save button.

- **Page Layout and Design**:
  - **Top Section**:
    - **Header**: Display the title "Create Purchase Order" centered at the top of the page.
    - **Date Field**: Positioned below the header, aligned to the left. Use a date picker component from MUI.
    - **Shipping Address Field**: Positioned next to the date field, aligned to the right. Use a text field component from MUI.

  - **Mid-Section**:
    - **Company Information**:
      - **Company Name Field**: Positioned below the date and shipping address fields, spanning the full width. Use a text field component from MUI.
      - **Company Logo Upload**: Positioned below the company name field, aligned to the left. Use a file upload component from MUI.
      - **Color Scheme Selector**: Positioned next to the logo upload, aligned to the right. Use a color picker component from MUI.
    - **Items Table**:
      - **Table Header**: Include columns for Item Name, Quantity, Unit Price, and Total Price.
      - **Table Rows**: Allow users to add, edit, and delete rows. Each row should have input fields for item name, quantity, and unit price, with the total price calculated automatically.
      - **Add Item Button**: Positioned below the table, aligned to the left. Use a button component from MUI.
    - **Signature Field**: Positioned below the items table, spanning the full width. Use a text field component from MUI for the user to type their name.

  - **Mid-Bottom Section**:
    - **Save Button**: Positioned to the left, below the signature field. Use a button component from MUI. On click, validate the form and save the data to local storage.
    - **Download as PDF Button**: Positioned next to the save button. Use a button component from MUI. On click, validate the form and generate a PDF file.
    - **Download as Excel Button**: Positioned next to the PDF button. Use a button component from MUI. On click, validate the form and generate an Excel file.

  - **Bottom Section**:
    - **Footer**: Display a simple footer with the text "Purchase Order Module" centered at the bottom of the page.

- **Visual Design**:
  - **Layout**: Use a grid layout to ensure proper alignment and spacing of components.
  - **Colors**: 
    - Header and buttons: Orange (#FFA500)
    - Background: White (#FFFFFF)
    - Text: Black (#000000)
  - **Typography**:
    - Header: Font size 24px, weight 600
    - Form Labels: Font size 16px, weight 400
    - Input Fields: Font size 14px, weight 400
    - Buttons: Font size 16px, weight 500
  - **Styling**:
    - Use consistent padding and margins to ensure a clean and organized layout.
    - Apply rounded corners to buttons and input fields for a modern look.
    - Ensure high contrast between text and background for readability.

---

### PAGE 2: Purchase Order History Page

- **Logic**:
  - **Fetch Data**: Retrieve purchase order details from local storage and display them in a table.
  - **Search Functionality**: Implement a search function to filter the table based on date, vendor, or status.
  - **View Template**: Allow users to view the PDF/Excel template of a selected purchase order by clicking a button.

- **Page Layout and Design**:
  - **Top Section**:
    - **Header**: Display the title "Purchase Order History" centered at the top of the page.
    - **Search Bar**: Positioned below the header, spanning the full width. Use a text field component from MUI with a search icon.

  - **Mid-Section**:
    - **Purchase Orders Table**:
      - **Table Header**: Include columns for Date, Vendor, Total Amount, and Status.
      - **Table Rows**: Display purchase order details retrieved from local storage. Each row should include a button to view the PDF/Excel template.
      - **View Template Button**: Positioned in the last column of each row. Use a button component from MUI. On click, open the corresponding PDF/Excel file.

  - **Mid-Bottom Section**:
    - **Pagination**: Positioned below the table, centered. Use a pagination component from MUI to navigate through multiple pages of purchase orders.

  - **Bottom Section**:
    - **Footer**: Display a simple footer with the text "Purchase Order Module" centered at the bottom of the page.

- **Visual Design**:
  - **Layout**: Use a grid layout to ensure proper alignment and spacing of components.
  - **Colors**: 
    - Header and buttons: Orange (#FFA500)
    - Background: White (#FFFFFF)
    - Text: Black (#000000)
  - **Typography**:
    - Header: Font size 24px, weight 600
    - Table Headers: Font size 16px, weight 500
    - Table Rows: Font size 14px, weight 400
    - Buttons: Font size 16px, weight 500
  - **Styling**:
    - Use consistent padding and margins to ensure a clean and organized layout.
    - Apply rounded corners to buttons and input fields for a modern look.
    - Ensure high contrast between text and background for readability.

### MODULE: Assembly

Colour Theme:
- Primary Color: Orange (#FFA500)
- Secondary Color: White (#FFFFFF)

---

### PAGE 1: Assembly Tracking Page

- **Logic**: 
  - **Form Validation**: Ensure all required fields (time, date, frame number, project, frame type, and picture upload) are filled before allowing submission.
  - **Save Function**: Save the assembly details in local storage when the user clicks the save button.
  - **Submit Function**: Submit the form data and log deficiencies for review in the statistics page.
  - **Signature Capture**: Capture and store the worker's signature.
  - **Deficiency Logging**: Allow workers to log deficiencies, which are then marked for review.

- **Page Layout and Design**:
  - **Top Section**:
    - **Header**: Display a header with the title "Assembly Tracking" centered and styled with the primary color (Orange #FFA500) and a bold font weight.
    - **Date and Time Fields**: Place date and time input fields side by side, with labels above each field. Use a simple, clean design with white backgrounds and a border color matching the primary color.
  
  - **Mid-Section**:
    - **Frame Details Form**:
      - **Frame Number**: A text input field for the frame number with a label above it.
      - **Project**: A dropdown menu for selecting the project, with a label above it.
      - **Frame Type**: A dropdown menu for selecting the frame type, with a label above it.
      - **Picture Upload**: An upload button for the frame drawing picture, with a label above it. Display a thumbnail preview of the uploaded image.
    - **Signature Field**: 
      - **Canvas for Signature**: A canvas area where workers can sign using a stylus or mouse. Include a clear button to reset the signature.
      - **Signature Label**: A label above the canvas area indicating "Worker Signature".
  
  - **Mid-Bottom Section**:
    - **Deficiency Logging**:
      - **Text Area**: A large text area for logging deficiencies, with a label above it.
      - **Deficiency List**: Display a list of logged deficiencies below the text area, with options to edit or delete each entry.
  
  - **Bottom Section**:
    - **Action Buttons**:
      - **Save Button**: A button labeled "Save" styled with the primary color (Orange #FFA500) and white text. On click, it saves the form data to local storage.
      - **Submit Button**: A button labeled "Submit" styled with the primary color (Orange #FFA500) and white text. On click, it validates the form and submits the data.
      - **Clear Button**: A button labeled "Clear" styled with a secondary color (White #FFFFFF) and primary color text. On click, it clears all form fields.

- **Visual Design**:
  - **Layout**: Use a single-column layout with sections stacked vertically. Ensure adequate spacing between sections for clarity.
  - **Colors**:
    - **Primary Color**: Orange (#FFA500) for buttons, labels, and headers.
    - **Secondary Color**: White (#FFFFFF) for backgrounds and text areas.
  - **Typography**:
    - **Headers**: Bold font weight, primary color, and a font size of 24px.
    - **Labels**: Regular font weight, primary color, and a font size of 16px.
    - **Input Fields**: Regular font weight, secondary color, and a font size of 14px.
  - **Components**:
    - **Input Fields**: White background with a border color matching the primary color. Padding inside the fields for better user experience.
    - **Buttons**: Rounded corners with a slight shadow for a 3D effect. Primary color background with white text for primary actions, and vice versa for secondary actions.
    - **Signature Canvas**: A bordered area with a light grey background to distinguish it from other form fields.
    - **Deficiency List**: Each deficiency entry in a bordered box with a light grey background, and edit/delete icons on the right side.

This detailed plan ensures that the Assembly Tracking Page is user-friendly, visually appealing, and functionally robust, adhering to the specified color theme and design guidelines.

### MODULE: Glazing

Colour Theme:
- Primary Color: Orange (#FFA500)
- Secondary Color: White (#FFFFFF)

---

### PAGE 1: Glazing Tracking Page

- **Logic**: 
  - **Form Validation**: Ensure all required fields (time, date, frame number, project, frame type, and picture upload) are filled before allowing submission.
  - **Local Storage**: Save the glazing details in local storage upon form submission.
  - **Deficiency Logging**: Allow workers to log deficiencies, which are then marked for review and can be viewed on the statistics page.
  - **Signature Capture**: Capture and store the worker's signature as part of the form submission.

- **Page Layout and Design**:

    - **Top Section**:
        - **Header**: A simple header with the title "Glazing Tracking" centered and styled with the primary color (Orange #FFA500) and secondary color (White #FFFFFF).
        - **Date and Time Fields**: Two input fields for date and time, placed side by side. The date field uses a date picker, and the time field uses a time picker. Both fields are required and have placeholder text "Select Date" and "Select Time" respectively.

    - **Mid-Section**:
        - **Frame Details Form**:
            - **Frame Number**: A text input field labeled "Frame Number" with placeholder text "Enter Frame Number". This field is required.
            - **Project**: A dropdown menu labeled "Project" with a list of dummy project names. This field is required.
            - **Frame Type**: A dropdown menu labeled "Frame Type" with options like "Type A", "Type B", etc. This field is required.
            - **Picture Upload**: A file input field labeled "Upload Frame Drawing". This allows users to upload an image file. The field is required and accepts only image formats (JPEG, PNG).

    - **Mid-Bottom Section**:
        - **Signature Field**: 
            - **Canvas for Signature**: A canvas element where workers can draw their signature using a mouse or touch input. The canvas should have a clear button to reset the signature.
            - **Signature Capture**: The captured signature is converted to a data URL and stored in local storage along with other form data.
        - **Deficiency Log**:
            - **Text Area**: A large text area labeled "Log Deficiencies" where workers can enter any issues or deficiencies they notice. This field is optional.

    - **Bottom Section**:
        - **Buttons**:
            - **Save Button**: A button labeled "Save" that saves the current form data to local storage without submitting it. The button is styled with the primary color (Orange #FFA500) and white text.
            - **Submit Button**: A button labeled "Submit" that validates the form, saves the data to local storage, and marks any deficiencies for review. The button is styled similarly to the save button.

- **Visual Design**:
    - **Layout**: The page uses a single-column layout with a centered form. Each section is separated by ample white space to ensure clarity and ease of use.
    - **Colors**: 
        - Background: White (#FFFFFF)
        - Text: Black (#000000) for labels and input text, Orange (#FFA500) for headers and buttons.
    - **Typography**:
        - Headers: Bold, 24px, Orange (#FFA500)
        - Labels: Regular, 16px, Black (#000000)
        - Input Text: Regular, 14px, Black (#000000)
    - **Components**:
        - **Input Fields**: Styled with a border radius of 4px, border color light grey (#D3D3D3), and padding of 8px.
        - **Buttons**: Rounded corners with a border radius of 4px, background color Orange (#FFA500), and white text. On hover, the background color darkens slightly to #FF8C00.
        - **Canvas for Signature**: A bordered area with a light grey (#D3D3D3) border and a clear button styled similarly to the form buttons.

This detailed plan ensures that the Glazing Tracking Page is user-friendly, visually appealing, and functionally robust, adhering to the specified color theme and design guidelines.

### MODULE: Installation

Colour Theme:
- Primary Color: Orange (#FFA500)
- Secondary Color: White (#FFFFFF)

---

### PAGE 1: Installation Tracking Page

- **Logic**: 
  - **Form Validation**: Ensure all required fields (time, date, frame number, project, frame type, and picture upload) are filled before allowing submission.
  - **Local Storage**: Save the installation details in the browser's local storage upon form submission.
  - **Deficiency Logging**: Allow workers to log deficiencies, which are then marked for review and can be viewed on the statistics page.
  - **Signature Capture**: Capture and store the worker's signature digitally.
  - **Form Reset**: Reset the form fields after successful submission.

- **Page Layout and Design**:

    - **Top Section**:
        - **Header**: 
          - A simple header with the title "Installation Tracking" centered.
          - Font: Arial, 24px, bold, color: Orange (#FFA500).
          - Background: White (#FFFFFF).
          - Padding: 20px.
    
    - **Mid-Section**:
        - **Form Fields**:
          - **Time and Date**:
            - Two input fields side by side.
            - Time Input: Type "time", placeholder "HH:MM", required.
            - Date Input: Type "date", placeholder "YYYY-MM-DD", required.
            - Styling: Border-radius: 5px, Border: 1px solid Orange (#FFA500), Padding: 10px, Margin: 10px.
          - **Frame Details**:
            - Frame Number: Text input, placeholder "Frame Number", required.
            - Project: Text input, placeholder "Project Name", required.
            - Frame Type: Dropdown select with options (e.g., "Type A", "Type B"), required.
            - Styling: Border-radius: 5px, Border: 1px solid Orange (#FFA500), Padding: 10px, Margin: 10px.
          - **Picture Upload**:
            - File input for uploading a picture of the frame drawing.
            - Accepts image files only (e.g., .jpg, .png).
            - Styling: Border-radius: 5px, Border: 1px solid Orange (#FFA500), Padding: 10px, Margin: 10px.
    
    - **Mid-Bottom Section**:
        - **Signature Field**:
          - Canvas area for capturing the worker's signature.
          - Clear button to reset the signature field.
          - Styling: Border: 2px solid Orange (#FFA500), Width: 100%, Height: 150px, Margin: 10px.
        - **Deficiency Log**:
          - Text area for logging deficiencies.
          - Placeholder: "Log any deficiencies here..."
          - Styling: Border-radius: 5px, Border: 1px solid Orange (#FFA500), Padding: 10px, Margin: 10px, Width: 100%, Height: 100px.
    
    - **Bottom Section**:
        - **Buttons**:
          - Save Button: Saves the form data to local storage.
            - Text: "Save", Background: Orange (#FFA500), Color: White (#FFFFFF), Border-radius: 5px, Padding: 10px 20px, Margin: 10px.
          - Submit Button: Validates the form and submits the data.
            - Text: "Submit", Background: Orange (#FFA500), Color: White (#FFFFFF), Border-radius: 5px, Padding: 10px 20px, Margin: 10px.
          - Reset Button: Clears all form fields.
            - Text: "Reset", Background: White (#FFFFFF), Color: Orange (#FFA500), Border-radius: 5px, Padding: 10px 20px, Margin: 10px, Border: 1px solid Orange (#FFA500).

- **Visual Design**:
    - **Layout**:
      - The page is divided into four main sections: Top, Mid, Mid-Bottom, and Bottom.
      - Each section is clearly separated with ample padding and margin to ensure a clean and organized appearance.
    - **Components**:
      - **Header**: Bold and prominent to immediately inform the user of the page's purpose.
      - **Form Fields**: Uniform styling with rounded borders and consistent padding/margin to enhance usability.
      - **Signature Field**: Large enough to capture clear signatures, with a reset option for convenience.
      - **Deficiency Log**: Spacious text area to accommodate detailed notes.
      - **Buttons**: Clearly labeled and color-coded for intuitive interaction.
    - **Colors**:
      - Primary Color: Orange (#FFA500) for key interactive elements (buttons, borders).
      - Secondary Color: White (#FFFFFF) for background and text areas.
    - **Typography**:
      - Header: Arial, 24px, bold, Orange (#FFA500).
      - Form Labels and Inputs: Arial, 16px, regular, Black (#000000).
      - Buttons: Arial, 16px, bold, White (#FFFFFF) for text on Orange buttons, Orange (#FFA500) for text on White buttons.
    - **Overall Styling**:
      - Clean and professional with a focus on usability.
      - Consistent use of the primary and secondary colors to create a cohesive look.
      - Rounded corners and ample spacing to enhance the user experience and make the form approachable.

### MODULE: Work Orders

Colour Theme:
- Primary Color: Orange (#FFA500)
- Secondary Color: White (#FFFFFF)

---

### PAGE 1: Work Order Assignment Page

- **Logic**: 
  - **Form Validation**: Ensure all required fields (project, frame number, process, worker, and due date) are filled before allowing submission.
  - **Save Work Order**: Function to save work order details in local storage.
  - **Assign Multiple Work Orders**: Function to allow batch assignment of work orders to multiple frames or workers efficiently.

- **Page Layout and Design**:
  - **Top Section**:
    - **Title**: "Assign Work Orders" in bold, large font (24px, weight 700), centered.
    - **Breadcrumb Navigation**: "Home > Work Orders > Assign" in smaller font (14px, weight 400), left-aligned.

  - **Mid-Section**:
    - **Form Fields**:
      - **Project Dropdown**: Dropdown menu to select the project. Label: "Project", placeholder: "Select Project".
      - **Frame Number Input**: Text input for frame number. Label: "Frame Number", placeholder: "Enter Frame Number".
      - **Process Dropdown**: Dropdown menu to select the process. Label: "Process", placeholder: "Select Process".
      - **Worker Dropdown**: Dropdown menu to select the worker. Label: "Worker", placeholder: "Select Worker".
      - **Due Date Picker**: Date picker for selecting the due date. Label: "Due Date", placeholder: "Select Due Date".
    - **Form Validation**:
      - Real-time validation with error messages displayed below each field if not filled correctly.
      - Disabled submit button until all fields are valid.

  - **Mid-Bottom Section**:
    - **Buttons**:
      - **Save Button**: Orange button (#FFA500) with white text, labeled "Save Work Order". Positioned to the right.
      - **Assign Button**: Orange button (#FFA500) with white text, labeled "Assign Work Orders". Positioned next to the Save button.
    - **Button Logic**:
      - Save Button: On click, validate form and save work order details to local storage.
      - Assign Button: On click, validate form and assign multiple work orders based on user input.

  - **Bottom Section**:
    - **Status Message**: Area to display success or error messages after form submission. Positioned below the buttons, centered, with dynamic text color (green for success, red for error).

- **Visual Design**:
  - **Layout**: 
    - Form fields arranged in a single column, centered on the page with ample spacing (20px) between each field.
    - Buttons aligned horizontally, right-aligned within the form container.
  - **Colors**:
    - Form Labels: Orange (#FFA500)
    - Input Fields: White background (#FFFFFF) with orange border (#FFA500)
    - Buttons: Orange background (#FFA500) with white text (#FFFFFF)
  - **Typography**:
    - Title: 24px, weight 700, color Orange (#FFA500)
    - Breadcrumb: 14px, weight 400, color Black (#000000)
    - Form Labels: 16px, weight 500, color Orange (#FFA500)
    - Input Fields: 16px, weight 400, color Black (#000000)
    - Buttons: 16px, weight 600, color White (#FFFFFF)
  - **Overall Styling**:
    - Clean and modern design with a focus on usability.
    - Consistent use of primary and secondary colors to maintain visual coherence.
    - Clear and readable typography to enhance user experience.

---

### PAGE 2: Worker Work Order Page

- **Logic**: 
  - **Fetch Work Orders**: Function to fetch assigned work orders from local storage.
  - **Display Work Orders**: Function to display work orders in a table format.
  - **Log Completed Parts**: Function to log completed parts and update the status of work orders.

- **Page Layout and Design**:
  - **Top Section**:
    - **Title**: "My Work Orders" in bold, large font (24px, weight 700), centered.
    - **Breadcrumb Navigation**: "Home > Work Orders > My Work Orders" in smaller font (14px, weight 400), left-aligned.

  - **Mid-Section**:
    - **Work Orders Table**:
      - **Columns**: Project, Frame Number, Process, Due Date, Status, Actions.
      - **Rows**: Dynamically populated with work order data from local storage.
      - **Table Design**:
        - Header Row: Orange background (#FFA500) with white text (#FFFFFF), bold font (16px, weight 600).
        - Data Rows: Alternating row colors (white #FFFFFF and light grey #F5F5F5) for readability.
        - Actions Column: Contains a button to log completed parts.

  - **Mid-Bottom Section**:
    - **Log Completed Parts Button**:
      - Orange button (#FFA500) with white text, labeled "Log Completed Parts".
      - Positioned within the Actions column of each row.
    - **Button Logic**:
      - On click, open a modal to log completed parts.
      - Modal contains input fields for parts completed and a submit button.
      - On submit, update the status of the work order in local storage.

  - **Bottom Section**:
    - **Status Message**: Area to display success or error messages after logging completed parts. Positioned below the table, centered, with dynamic text color (green for success, red for error).

- **Visual Design**:
  - **Layout**:
    - Table centered on the page with ample spacing (20px) between rows.
    - Log Completed Parts button within each row for easy access.
  - **Colors**:
    - Table Header: Orange (#FFA500) background with white text (#FFFFFF)
    - Table Rows: Alternating white (#FFFFFF) and light grey (#F5F5F5)
    - Buttons: Orange background (#FFA500) with white text (#FFFFFF)
  - **Typography**:
    - Title: 24px, weight 700, color Orange (#FFA500)
    - Breadcrumb: 14px, weight 400, color Black (#000000)
    - Table Header: 16px, weight 600, color White (#FFFFFF)
    - Table Data: 14px, weight 400, color Black (#000000)
    - Buttons: 14px, weight 600, color White (#FFFFFF)
  - **Overall Styling**:
    - Clean and modern design with a focus on usability.
    - Consistent use of primary and secondary colors to maintain visual coherence.
    - Clear and readable typography to enhance user experience.

### MODULE: Statistics

Colour Theme:
- Primary Color: Orange (#FFA500)
- Secondary Color: White (#FFFFFF)

---

### PAGE 1: Statistics Dashboard Page

- **Logic**: 
  - **Data Fetching**: Implement a function to fetch data from local storage. This function will retrieve the necessary data for visualization and analysis.
  - **Graph Generation**: Use a library like Chart.js or Recharts to generate various types of graphs (e.g., bar charts, line charts) based on the fetched data.
  - **Table Generation**: Create tables using MUI's DataGrid component to display detailed data breakdowns.
  - **Mathematical Statistics**: Calculate and display key statistics such as averages, totals, and other relevant metrics.
  - **Data Export**: Implement functions to export the displayed data in PDF and Excel formats using libraries like jsPDF and SheetJS.

- **Page Layout and Design**:
  - **Top Section**:
    - **Title**: A prominent title "Statistics Dashboard" centered at the top.
    - **Date Range Picker**: A date range picker component to filter data by date.
    - **Export Buttons**: Two buttons labeled "Export to PDF" and "Export to Excel" for exporting the data.

  - **Mid-Section**:
    - **Graphs**:
      - **Bar Chart**: A bar chart to visualize categorical data trends.
      - **Line Chart**: A line chart to show data trends over time.
      - **Pie Chart**: A pie chart to represent data distribution.
    - **Tables**:
      - **Data Table**: A detailed data table using MUI's DataGrid component to display raw data.
      - **Summary Table**: A smaller table summarizing key statistics (e.g., averages, totals).
    - **Statistics Summaries**:
      - **Average**: Display the average of a particular dataset.
      - **Total**: Display the total sum of a dataset.
      - **Other Metrics**: Display other relevant metrics as needed.

  - **Mid-Bottom Section**:
    - **Filters**: Additional filters to refine the data displayed in the graphs and tables (e.g., dropdowns for category selection).
    - **Refresh Button**: A button to refresh the data displayed on the dashboard.

  - **Bottom Section**:
    - **Footer**: A simple footer with the text "© 2023 Statistics Module" centered at the bottom.

- **Visual Design**:
  - **Layout**:
    - The page is divided into four main sections: Top, Mid, Mid-Bottom, and Bottom.
    - The Top section contains the title, date range picker, and export buttons.
    - The Mid section is split into two columns: the left column for graphs and the right column for tables and statistics summaries.
    - The Mid-Bottom section contains filters and a refresh button.
    - The Bottom section contains the footer.
  - **Components**:
    - **Title**: Font size 24px, font weight bold, color Orange (#FFA500).
    - **Date Range Picker**: Positioned to the right of the title, with a border color of Orange (#FFA500).
    - **Export Buttons**: Orange background (#FFA500), white text (#FFFFFF), rounded corners, and a hover effect that darkens the background color.
    - **Graphs**: Each graph has a white background (#FFFFFF) with a border color of Orange (#FFA500).
    - **Tables**: Tables have alternating row colors (white and light grey), with headers in Orange (#FFA500) and text in black.
    - **Statistics Summaries**: Displayed in bold text, with key metrics highlighted in Orange (#FFA500).
    - **Filters**: Dropdowns and other filter components have a white background (#FFFFFF) with a border color of Orange (#FFA500).
    - **Refresh Button**: Orange background (#FFA500), white text (#FFFFFF), rounded corners, and a hover effect that darkens the background color.
    - **Footer**: Font size 14px, color Orange (#FFA500), centered text.

This detailed plan ensures that the Statistics Dashboard Page is both functional and visually appealing, adhering to the specified color theme and providing a comprehensive data visualization and analysis experience.

"""
def parse_modules_to_list(data):
    modules = []
    current_module = ""

    lines = data.strip().splitlines()
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("### MODULE:") and current_module:
            # If a new module starts, append the current module to the list
            modules.append(current_module.strip())
            current_module = line + " "
        else:
            current_module += line + " "
    
    # Append the last module to the list
    if current_module:
        modules.append(current_module.strip())

    return modules

# print(parse_modules_to_list(moduleList))

for module in parse_modules_to_list(moduleList):
    print(module)
    print("\n")