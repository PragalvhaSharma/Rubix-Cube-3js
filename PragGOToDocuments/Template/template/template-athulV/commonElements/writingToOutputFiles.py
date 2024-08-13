class WritingToOutputFiles:
    @staticmethod
    def writeToOutputFILE(content, filePath):
        """
        Write the provided content to codeOutputFile.txt.
        """
        try:
            with open(filePath, 'a') as file:
                file.write(content)
            print("Content successfully appended to codeOutputFile.txt")
        except Exception as e:
            print(f"An error occurred while writing to codeOutputFile.txt: {e}")
    