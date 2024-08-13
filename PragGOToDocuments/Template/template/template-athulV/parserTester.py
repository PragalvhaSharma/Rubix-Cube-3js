parseTester = """
### MODULE: Purchase Orders

1. **Module Overview**:
- **Purpose**: 
    The Purchase Orders module is designed to streamline the process of creating, managing, and tracking purchase orders sent to vendors. It ensures that all purchase orders are standardized, easily accessible, and well-documented. This module supports the business objective of maintaining organized and efficient procurement processes by providing a user-friendly interface for procurement team members, finance team members, and managers.

- **Responsibilities**: 
    The key tasks and functions handled by the Purchase Orders module include:
    - Creating new purchase orders using a standardized form.
    - Allowing users to fill in purchase order details such as date, shipping address, company name, and item list.
    - Providing options to download purchase orders in PDF or Excel format.
    - Displaying a history of past purchase orders with detailed views.
    - Enabling users to access and view the PDF/Excel version of past purchase orders.
    - Integrating with other modules for data exchange, such as inventory and vendor management.

2. **Page Details**:
For each page within the module, provide:

- **Page Title and Description**:
    - **Title**: Purchase Order Form
    - **Description**: 
        The Purchase Order Form page allows users to create new purchase orders by filling in necessary details. The target audience includes procurement team members who need to generate purchase orders, finance team members who need to verify them, and managers who need to review and approve them. Key features include a form for entering purchase order details, options to download the order in PDF or Excel format, and navigation to the Purchase Order History page.

- **Component Details**:
    - **General Description**: 
        - **TextInput**: Used for entering text details such as date, shipping address, and company name.
        - **Table**: Used for listing items and their prices, allowing users to add, edit, and remove items.
        - **Button**: Used for actions like "Download PDF" and "Download Excel".
        - **SignatureField**: Used for capturing the user's signature to include in the generated document.
    - **Layout**: 
        The layout follows a structured form design with aligned input fields, a table for item listing, and action buttons at the bottom. The form is divided into sections for easy navigation and data entry.
    - **Interactions**: 
        - Users fill in the TextInput components with relevant details.
        - Users interact with the Table component to manage the item list.
        - Users click the Button components to trigger the download of the purchase order in the selected format.
        - Users sign in the SignatureField to finalize the purchase order.
    - **Styling Requirements**: 
        - **Primary Colour**: #FFA500 (Orange)
        - **Secondary Colour**: #FFFFFF (White)
        - **Accent Colour**: #000000 (Black)
        - **Background Colour**: #F5F5F5 (Light Grey)
        - **Text Colour**: #333333 (Dark Grey)
        - **Link Colour**: #FFA500 (Orange)
        - Fonts: Use a consistent font family with sizes ranging from 14px to 18px for readability.

- **Component Implementation**:
    - **Integration**: 
        - Import and use the TextInput, Table, Button, and SignatureField components within the form.
        - Ensure reusability by adhering to the overall design system and avoiding redundant details.
        - Example:
            ```jsx
            import TextInput from 'components/TextInput';
            import Table from 'components/Table';
            import Button from 'components/Button';
            import SignatureField from 'components/SignatureField';

            const PurchaseOrderForm = () => {
                return (
                    <div className="purchase-order-form">
                        <TextInput label="Date" />
                        <TextInput label="Shipping Address" />
                        <TextInput label="Company Name" />
                        <Table />
                        <SignatureField />
                        <Button label="Download PDF" />
                        <Button label="Download Excel" />
                    </div>
                );
            };
            ```

3. **Page Layout and Design**:
For each page within the module, provide:

- **Top Section**: 
    The top section includes a header with the page title "Purchase Order Form" and a brief description of the page's purpose. It sets the context for the user and provides navigation links to other pages, such as the Purchase Order History page.

- **Content Area**: 
    The main content area contains the form for entering purchase order details. It includes:
    - TextInput components for date, shipping address, and company name.
    - A Table component for listing items and their prices.
    - A SignatureField for capturing the user's signature.
    - Action buttons for downloading the purchase order in PDF or Excel format.
    The layout is designed to facilitate easy data entry and ensure all necessary information is captured.

- **Bottom Section**: 
    The bottom section includes navigation links or buttons to other relevant pages, such as the Purchase Order History page. It may also contain additional information or tips for users.

4. **Visual Design**:
For each page within the module, provide:

- **Detailed Description**: 
    The visual design follows a clean and professional look, using the specified color scheme and typography. The layout is structured to ensure readability and ease of use. Key elements include:
    - Consistent use of the primary color (#FFA500) for buttons and links.
    - A light grey background (#F5F5F5) to provide contrast and focus on the form elements.
    - Dark grey text (#333333) for readability.
    - Adequate spacing between form elements to avoid clutter and enhance usability.

5. **File and Component Structure**:
FOR THE OVERALL MODULE:
- **Module Files**: 
    Organize all related files within a single directory named `PurchaseOrders`. This directory includes:
    - `PurchaseOrderForm.jsx`: The main component for the Purchase Order Form page.
    - `PurchaseOrderHistory.jsx`: The main component for the Purchase Order History page.
    - `components/`: A subdirectory containing reusable components like TextInput, Table, Button, and SignatureField.
    - `styles/`: A subdirectory containing CSS or styled-components for consistent styling.

- **Component Usage**: 
    Provide guidance on importing and using components within the module. Emphasize reusability and consistency throughout the module. Reference existing components where applicable to avoid duplication.
    - Example:
        ```jsx
        import TextInput from 'components/TextInput';
        import Table from 'components/Table';
        import Button from 'components/Button';
        import SignatureField from 'components/SignatureField';
        ```

---

**Page Title and Description**:
- **Title**: Purchase Order History
- **Description**: 
    The Purchase Order History page allows users to view a list of past purchase orders. The target audience includes procurement team members who need to track orders, finance team members who need to verify them, and managers who need to review them. Key features include a table displaying past purchase orders, options to view detailed information, and buttons to view the PDF/Excel version of specific orders.

- **Component Details**:
    - **General Description**: 
        - **Table**: Used for displaying the list of past purchase orders with columns for date, company name, and status.
        - **Button**: Used for actions like "View PDF" and "View Excel".
    - **Layout**: 
        The layout follows a tabular design with columns for different attributes of the purchase orders. Action buttons are placed within the table rows for easy access.
    - **Interactions**: 
        - Users can click on table rows to view detailed information about a specific purchase order.
        - Users can click the Button components to view the PDF/Excel version of the selected purchase order.
    - **Styling Requirements**: 
        - **Primary Colour**: #FFA500 (Orange)
        - **Secondary Colour**: #FFFFFF (White)
        - **Accent Colour**: #000000 (Black)
        - **Background Colour**: #F5F5F5 (Light Grey)
        - **Text Colour**: #333333 (Dark Grey)
        - **Link Colour**: #FFA500 (Orange)
        - Fonts: Use a consistent font family with sizes ranging from 14px to 18px for readability.

- **Component Implementation**:
    - **Integration**: 
        - Import and use the Table and Button components within the history page.
        - Ensure reusability by adhering to the overall design system and avoiding redundant details.
        - Example:
            ```jsx
            import Table from 'components/Table';
            import Button from 'components/Button';

            const PurchaseOrderHistory = () => {
                return (
                    <div className="purchase-order-history">
                        <Table>
                            {/* Table rows with purchase order details */}
                            <tr>
                                <td>Date</td>
                                <td>Company Name</td>
                                <td>Status</td>
                                <td>
                                    <Button label="View PDF" />
                                    <Button label="View Excel" />
                                </td>
                            </tr>
                        </Table>
                    </div>
                );
            };
            ```

3. **Page Layout and Design**:
For each page within the module, provide:

- **Top Section**: 
    The top section includes a header with the page title "Purchase Order History" and a brief description of the page's purpose. It sets the context for the user and provides navigation links to other pages, such as the Purchase Order Form page.

- **Content Area**: 
    The main content area contains the table displaying past purchase orders. It includes:
    - Columns for date, company name, and status.
    - Action buttons within each row for viewing the PDF/Excel version of the purchase order.
    The layout is designed to facilitate easy tracking and management of past orders.

- **Bottom Section**: 
    The bottom section includes navigation links or buttons to other relevant pages, such as the Purchase Order Form page. It may also contain additional information or tips for users.

4. **Visual Design**:
For each page within the module, provide:

- **Detailed Description**: 
    The visual design follows a clean and professional look, using the specified color scheme and typography. The layout is structured to ensure readability and ease of use. Key elements include:
    - Consistent use of the primary color (#FFA500) for buttons and links.
    - A light grey background (#F5F5F5) to provide contrast and focus on the table elements.
    - Dark grey text (#333333) for readability.
    - Adequate spacing between table rows to avoid clutter and enhance usability.

5. **File and Component Structure**:
FOR THE OVERALL MODULE:
- **Module Files**: 
    Organize all related files within a single directory named `PurchaseOrders`. This directory includes:
    - `PurchaseOrderForm.jsx`: The main component for the Purchase Order Form page.
    - `PurchaseOrderHistory.jsx`: The main component for the Purchase Order History page.
    - `components/`: A subdirectory containing reusable components like TextInput, Table, Button, and SignatureField.
    - `styles/`: A subdirectory containing CSS or styled-components for consistent styling.

- **Component Usage**: 
    Provide guidance on importing and using components within the module. Emphasize reusability and consistency throughout the module. Reference existing components where applicable to avoid duplication.
    - Example:
        ```jsx
        import Table from 'components/Table';
        import Button from 'components/Button';
        ```

### MODULE: Assembly

1. **Module Overview**:
    - **Purpose**: 
        The Assembly module is designed to streamline the process of tracking and managing frames during the assembly process. It ensures that all frames are properly logged, deficiencies are noted, and workers can easily identify the frames they need to work on. This module supports the business objective of maintaining quality and efficiency in the assembly process by providing a structured and user-friendly interface for assembly line workers, quality control personnel, and managers.

    - **Responsibilities**: 
        The key tasks and functions handled by the Assembly module include:
        - Logging basic information such as time, date, frame details, and frame drawing.
        - Allowing workers to sign and note deficiencies.
        - Tracking and displaying deficiencies in the statistics page.
        - Ensuring seamless data exchange with other modules, particularly those related to quality control and project management.

2. **Page Details**:

    - **Page Title and Description**:
        - **Title**: Frame Logging
        - **Description**: 
            The Frame Logging page is designed for assembly line workers to log details about each frame they work on. This includes entering information such as time, date, frame number, project, and frame type. Workers can also view the frame drawing, sign off on their work, and note any deficiencies. This page ensures that all necessary information is captured accurately and efficiently, contributing to the overall quality and traceability of the assembly process.

    - **Component Details**:
        - **General Description**: 
            - **TextInput**: Used for entering text details like time, date, frame number, project, and frame type. Each TextInput component captures specific information required for logging the frame.
            - **ImageViewer**: Displays the frame drawing, allowing workers to reference it while logging details.
            - **SignatureField**: Captures the worker's signature, providing a digital record of who logged the frame.
            - **TextArea**: Allows users to note any deficiencies observed during the assembly process.
        - **Layout**: 
            The layout follows a structured form design:
            - The top section contains the TextInput components for time, date, frame number, project, and frame type, arranged in a grid format for easy data entry.
            - The middle section features the ImageViewer, centrally positioned to provide a clear view of the frame drawing.
            - The bottom section includes the SignatureField and TextArea, allowing workers to sign off and note deficiencies.
        - **Interactions**: 
            - Users interact with the TextInput components to enter details.
            - The ImageViewer is static but can be zoomed or panned if needed.
            - The SignatureField captures input via touch or mouse.
            - The TextArea allows for text input, with validation to ensure deficiencies are noted clearly.
        - **Styling Requirements**: 
            - **Primary Colour**: #FFA500 (Orange)
            - **Secondary Colour**: #FFFFFF (White)
            - **Accent Colour**: #000000 (Black)
            - **Background Colour**: #F5F5F5 (Light Grey)
            - **Text Colour**: #333333 (Dark Grey)
            - **Link Colour**: #FFA500 (Orange)
            - Fonts should be legible, with sizes ranging from 14px to 18px for input fields and labels.

    - **Component Implementation**:
        - **Integration**: 
            - Import the TextInput, ImageViewer, SignatureField, and TextArea components from the shared components library.
            - Ensure each component is properly configured to capture and validate the required data.
            - Use a form handler to manage the state and submission of the form, ensuring data is saved to a mock service or dummy data store.

    - **Page Layout and Design**:
        - **Top Section**: 
            - Contains the header with the page title "Frame Logging".
            - Includes navigation links or buttons to other pages, such as the Deficiency Tracking page.
        - **Content Area**: 
            - The main content area is divided into three sections:
                - **Input Section**: Contains TextInput components for time, date, frame number, project, and frame type.
                - **Drawing Section**: Features the ImageViewer for displaying the frame drawing.
                - **Signature and Deficiency Section**: Includes the SignatureField and TextArea for capturing the worker's signature and noting deficiencies.
        - **Bottom Section**: 
            - Contains the form submission button, styled to match the primary colour scheme.
            - Includes any additional navigation links or buttons for user convenience.

    - **Visual Design**:
        - **Detailed Description**: 
            The visual design of the Frame Logging page follows a clean and structured layout, with a focus on usability and clarity. The primary colour (orange) is used for buttons and highlights, while the background is light grey to reduce eye strain. Text is dark grey for readability, and the overall design adheres to a consistent and professional aesthetic.

3. **Page Title and Description**:
    - **Title**: Deficiency Tracking
    - **Description**: 
        The Deficiency Tracking page is designed for quality control personnel and managers to view and manage logged deficiencies. This page displays a list or table of deficiencies, allowing users to click on specific entries to view detailed information. The objective is to provide a clear and organized view of all deficiencies, facilitating timely resolution and quality assurance.

    - **Component Details**:
        - **General Description**: 
            - **Table**: Displays the list of logged deficiencies, with columns for date, frame number, and description.
            - **Button**: Allows users to perform actions such as "View Details" for each deficiency entry.
        - **Layout**: 
            The layout is designed to present information clearly:
            - The top section contains filters and search options to help users find specific deficiencies.
            - The main content area features the Table component, with rows representing individual deficiencies.
            - Action buttons are placed next to each row for easy access.
        - **Interactions**: 
            - Users can interact with the Table to sort and filter deficiencies.
            - Clicking on a "View Details" button opens a detailed view of the selected deficiency.
        - **Styling Requirements**: 
            - **Primary Colour**: #FFA500 (Orange)
            - **Secondary Colour**: #FFFFFF (White)
            - **Accent Colour**: #000000 (Black)
            - **Background Colour**: #F5F5F5 (Light Grey)
            - **Text Colour**: #333333 (Dark Grey)
            - Fonts should be consistent with the Frame Logging page, ensuring a cohesive design.

    - **Component Implementation**:
        - **Integration**: 
            - Import the Table and Button components from the shared components library.
            - Configure the Table to fetch and display data from a mock service or dummy data store.
            - Ensure buttons are linked to appropriate actions, such as opening a detailed view of deficiencies.

    - **Page Layout and Design**:
        - **Top Section**: 
            - Contains the header with the page title "Deficiency Tracking".
            - Includes filters and search options for finding specific deficiencies.
        - **Content Area**: 
            - The main content area features the Table component, displaying a list of deficiencies.
            - Action buttons are placed next to each row for easy access to detailed views.
        - **Bottom Section**: 
            - Contains navigation links or buttons to other pages, such as the Frame Logging page.

    - **Visual Design**:
        - **Detailed Description**: 
            The visual design of the Deficiency Tracking page is consistent with the Frame Logging page, using the same colour scheme and typography. The layout is clean and organized, with a focus on presenting information clearly and facilitating user interactions.

4. **File and Component Structure**:
    - **Module Files**: 
        All related files for the Assembly module should be organized within a single directory, such as `src/modules/assembly`. This directory should contain subdirectories for components, pages, and services, ensuring a clear and logical structure.
    - **Component Usage**: 
        - Import components from the shared components library to ensure consistency and reusability.
        - Use existing components where applicable to avoid duplication and maintain a cohesive design system.
        - Ensure all components are properly documented and configured for easy integration within the module.

### MODULE: Glazing

1. **Module Overview**:
    - **Purpose**: 
        The Glazing module is designed to streamline the process of tracking and managing frames during the glazing process. It ensures that all frames are properly logged, deficiencies are noted, and workers can easily identify the frames they need to work on. This module supports the business objective of maintaining quality and efficiency in the glazing process by providing a structured and user-friendly interface for logging and tracking frames.

    - **Responsibilities**: 
        The key tasks and functions handled by the Glazing module include:
        - Logging basic information such as time, date, frame details, and frame drawing.
        - Allowing workers to sign and note deficiencies.
        - Tracking and displaying deficiencies in the statistics page.
        - Interacting with other modules for data exchange, particularly with quality control and management modules to ensure seamless integration and data consistency.

2. **Page Details**:

    **PAGE 1: Frame Logging**
    - **Page Title and Description**:
        - **Title**: Frame Logging
        - **Description**: 
            The Frame Logging page is designed for glazing line workers to log details of each frame they work on. This includes entering basic information such as time, date, frame number, project, and frame type. Workers can also view the frame drawing, sign off on the frame, and note any deficiencies. This page ensures that all necessary information is captured accurately and efficiently, facilitating quality control and tracking.

    - **Component Details**:
        - **General Description**: 
            - **TextInput**: Used for entering text details like time, date, frame number, project, and frame type. Each TextInput component will have a label and placeholder text to guide the user.
            - **ImageViewer**: Displays the frame drawing, allowing workers to visually inspect the frame.
            - **SignatureField**: Captures the worker's signature, ensuring accountability and traceability.
            - **TextArea**: Allows users to note any deficiencies observed in the frame.
        - **Layout**: 
            The layout will follow a vertical flow, with each component stacked one after the other. The TextInput fields will be grouped together, followed by the ImageViewer, SignatureField, and TextArea. Adequate spacing will be provided between components to ensure a clean and organized appearance.
        - **Interactions**: 
            - Users will input data into the TextInput fields.
            - The ImageViewer will display the frame drawing, which can be zoomed in/out if necessary.
            - The SignatureField will allow users to draw their signature using a mouse or touch input.
            - The TextArea will enable users to type in any deficiencies.
        - **Styling Requirements**: 
            - **Primary Colour**: #FFA500 (Orange)
            - **Secondary Colour**: #FFFFFF (White)
            - **Accent Colour**: #000000 (Black)
            - **Background Colour**: #F5F5F5 (Light Grey)
            - **Text Colour**: #333333 (Dark Grey)
            - **Link Colour**: #FFA500 (Orange)
            - Fonts: Use a sans-serif font with sizes ranging from 14px to 18px for readability. Headers should be bold, while body text should be regular weight.

    - **Component Implementation**:
        - **Integration**: 
            - Import the necessary components from the UI library.
            - Use the TextInput component for each field, ensuring proper labels and placeholders.
            - Integrate the ImageViewer component to display the frame drawing.
            - Use the SignatureField component to capture signatures.
            - Implement the TextArea component for noting deficiencies.
            - Ensure all components adhere to the overall design system for consistency.

    - **Page Layout and Design**:
        - **Top Section**: 
            The top section will include a header with the page title "Frame Logging". This section will also have a brief description or instructions for the user.
        - **Content Area**: 
            The main content area will include the TextInput fields for time, date, frame number, project, and frame type, followed by the ImageViewer, SignatureField, and TextArea. Each component will be clearly labeled and spaced for ease of use.
        - **Bottom Section**: 
            The bottom section will include a submit button to save the logged information and a link or button to navigate to the Deficiency Tracking page.

    - **Visual Design**:
        - **Detailed Description**: 
            The visual design will follow a clean and modern aesthetic, using the specified color scheme and typography. The layout will be intuitive, with clear labels and adequate spacing between components. The use of orange as the primary color will highlight important elements, while the light grey background will provide a neutral backdrop.

3. **PAGE 2: Deficiency Tracking**
    - **Page Title and Description**:
        - **Title**: Deficiency Tracking
        - **Description**: 
            The Deficiency Tracking page is designed for quality control personnel and managers to view and monitor logged deficiencies. This page displays a list or table of deficiencies, allowing users to click on a specific deficiency to view its details. This functionality helps in identifying recurring issues and ensuring that all deficiencies are addressed promptly.

    - **Component Details**:
        - **General Description**: 
            - **Table**: Displays the list of logged deficiencies with columns for date, frame number, and description.
            - **Button**: Allows users to view the details of the selected deficiency.
        - **Layout**: 
            The layout will feature a table at the center of the page, with each row representing a logged deficiency. Buttons will be placed within the table rows to allow users to view details.
        - **Interactions**: 
            - Users can scroll through the table to view all logged deficiencies.
            - Clicking on a button within a table row will open a detailed view of the selected deficiency.
        - **Styling Requirements**: 
            - **Primary Colour**: #FFA500 (Orange)
            - **Secondary Colour**: #FFFFFF (White)
            - **Accent Colour**: #000000 (Black)
            - **Background Colour**: #F5F5F5 (Light Grey)
            - **Text Colour**: #333333 (Dark Grey)
            - **Link Colour**: #FFA500 (Orange)
            - Fonts: Use a sans-serif font with sizes ranging from 14px to 18px for readability. Headers should be bold, while body text should be regular weight.

    - **Component Implementation**:
        - **Integration**: 
            - Import the Table and Button components from the UI library.
            - Populate the Table component with data fetched from a mock service or dummy data store.
            - Implement the Button component within each table row to allow users to view details.
            - Ensure all components adhere to the overall design system for consistency.

    - **Page Layout and Design**:
        - **Top Section**: 
            The top section will include a header with the page title "Deficiency Tracking". This section will also have a brief description or instructions for the user.
        - **Content Area**: 
            The main content area will feature the Table component displaying logged deficiencies. Each row will include details such as date, frame number, and description, along with a button to view more details.
        - **Bottom Section**: 
            The bottom section will include a link or button to navigate back to the Frame Logging page.

    - **Visual Design**:
        - **Detailed Description**: 
            The visual design will follow a clean and modern aesthetic, using the specified color scheme and typography. The layout will be intuitive, with clear labels and adequate spacing between components. The use of orange as the primary color will highlight important elements, while the light grey background will provide a neutral backdrop.

4. **File and Component Structure**:
    - **Module Files**: 
        Organize all related files within a single directory named `GlazingModule`. This directory will include subdirectories for components, pages, and services. Each subdirectory will contain files relevant to its purpose, ensuring a clear and logical structure.
    - **Component Usage**: 
        Provide guidance on importing and using components within the module. Emphasize reusability and consistency throughout the module. Reference existing components where applicable to avoid duplication. For example, the TextInput component can be reused across multiple pages, ensuring a consistent user experience.
"""

def parse_modules(input_string):
    # Split the input string into modules based on the '### MODULE' delimiter
    modules = input_string.strip().split('### MODULE')

    # Remove any empty strings from the list and prepend 'MODULE' to each module
    modules = [f"MODULE{module.strip()}" for module in modules if module.strip()]

    return modules

testList = parse_modules(parseTester)
