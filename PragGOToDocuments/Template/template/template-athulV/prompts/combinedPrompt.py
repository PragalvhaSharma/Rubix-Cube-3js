overallPlanner = """
        **Business Problem and Requirements**:
        <{businessProblem}>
        
        **Tech Stack**:
        React 18 
        
        Instructions:

        Frontend Pages:
        Each page is a self-contained unit managing specific tasks/features, e.g., "Dashboard," "User Management," etc. No backend or database integration—purely frontend logic.

        For each page, provide:
        
        ### PAGE: [PAGE NAME]

        Overview:
        - Purpose: Describe the page’s purpose, its role within the broader application, and how it addresses specific business objectives.
        - Core Functionality: Identify and detail the essential functions provided by the page. Focus on the logical processes, data handling, and user interactions that are key to fulfilling the page’s objectives.
        - Target Users: Define the primary users of this page and the specific needs or tasks they are expected to perform.

        Functional Specification:
        - Key Features: List and describe the core features within the page. Emphasize functionality, including:
        - Data Handling: How data is processed, stored in memory, and manipulated within the page.
        - User Interactions: Describe how users will interact with the features (e.g., form inputs, drag-and-drop, selection, etc.), and the expected outcomes of these interactions.
        - Business Logic Implementation: Outline any rules, calculations, or decision-making processes that are crucial for the page’s operation.
        - State Management: Explain how the page manages state, including the flow of data between components and how the state changes in response to user actions.

        - Component Breakdown:
        - Core Components: Identify the main components within the page, detailing their purpose, functionality, and how they interact with each other.
        - Reusable Components: Highlight any components that can be reused across different parts of the page or other pages within the module.
        - Component Interactions: Elaborate on how data flows between components, and how user interactions trigger changes in component behavior or state.

        Navigation Flow:
        - Intra-Page Navigation: Describe how users navigate between different sections or components within the page. Detail the logic behind navigation and any state persistence or data transfer that occurs during navigation.

        Styling (For Contextual Consistency):
        - General Colour Scheme: (Optional – For reference)
        - Primary Colour: [Hex Code]
        - Secondary Colour: [Hex Code]
        - Accent Colour: [Hex Code]
        - Background Colour: [Hex Code]
        - Text Colour: [Hex Code]
        - Link Colour: [Hex Code]
        
        **Action Required:**
        Generate a detailed plan for each page, focusing on functionality, components, user interactions, and navigation within the page.

        MENTION FILE PATHS WITHIN EACH PAGE THAT ARE RELEVANT.
        """
